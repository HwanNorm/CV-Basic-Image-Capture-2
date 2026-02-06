# CV Image Filtering

A Flask-based web application for real-time image filtering with 10 different OpenCV filters. Built for Assignment 2 of Computer Vision course.

## Result

![Image Filtering Result](result.png)

Successfully applied 10 image filters to camera feeds from ACLAB Makerspace IP cameras.

## Implemented Filters

| # | Filter | Description | File |
|---|--------|-------------|------|
| 1 | Grayscale | Convert BGR to grayscale | `Week2_Ex1_Grayscale.py` |
| 2 | Gaussian Blur | Smooth image, reduce noise | `Week2_Ex2_Gaussian.py` |
| 3 | Median Blur | Remove salt-and-pepper noise | `Week2_Ex3_MedianBlur.py` |
| 4 | Sobel X | Edge detection (X direction) | `Week2_Ex4_SobelX.py` |
| 5 | Laplacian | Edge detection (all directions) | `Week2_Ex5_Laplacian.py` |
| 6 | Sharpening | Enhance edges and details | `Week2_Ex6_Sharpening.py` |
| 7 | Bilateral | Edge-preserving smoothing | `Week2_Ex7_Bilateral.py` |
| 8 | Threshold | Binary thresholding | `Week2_Ex8_Threshold.py` |
| 9 | Erosion | Morphological erosion | `Week2_Ex9_Erosion.py` |
| 10 | Dilation | Morphological dilation | `Week2_Ex10_Dilation.py` |

## Requirements

- Python 3.8+
- OpenCV
- Flask
- NumPy

## Installation

1. Clone the repository:
```bash
git clone https://github.com/HwanNorm/CV-Image-Filtering.git
cd CV-Image-Filtering
```

2. Create and activate virtual environment:
```bash
python -m venv venv
venv\Scripts\activate  # Windows
# or
source venv/bin/activate  # Linux/Mac
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Run the application:
```bash
python app.py
```

2. Open browser and go to: http://127.0.0.1:5000

3. Connect to cameras:
   - **For IP cameras (RTSP):** Enter the RTSP URL in the input field
   - **For local webcam:** Enter `0` (or `1` for second webcam)

4. Click **Connect** to start the video stream

5. Click the camera icon to capture and process images

## Switching Filters

To test different filters, edit `process.py` and change the `CURRENT_FILTER` variable:

```python
CURRENT_FILTER = 1  # Change this number (1-10)
# 1 = Grayscale
# 2 = Gaussian Blur
# 3 = Median Blur
# 4 = Sobel X Edge Detection
# 5 = Laplacian Edge Detection
# 6 = Sharpening
# 7 = Bilateral Filter
# 8 = Threshold (Binary)
# 9 = Erosion
# 10 = Dilation
```

Then restart the app and click Capture to see the filter applied.

## Connecting to ACLAB Cameras

To replicate the setup at FUV Makerspace:

1. Connect to the **ACLAB** WiFi network

2. Enter the following RTSP URLs:
   - **Camera 1:** `rtsp://admin:ACLAB2023@192.168.8.105:554/Streaming/channels/101`
   - **Camera 2:** `rtsp://admin:ACLAB2023@192.168.8.106:554/Streaming/channels/101`

3. Click **Connect** for each camera

## Camera Source Formats

| Type | Format | Example |
|------|--------|---------|
| RTSP | `rtsp://user:pass@ip:port/path` | `rtsp://admin:password@192.168.1.100:554/Streaming/channels/101` |
| HTTP | `http://ip:port/path` | `http://192.168.1.100:8080/video` |
| Webcam | `0`, `1`, etc. | `0` (default camera) |

## Project Structure

```
CV-Image-Filtering/
├── app.py                      # Flask web server & routes
├── camera.py                   # Video camera handler (threading)
├── process.py                  # Image processing pipeline
├── templates/
│   └── index.html              # Web interface
├── static/
│   ├── main.js                 # Frontend JavaScript
│   └── style.css               # Styling
├── Week1_Capturering/
│   └── Week1_captureSaveImg.py # Image capture & save
├── Week2_Filtering/
│   ├── Week2_Ex1_Grayscale.py  # Grayscale filter
│   ├── Week2_Ex2_Gaussian.py   # Gaussian blur
│   ├── Week2_Ex3_MedianBlur.py # Median blur
│   ├── Week2_Ex4_SobelX.py     # Sobel X edge detection
│   ├── Week2_Ex5_Laplacian.py  # Laplacian edge detection
│   ├── Week2_Ex6_Sharpening.py # Sharpening filter
│   ├── Week2_Ex7_Bilateral.py  # Bilateral filter
│   ├── Week2_Ex8_Threshold.py  # Binary threshold
│   ├── Week2_Ex9_Erosion.py    # Erosion
│   └── Week2_Ex10_Dilation.py  # Dilation
├── CapturedImage/              # Saved captures
└── requirements.txt            # Dependencies
```

## Author

HwanNorm - Fulbright University Vietnam, Spring 2026
