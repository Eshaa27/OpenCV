# Basic OpenCV

> A practical collection of beginner-friendly OpenCV examples built with Python.

This repository is a small learning project for exploring core computer-vision operations: loading images and video, drawing, resizing, blurring, thresholding, contours, edge detection, and webcam-based colour detection.

## Highlights

- Image, video, and webcam input with OpenCV
- Basic image transformations and drawing tools
- Blur, threshold, contour, and edge-detection examples
- HSV colour-range detection with a live webcam feed

## Project structure

```text
.
├── assets/
│   ├── images/             # Sample input images
│   └── videos/             # Sample input videos
├── src/                    # Standalone Python examples
├── requirements.txt        # Project dependencies
└── README.md
```

## Getting started

### 1. Clone the repository

```bash
git clone https://github.com/Eshaa27/OpenCV.git
cd OpenCV
```

### 2. Create and activate a virtual environment *(recommended)*

```bash
python -m venv .venv
```

**Windows**

```bash
.venv\Scripts\activate
```

**macOS / Linux**

```bash
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run an example

Run commands from the project root:

```bash
python src/edge_detection.py
```

Press any key while an image window is open to close it. For webcam examples, press `q` to quit.

## Examples

| File | Demonstrates |
| --- | --- |
| `io_image.py` | Loading and displaying an image |
| `io_video.py` | Playing a video file |
| `io_webcam.py` | Reading frames from a webcam |
| `drawing.py` | Adding text and shapes to an image |
| `cropping.py` / `resizing.py` | Cropping and resizing images |
| `blurring.py` | Average, Gaussian, and median blurring |
| `colorspacing.py` | Converting BGR images to grayscale, RGB, and HSV |
| `threshold.py` | Binary and adaptive thresholding |
| `contours.py` | Finding contours and bounding rectangles |
| `edge_detection.py` | Canny edges, dilation, and erosion |
| `colordetection.py` | Live green-object detection using HSV |

## Requirements

- Python 3.9 or newer
- A webcam for `io_webcam.py` and `colordetection.py`

## Notes

The files in `src/` are intentionally small and independent, so you can run, modify, and learn from each example on its own.

---

Built for learning with [OpenCV](https://opencv.org/).
