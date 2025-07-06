import os
import tempfile
from pathlib import Path
from PyPDF2 import PdfReader, PdfWriter, PdfMerger
import ocrmypdf
import streamlit as st

st.set_page_config(page_title="OCR PDF Converter", layout="centered")
st.title("📄 Convert Scanned PDF to Searchable PDF")

OUTPUT_DIR = Path("output")
OUTPUT_DIR.mkdir(exist_ok=True)

if "processing" not in st.session_state:
    st.session_state.processing = False
if "ocr_done" not in st.session_state:
    st.session_state.ocr_done = False
if "output_path" not in st.session_state:
    st.session_state.output_path = ""

uploaded_file = st.file_uploader("📤 Upload scanned PDF (≤200 MB)", type=["pdf"], key="uploader")

if uploaded_file and not st.session_state.processing:
    st.markdown(f"**Selected file:** `{uploaded_file.name}`")
    if st.button("▶️ Start OCR"):
        st.session_state.processing = True

if uploaded_file and st.session_state.processing and not st.session_state.ocr_done:
    try:
        st.info("📥 Saving uploaded PDF temporarily…")
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
            tmp.write(uploaded_file.read())
            input_path = Path(tmp.name)

        reader = PdfReader(str(input_path))
        total_pages = len(reader.pages)
        st.info(f"🔍 Detected {total_pages} pages")

        progress_bar = st.progress(0)
        percent_complete = 0

        merger = PdfMerger()
        for i in range(total_pages):
            page_path = Path(tempfile.mktemp(suffix=".pdf"))
            with open(page_path, "wb") as f:
                writer = PdfWriter()
                writer.add_page(reader.pages[i])
                writer.write(f)

            ocr_page_path = Path(tempfile.mktemp(suffix=".pdf"))
            ocrmypdf.ocr(
                input_file=str(page_path),
                output_file=str(ocr_page_path),
                language="eng",
                deskew=True,
                skip_text=True,
                output_type="pdf",
                jobs=1,
                progress_bar=False,
            )

            # Append to final merged file
            merger.append(str(ocr_page_path))

            # Update progress bar
            percent_complete = (i + 1) / total_pages
            progress_bar.progress(percent_complete, f"OCR Progress: {int(percent_complete * 100)}%")

        # Save final merged file
        output_filename = f"OCR_{Path(uploaded_file.name).stem}.pdf"
        output_path = OUTPUT_DIR / output_filename
        with open(output_path, "wb") as f:
            merger.write(f)
        merger.close()

        input_path.unlink(missing_ok=True)

        st.session_state.ocr_done = True
        st.session_state.output_path = str(output_path)
        st.success("✅ OCR completed successfully!")

    except Exception as e:
        st.error(f"❌ Error: {e}")
        st.session_state.processing = False

def _cleanup_after_download(path: str):
    try:
        os.remove(path)
    except Exception as e:
        st.warning(f"⚠️ Could not delete output file: {e}")
    for key in ("processing", "ocr_done", "output_path", "uploader"):
        st.session_state.pop(key, None)

if st.session_state.ocr_done:
    path = st.session_state.output_path
    with open(path, "rb") as f:
        st.download_button(
            label="📥 Download Searchable PDF",
            data=f,
            file_name=Path(path).name,
            mime="application/pdf",
            on_click=_cleanup_after_download,
            args=(path,)
        )
