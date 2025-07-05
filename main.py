import os
import ocrmypdf
import multiprocessing

# Set input and output directories
input_dir = "input"
output_dir = "output"

# Use all available CPU cores
num_cores = multiprocessing.cpu_count()

# Create output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

for filename in os.listdir(input_dir):
    if filename.lower().endswith(".pdf"):
        input_path = os.path.join(input_dir, filename)
        output_path = os.path.join(output_dir, f"OCR_{filename}")

        print(f"\n🔄 Processing: {filename} using {num_cores} cores")
        try:
            ocrmypdf.ocr(
                input_path,
                output_path,
                language="eng",
                deskew=True,
                skip_text=True,
                output_type="pdfa-2",
                jobs=num_cores  # ✅ this enables parallel processing
            )
            print(f"✅ OCR complete for: {filename}")
        except Exception as e:
            print(f"❌ Error processing {filename}: {e}")
