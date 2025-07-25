# Image Compressor

A small personal project to compress images locally — mostly because I didn't want to rely on sketchy online tools.

## What it does
- Upload JPG/PNG/WEBP images
- Set max quality thresholds
- View and download the compressed result

## Setup Guide

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Installation

1. **Clone or download the project**
   ```bash
   git clone https://github.com/aadhirvivek22/image-processor
   cd image-compressor
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Streamlit app**
   ```bash
   streamlit run app.py
   ```

4. **Open your browser**
   Go to `http://localhost:8501` (however generally the browser opens up automatically)

### Usage

1. **Upload an image**: Click the upload button and select a JPG, PNG, or WEBP file
2. **Set quality**: Adjust the quality slider to your desired compression level
3. **Preview**: View the compressed result in real-time
4. **Download**: Save the compressed image to your device

### Building for Production

```bash
streamlit run app.py
```

### Dependencies

- Streamlit
- Pillow

## Maybe later
- Support more formats (HEIC, etc.)
- Batch compression
- Side-by-side visual comparison

---

Feel free to use or tweak it if it helps.