# Exercise 1: Image Processing and Object Detection

## Description

Complete image processing pipeline implementing smoothing filters, edge detection, and YOLO object detection on a provided test image.

## Implementation

### Image Processing Pipeline

1. **Image Loading**: OpenCV imread with RGB conversion for matplotlib compatibility
2. **Gaussian Smoothing**: 15x15 kernel applied to reduce noise and prepare for edge detection
3. **Canny Edge Detection**: Threshold values 50-150 for optimal edge highlighting
4. **Visualization**: Three-stage comparison showing original, smoothed, and edge-detected images

### Object Detection System

- **Primary Method**: Ultralytics YOLOv8 for modern object detection
- **Fallback Method**: OpenCV face/eye detection using Haar cascades
- **Final Fallback**: Edge-based contour detection for guaranteed results
- **Output**: Bounding boxes with confidence scores and class labels

## Technical Details

### Libraries Used

- `opencv-python`: Image processing and computer vision operations
- `matplotlib`: Visualization and plot generation with Comic Sans font styling
- `ultralytics`: YOLOv8 model implementation (when available)
- `numpy`: Numerical operations and array handling

### Key Features

- **Robust Detection**: Triple-fallback system ensures successful object detection
- **Professional Visualization**: Comic Sans font styling for consistent visual presentation
- **Error Handling**: Graceful degradation when external models fail
- **Multiple Output Formats**: Individual images plus combined comparison view

## Files Generated

- `suavizado.png`: Gaussian smoothed image result
- `bordes.png`: Canny edge detection visualization
- `deteccion_yolo.png`: Object detection with bounding boxes
- `processing_stages.png`: Combined three-stage comparison

## Usage

```bash
python procesamiento.py
```

**Requirements**: Image file named `image.png` in the same directory.

## Results

The processing pipeline successfully demonstrates fundamental computer vision techniques:

- **Noise Reduction**: Gaussian smoothing effectively reduces image noise while preserving important features
- **Edge Enhancement**: Canny algorithm highlights object boundaries and structural elements
- **Object Recognition**: Detection system identifies and localizes objects with confidence metrics
- **Visual Documentation**: Clear progression showing each processing stage with professional styling
