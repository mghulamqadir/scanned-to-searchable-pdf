# 🧾 Scanned to Searchable PDF

Convert scanned PDF documents into **searchable**, **OCR-processed**, and **PDF/A-2 compliant** files using [`ocrmypdf`](https://ocrmypdf.readthedocs.io/).  
Supports **parallel processing** to handle large documents efficiently.

---

## 📌 Features

- ✅ Converts scanned PDFs to searchable PDFs
- ✅ Skips pages that already contain text (`skip_text=True`)
- ✅ Uses all CPU cores for faster processing (`jobs=N`)
- ✅ Output is **PDF/A-2 compliant** for long-term archival
- ✅ Batch processes all PDFs in the `input/` directory

---

## 📁 Folder Structure

```
scanned-to-searchable-pdf/
├── input/                # Place all scanned PDFs here
├── output/               # Processed searchable PDFs will be saved here
├── main.py               # Main script
└── README.md             # This file

````

---

## 🛠️ Installation

### ✅ 1. Clone the Repository

```bash
git clone https://github.com/mghulamqadir/scanned-to-searchable-pdf.git
cd scanned-to-searchable-pdf
````

---

### ✅ 2. Setup Python Environment

#### 🔹 Ubuntu/Linux

```bash
sudo apt update
sudo apt install python3 python3-venv python3-pip ghostscript tesseract-ocr -y

# Create virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install --upgrade pip
pip install ocrmypdf
```

#### 🔹 Windows

1. ✅ Install [Python 3.10+](https://www.python.org/downloads/)
2. ✅ Install [Tesseract OCR for Windows](https://github.com/tesseract-ocr/tesseract/wiki#windows):

   * Download from [UB Mannheim builds](https://github.com/UB-Mannheim/tesseract/wiki)
   * Add Tesseract to your **System PATH**
3. ✅ Install [Ghostscript for Windows](https://www.ghostscript.com/download/gsdnld.html):

   * Add `gswin64c.exe` to your PATH
4. ✅ Open Command Prompt:

```cmd
python -m venv .venv
.venv\Scripts\activate
pip install --upgrade pip
pip install ocrmypdf
```

---

## ▶️ Usage

1. Place your scanned PDF files in the `input/` folder.
2. Run the script:

```bash
python main.py
```

3. Processed PDFs will appear in the `output/` directory, prefixed with `OCR_`.

---

## ⚙️ Configuration

* `language="eng"` — OCR language (change to `"eng+urd"` for English + Urdu, etc.)
* `output_type="pdfa-2"` — Output format; use `"pdf"` for standard PDF if PDF/A is not needed
* `skip_text=True` — Skips OCR on pages that already have selectable text
* `jobs=N` — Number of CPU cores for parallel page processing (auto-detected)

---

## 🧪 Example

```python
ocrmypdf.ocr(
    input_path,
    output_path,
    language="eng",
    deskew=True,
    skip_text=True,
    output_type="pdfa-2",
    jobs=num_cores # ⚠️ it will use all core of your processor make change accordinng to your need
)
```

---

## 📄 License

This project is licensed under the MIT License.
OCR engine used: [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)

---

## 🤝 Contributions

Pull requests are welcome! Please open an issue first for major changes.
