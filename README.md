# 🧾 Scanned to Searchable PDF (Web App)

Convert scanned PDF documents into **searchable**, **OCR-processed**, and **PDF/A-2 compliant** files using [`ocrmypdf`](https://ocrmypdf.readthedocs.io/), powered by an interactive **Streamlit** interface.
Supports **parallel processing** to handle large documents efficiently.

---

## 📌 Features

* ✅ Upload scanned PDFs via browser
* ✅ Converts scanned PDFs to searchable PDFs (with selectable text)
* ✅ Skips pages that already contain text (`skip_text=True`)
* ✅ Uses all CPU cores minus 2 for fast parallel processing (`jobs=N`)
* ✅ Output is **PDF/A-2 compliant** for long-term archival
* ✅ Instant download of processed PDF from the browser
* ✅ Fully cross-platform (works on Linux, Windows, macOS)

---

## 📁 Folder Structure

```
scanned-to-searchable-pdf/
├── output/               # Searchable PDFs saved here
├── app.py                # Streamlit OCR web app
├── README.md             # This file
```

---

## 🛠️ Installation

### ✅ 1. Clone the Repository

```bash
git clone https://github.com/mghulamqadir/scanned-to-searchable-pdf.git
cd scanned-to-searchable-pdf
```

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
pip install ocrmypdf streamlit PyPDF2
```

#### 🔹 Windows

1. ✅ Install [Python 3.10+](https://www.python.org/downloads/)
2. ✅ Install [Tesseract OCR for Windows](https://github.com/UB-Mannheim/tesseract/wiki)

   * Add Tesseract to your **System PATH**
3. ✅ Install [Ghostscript for Windows](https://www.ghostscript.com/download/gsdnld.html)

   * Add `gswin64c.exe` to your PATH
4. ✅ Create and activate a virtual environment:

```cmd
python -m venv .venv
.venv\Scripts\activate
pip install --upgrade pip
pip install ocrmypdf streamlit PyPDF2
```

---

## ▶️ Usage

1. Run the Streamlit app:

```bash
streamlit run app.py
```

2. Open the browser and upload your scanned PDF.
3. Click **Start OCR** to begin processing.
4. Download the searchable output once finished.

---

## ⚙️ Configuration Notes

* `language="eng"` — OCR language (you can change to `"eng+urd"` for English + Urdu, etc.)
* `output_type="pdfa-2"` — Output format (`pdfa-2` is for archival)
* `skip_text=True` — Skips OCR for pages with existing text
* `jobs=N` — Number of CPU cores to use (`cpu_count() - 2` is used for balance)

---

## 🧪 Behind the Scenes

The core OCR functionality uses the following:

```python
ocrmypdf.ocr(
    input_file=str(input_path),
    output_file=str(output_path),
    language="eng",
    deskew=True,
    skip_text=True,
    output_type="pdfa-2",
    jobs=multiprocessing.cpu_count() - 2 # Use all cores minus 2 for balance
)
```

---

## 📄 License

This project is licensed under the MIT License.
OCR engine used: [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)

---

## 🤝 Contributions

Pull requests are welcome! Please open an issue first if you're planning major changes.
