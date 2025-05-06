Here's a comprehensive `README.md` file tailored for your **QR Code Generator CLI tool (`qrgen`)**:

---

````markdown
# QRGen - QR Code Generator CLI

**QRGen** is a simple, customizable command-line tool for generating QR codes from text, URLs, or any string. It allows you to choose output filenames, image formats, and optionally preview the generated image.

---

## 📦 Features

- ✅ Generate QR codes from text, URLs, or any string
- 🖼️ Choose output format: PNG (default), JPEG, BMP
- 🔤 Input can be provided via CLI or environment variables
- 👁️ Optional auto-preview after saving
- 🧪 Easy to install and use as a CLI tool

---

## 🚀 Installation

Clone the repository and install it locally using pip:

```bash
git clone https://github.com/ialexeze/qrgen.git
cd qrgen
pip install --editable .
````

After this, you can use `qrgen` from anywhere in your terminal.

---

## 🔧 Usage

### Basic usage:

```bash
qrgen -t "https://example.com"
```

### With custom output filename and format:

```bash
qrgen -t "Hello World!" -o hello -f JPEG
```

### Disable automatic image preview:

```bash
qrgen -t "No Preview Example" --no-preview
```

---

## 🌿 Environment Variable Support

You can also use environment variables instead of CLI options:

| Variable | Description                         |
| -------- | ----------------------------------- |
| `TARGET` | Text or URL to encode               |
| `OUTPUT` | Output filename (no extension)      |
| `FORMAT` | Image format (`PNG`, `JPEG`, `BMP`) |

Example:

```bash
export TARGET="https://example.com"
export OUTPUT="site_qr"
export FORMAT="PNG"

qrgen
```

---

## 🖥️ CLI Options

```text
-h, --help            Show help message and exit
-t, --target          Content to encode (overrides TARGET env)
-o, --output          Output filename (overrides OUTPUT env)
-f, --format          Image format: PNG (default), JPEG, BMP
--no-preview          Disable image preview after saving
```

---

## 🛠️ Development

### Requirements

* Python 3.7+
* [qrcode](https://pypi.org/project/qrcode/)
* [Pillow](https://pypi.org/project/Pillow/)

Install dependencies:

```bash
pip install -r requirements.txt
```

(Or let `pip install .` manage it via `pyproject.toml`)

---

## 📄 License

MIT License © 2025 [Alex Eze](mailto:ialexeze@gmail.com)

---

![Alex QR Code](./qrgen/qr.png)

---

## 🙌 Acknowledgments

* [qrcode](https://pypi.org/project/qrcode/) for QR code generation
* [Pillow](https://python-pillow.org/) for image handling

---
