# Image Resizer Web Application

## [English](#english-version) | [中文](#中文版本) | [日本語](#日本語版)

---

### English Version

This is a simple web application built with Flask that allows users to resize images uploaded from their device.

#### How to Use

1. Clone this repository to your local machine.
2. Navigate to the project directory.
3. Install the required dependencies by running `pip install -r requirements.txt`.
4. Run the Flask application by executing `python app.py`.
5. Open your web browser and go to [http://localhost:5000/](http://localhost:5000/).
6. You will see a form where you can upload an image file (`jpg`, `jpeg`, `png`, etc.).
7. Enter the maximum size (in pixels) you want for the image, and optionally specify the width and/or height.
8. Click the "Resize Image" button.
9. The resized image will be downloaded automatically.

#### Files and Directories

- `app.py`: This is the main Python script that defines the Flask application.
- `templates/index.html`: This HTML file contains the form for uploading images and specifying resizing parameters.
- `requirements.txt`: This file lists all the Python dependencies required for the application.

#### Dependencies

- Flask: Used to create the web application.
- Pillow: Python Imaging Library fork used for image processing.

#### Notes

- Make sure to have the required dependencies installed before running the application.
- Images will be resized proportionally based on the provided maximum size. You can also specify the width and/or height.
- Resized images will be downloaded automatically with the filename `resized_image.png`.

---

### 中文版本

这是一个使用 Flask 构建的简单 Web 应用，允许用户调整上传到其设备的图像的大小。

#### 如何使用

1. 将此存储库克隆到本地计算机。
2. 导航至项目目录。
3. 运行 `pip install -r requirements.txt` 安装所需的依赖项。
4. 通过执行 `python app.py` 启动 Flask 应用。
5. 打开您的 Web 浏览器并转到 [http://localhost:5000/](http://localhost:5000/)。
6. 您将看到一个表单，您可以在其中上传图像文件（`jpg`、`jpeg`、`png` 等）。
7. 输入您希望图像的最大尺寸（以像素为单位），并可选择指定宽度和/或高度。
8. 单击“调整图像”按钮。
9. 调整后的图像将自动下载。

#### 文件和目录

- `app.py`：定义 Flask 应用的主要 Python 脚本。
- `templates/index.html`：此 HTML 文件包含用于上传图像和指定调整大小参数的表单。
- `requirements.txt`：列出了应用程序所需的所有 Python 依赖项。

#### 依赖项

- Flask：用于创建 Web 应用程序。
- Pillow：用于图像处理的 Python Imaging Library 分支。

#### 注意事项

- 在运行应用程序之前，请确保已安装所需的依赖项。
- 图像将根据提供的最大尺寸按比例调整大小。您还可以指定宽度和/或高度。
- 调整大小后的图像将以文件名 `resized_image.png` 自动下载。

---

### 日本語版

これは Flask を使用して構築されたシンプルな Web アプリケーションで、ユーザーがデバイスにアップロードした画像のサイズを調整できます。

#### 使い方

1. このリポジトリをローカルマシンにクローンします。
2. プロジェクトディレクトリに移動します。
3. `pip install -r requirements.txt` を実行して必要な依存関係をインストールします。
4. `python app.py` を実行して Flask アプリケーションを起動します。
5. Web ブラウザを開き、[http://localhost:5000/](http://localhost:5000/) に移動します。
6. 画像をアップロードするためのフォームが表示されます（`jpg`、`jpeg`、`png` など）。
7. 画像の最大サイズ（ピクセル単位）を入力し、幅と/または高さを指定することもできます。
8. "画像をリサイズ" ボタンをクリックします。
9. リサイズされた画像が自動的にダウンロードされます。

#### ファイルとディレクトリ

- `app.py`：Flask アプリケーションを定義するメインの Python スクリプトです。
- `templates/index.html`：画像をアップロードし、サイズ変更パラメータを指定するためのフォームが含まれる HTML ファイルです。
- `requirements.txt`：アプリケーションに必要なすべての Python 依存関係がリストされています。

#### 依存関係

- Flask：Web アプリケーションの作成に使用されます。
- Pillow：画像処理に使用される Python Imaging Library のフォーク。

#### 注意事項

- アプリケーションを実行する前に、必要な依存関係がインストールされていることを確認してください。
- 画像は指定された最大サイズに比例してリサイズされます。幅と/または高さも指定できます。
- リサイズされた画像は自動的に `resized_image.png` というファイル名でダウンロードされます。
