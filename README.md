# 🧾 Scanned to Searchable PDF (Web App)

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mghulamqadir/scanned-to-searchable-pdf/blob/colab/app-colab.py.ipynb)

Convert scanned PDF documents into **searchable**, **OCR-processed**, and **PDF/A-2 compliant** files using [`ocrmypdf`](https://ocrmypdf.readthedocs.io/), powered by an interactive **Streamlit** interface.
Supports **parallel processing** to handle large documents efficiently.

---

## 📌 Features

* ✅ Upload scanned PDFs via browser (local or Google Colab)
* ✅ Converts scanned PDFs to searchable PDFs (with selectable text)
* ✅ Skips pages that already contain text (`skip_text=True`)
* ✅ Uses all CPU cores minus 2 for fast parallel processing (`jobs=N`)
* ✅ Output is **PDF/A-2 compliant** for long-term archival
* ✅ Instant download of processed PDF
* ✅ Fully cross-platform (works on Linux, Windows, macOS, or Colab)

---

## 📁 Folder Structure

```
scanned-to-searchable-pdf/
├── output/               # Searchable PDFs saved here
├── app.py                # Streamlit OCR web app
├── app-colab.py.ipynb    # Google Colab version (Jupyter notebook)
├── README.md             # This file
```

---

## 🚀 Run in Google Colab

If you don’t want to install anything locally, use the hosted notebook:

👉 **[Open in Google Colab](https://colab.research.google.com/github/mghulamqadir/scanned-to-searchable-pdf/blob/colab/app-colab.py.ipynb)**

### 🔹 Colab Features:

* No setup required — ready to run in seconds
* Upload scanned PDFs and download searchable PDFs
* Uses the same `ocrmypdf` backend
* Ideal for quick OCR jobs on the go

---

## 🛠️ Installation (Local)

<details>
<summary><strong>Click to expand local setup instructions</strong></summary>

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

### 🔹 Local App

```bash
streamlit run app.py
```

### 🔹 Colab

Click the badge above or [this link](https://colab.research.google.com/github/mghulamqadir/scanned-to-searchable-pdf/blob/colab/app-colab.py.ipynb)

---

## ⚙️ Configuration Notes

* `language="eng"` — OCR language (can be changed to `"eng+urd"` for English + Urdu)
* `output_type="pdfa-2"` — Use `"pdf"` for non-archival output
* `skip_text=True` — Skips OCR on pages with existing text
* `jobs=N` — Number of CPU cores (`cpu_count() - 2` by default)

---

## 📄 License

MIT License
OCR engine: [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)

---

## 🤝 Contributions

Pull requests are welcome! Please open an issue first if you're planning major changes.
