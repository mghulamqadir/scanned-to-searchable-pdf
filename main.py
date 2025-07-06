import os
import tempfile
from pathlib import Path

import ocrmypdf
import streamlit as st
from PyPDF2 import PdfReader
import multiprocessing

# --- Streamlit page setup ---
st.set_page_config(page_title="OCR PDF Converter", layout="centered")
st.title("📄 Convert Scanned PDF to Searchable PDF")

# --- Output folder ---
OUTPUT_DIR = Path("output")
OUTPUT_DIR.mkdir(exist_ok=True)

# --- Session-state flags initialization ---
if "processing" not in st.session_state:
    st.session_state.processing = False
if "ocr_done" not in st.session_state:
    st.session_state.ocr_done = False
if "output_path" not in st.session_state:
    st.session_state.output_path = ""

# --- Upload widget ---
uploaded_file = st.file_uploader(
    "Drag & drop your scanned PDF here (≤200 MB)", 
    type=["pdf"],
    key="uploader"
)

# --- Start OCR button ---
if uploaded_file and not st.session_state.processing:
    st.markdown(f"**Selected file:** `{uploaded_file.name}`")
    if st.button("▶️ Start OCR"):
        st.session_state.processing = True

# --- OCR processing (once) ---
if uploaded_file and st.session_state.processing and not st.session_state.ocr_done:
    try:
        st.info("📤 Saving uploaded PDF to temp file…")
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
            tmp.write(uploaded_file.read())
            input_path = Path(tmp.name)

        st.info("🔢 Counting pages…")
        reader = PdfReader(str(input_path))
        total_pages = len(reader.pages)

        st.info(f"🔄 Running OCR on {total_pages} page(s)…")
        progress_bar = st.progress(0)

        # Perform OCR on the entire PDF
        output_filename = f"OCR_{Path(uploaded_file.name).stem}.pdf"
        output_path = OUTPUT_DIR / output_filename
        ocrmypdf.ocr(
            input_file=str(input_path),
            output_file=str(output_path),
            language="eng",
            deskew=True,
            skip_text=True,
            output_type="pdfa-2",
            progress_bar=False,  # Streamlit handles progress
            jobs=multiprocessing.cpu_count()-2  # Use multiple CPU cores
        )

        # Update progress to 100% upon completion
        progress_bar.progress(1.0, "OCR completed")

        # Cleanup the input temp file
        try:
            input_path.unlink()
        except:
            pass

        # Mark done
        st.session_state.ocr_done = True
        st.session_state.output_path = str(output_path)
        st.success("✅ OCR completed successfully!")

    except Exception as e:
        st.error(f"❌ Error during OCR: {e}")
        st.session_state.processing = False

# --- Download button with cleanup callback ---
def _cleanup_after_download(path: str):
    try:
        os.remove(path)
    except Exception as e:
        st.warning(f"⚠️ Could not delete output file: {e}")
    # Reset session state
    for key in ("processing", "ocr_done", "output_path", "uploader"):
        st.session_state.pop(key, None)

if st.session_state.ocr_done:
    path = st.session_state.output_path
    # Open the file once for the download button
    with open(path, "rb") as f:
        st.download_button(
            label="📥 Download Searchable PDF",
            data=f,
            file_name=Path(path).name,
            mime="application/pdf",
            on_click=_cleanup_after_download,
            args=(path,)
        )