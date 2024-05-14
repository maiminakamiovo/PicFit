from flask import Flask, render_template, request, send_file
from PIL import Image
import io
import os

app = Flask(__name__)


def resize_image(image, max_size):
    original_width, original_height = image.size
    ratio = min(max_size / original_width, max_size / original_height)
    new_width = int(original_width * ratio)
    new_height = int(original_height * ratio)
    return image.resize((new_width, new_height), Image.ANTIALIAS)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        max_size = int(request.form["max_size"])
        uploaded_image = request.files["image"]
        image = Image.open(uploaded_image)
        resized_image = resize_image(image, max_size)
        output = io.BytesIO()
        resized_image.save(output, format="PNG")
        output.seek(0)

        # 为了提供附件名，我们先将图像保存到临时文件中
        temp_file_path = "resized_image.png"
        with open(temp_file_path, "wb") as f:
            f.write(output.getvalue())

        # 发送文件并删除临时文件
        return send_file(temp_file_path, as_attachment=True)
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
