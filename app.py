from flask import Flask, render_template, request, send_file
from PIL import Image
import io
import os
import zipfile

app = Flask(__name__)


def resize_image(image, max_size, format="PNG"):
    original_width, original_height = image.size
    ratio = min(max_size / original_width, max_size / original_height)
    new_width = int(original_width * ratio)
    new_height = int(original_height * ratio)
    return image.resize((new_width, new_height), Image.ANTIALIAS)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        max_size = int(request.form.get("max_size", 80))
        uploaded_images = request.files.getlist("images")

        if len(uploaded_images) == 1:
            # 如果只有一个文件，直接下载图片
            uploaded_image = uploaded_images[0]
            image = Image.open(uploaded_image)
            resized_image = resize_image(
                image, max_size, format=request.form.get("format", "PNG")
            )
            output = io.BytesIO()
            resized_image.save(output, format=request.form.get("format", "PNG"))
            output.seek(0)
            return send_file(
                output,
                as_attachment=True,
                download_name=uploaded_image.filename,
                mimetype="image/png",
            )

        else:
            # 如果有多个文件，将它们打包成一个 ZIP 文件并下载
            output_zip = io.BytesIO()
            with zipfile.ZipFile(output_zip, "w") as zipf:
                for uploaded_image in uploaded_images:
                    image = Image.open(uploaded_image)
                    resized_image = resize_image(
                        image, max_size, format=request.form.get("format", "PNG")
                    )
                    temp_output = io.BytesIO()
                    resized_image.save(
                        temp_output, format=request.form.get("format", "PNG")
                    )
                    zipf.writestr(uploaded_image.filename, temp_output.getvalue())

            output_zip.seek(0)
            return send_file(
                output_zip,
                as_attachment=True,
                download_name="resized_images.zip",
                mimetype="application/zip",
            )

    return render_template("index.html")


@app.route("/download")
def download():
    return render_template("download.html")


if __name__ == "__main__":
    app.run(debug=True)
