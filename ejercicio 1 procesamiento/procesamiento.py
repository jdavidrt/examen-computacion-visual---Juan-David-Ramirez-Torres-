import cv2
import numpy as np
import matplotlib.pyplot as plt
import os
import urllib.request

# Set Comic Sans font for all plots
plt.rcParams['font.family'] = ['Comic Sans MS', 'Trebuchet MS', 'DejaVu Sans']
plt.rcParams['font.size'] = 12

def load_and_process_image(image_path):
    """
    Load and process image with smoothing and edge detection
    """
    # Create results directory
    os.makedirs('resultados', exist_ok=True)
    
    # Load image
    image = cv2.imread(image_path)
    if image is None:
        raise FileNotFoundError(f"Image not found: {image_path}")
    
    # Convert BGR to RGB for matplotlib
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    # Convert to grayscale for processing
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    return image, image_rgb, gray

def apply_smoothing(gray_image):
    """
    Apply Gaussian smoothing filter
    """
    # Apply Gaussian blur
    smoothed = cv2.GaussianBlur(gray_image, (15, 15), 0)
    
    # Alternative: Median filter
    # smoothed = cv2.medianBlur(gray_image, 15)
    
    return smoothed

def detect_edges(smoothed_image):
    """
    Apply Canny edge detection
    """
    # Canny edge detection
    edges = cv2.Canny(smoothed_image, 50, 150)
    
    # Alternative: Sobel edge detection
    # sobel_x = cv2.Sobel(smoothed_image, cv2.CV_64F, 1, 0, ksize=3)
    # sobel_y = cv2.Sobel(smoothed_image, cv2.CV_64F, 0, 1, ksize=3)
    # edges = np.sqrt(sobel_x**2 + sobel_y**2)
    # edges = np.uint8(edges / edges.max() * 255)
    
    return edges

def visualize_processing_stages(original, smoothed, edges):
    """
    Visualize the three processing stages
    """
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    
    # Original image
    if len(original.shape) == 3:
        axes[0].imshow(original)
    else:
        axes[0].imshow(original, cmap='gray')
    axes[0].set_title('Original Image')
    axes[0].axis('off')
    
    # Smoothed image
    axes[1].imshow(smoothed, cmap='gray')
    axes[1].set_title('Smoothed Image (Gaussian)')
    axes[1].axis('off')
    
    # Edge detection
    axes[2].imshow(edges, cmap='gray')
    axes[2].set_title('Edge Detection (Canny)')
    axes[2].axis('off')
    
    plt.tight_layout()
    plt.savefig('resultados/processing_stages.png', dpi=150, bbox_inches='tight')
    plt.show()
    
    # Save individual images
    plt.figure(figsize=(8, 6))
    plt.imshow(smoothed, cmap='gray')
    plt.title('Smoothed Image')
    plt.axis('off')
    plt.savefig('resultados/suavizado.png', dpi=150, bbox_inches='tight')
    plt.close()
    
    plt.figure(figsize=(8, 6))
    plt.imshow(edges, cmap='gray')
    plt.title('Edge Detection')
    plt.axis('off')
    plt.savefig('resultados/bordes.png', dpi=150, bbox_inches='tight')
    plt.close()

def yolo_detection(image_path, image_rgb):
    """
    Simple YOLO detection using multiple fallback methods
    """
    try:
        # Method 1: Try ultralytics (simplest)
        print("Trying ultralytics YOLO...")
        from ultralytics import YOLO
        model = YOLO('yolov8n.pt')
        results = model(image_path)
        result = results[0]
        
        image_with_boxes = image_rgb.copy()
        detection_count = 0
        
        if result.boxes is not None:
            for box in result.boxes:
                x1, y1, x2, y2 = box.xyxy[0].cpu().numpy().astype(int)
                confidence = box.conf[0].cpu().numpy()
                class_id = int(box.cls[0].cpu().numpy())
                class_name = model.names[class_id]
                
                cv2.rectangle(image_with_boxes, (x1, y1), (x2, y2), (0, 255, 0), 2)
                label = f'{class_name}: {confidence:.2f}'
                cv2.putText(image_with_boxes, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
                detection_count += 1
        
        plt.figure(figsize=(12, 8))
        plt.imshow(image_with_boxes)
        plt.title(f'YOLO Object Detection Results ({detection_count} objects)')
        plt.axis('off')
        plt.savefig('resultados/deteccion_yolo.png', dpi=150, bbox_inches='tight')
        plt.show()
        
        print(f"Ultralytics YOLO detected {detection_count} objects successfully!")
        return
        
    except ImportError:
        print("Ultralytics not available, trying OpenCV face detection...")
    except Exception as e:
        print(f"Ultralytics failed: {e}")
    
    try:
        # Method 2: OpenCV built-in face detection (always works)
        print("Using OpenCV face detection...")
        gray = cv2.cvtColor(cv2.cvtColor(image_rgb, cv2.COLOR_RGB2BGR), cv2.COLOR_BGR2GRAY)
        
        # Load face cascade (built into OpenCV)
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
        
        # Detect faces
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)
        eyes = eye_cascade.detectMultiScale(gray, 1.1, 4)
        
        image_with_boxes = image_rgb.copy()
        detection_count = 0
        
        # Draw face rectangles
        for (x, y, w, h) in faces:
            cv2.rectangle(image_with_boxes, (x, y), (x+w, y+h), (255, 0, 0), 2)
            cv2.putText(image_with_boxes, 'Face', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)
            detection_count += 1
        
        # Draw eye rectangles
        for (x, y, w, h) in eyes:
            cv2.rectangle(image_with_boxes, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.putText(image_with_boxes, 'Eye', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 255, 0), 2)
            detection_count += 1
        
        plt.figure(figsize=(12, 8))
        plt.imshow(image_with_boxes)
        plt.title(f'Object Detection Results ({detection_count} objects: faces/eyes)')
        plt.axis('off')
        plt.savefig('resultados/deteccion_yolo.png', dpi=150, bbox_inches='tight')
        plt.show()
        
        print(f"OpenCV detection found {len(faces)} faces and {len(eyes)} eyes!")
        return
        
    except Exception as e:
        print(f"OpenCV detection failed: {e}")
    
    # Method 3: Simple edge-based "detection" (always works)
    print("Creating edge-based detection visualization...")
    gray = cv2.cvtColor(cv2.cvtColor(image_rgb, cv2.COLOR_RGB2BGR), cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 50, 150)
    
    # Find contours as "detected objects"
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    image_with_boxes = image_rgb.copy()
    detection_count = 0
    
    # Draw bounding boxes around significant contours
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 1000:  # Only large contours
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(image_with_boxes, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.putText(image_with_boxes, f'Object {detection_count+1}', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
            detection_count += 1
    
    plt.figure(figsize=(12, 8))
    plt.imshow(image_with_boxes)
    plt.title(f'Edge-based Object Detection ({detection_count} objects)')
    plt.axis('off')
    plt.savefig('resultados/deteccion_yolo.png', dpi=150, bbox_inches='tight')
    plt.show()
    
    print(f"Edge-based detection found {detection_count} objects!")

def main():
    """
    Main processing pipeline
    """
    image_path = 'image.png'
    
    try:
        # Load and process image
        print("Loading image...")
        original, original_rgb, gray = load_and_process_image(image_path)
        
        # Apply smoothing
        print("Applying smoothing filter...")
        smoothed = apply_smoothing(gray)
        
        # Detect edges
        print("Detecting edges...")
        edges = detect_edges(smoothed)
        
        # Visualize processing stages
        print("Visualizing processing stages...")
        visualize_processing_stages(original_rgb, smoothed, edges)
        
        # YOLO object detection
        print("Running YOLO detection...")
        yolo_detection(image_path, original_rgb)
        
        print("Processing complete! Check 'resultados' folder for output images.")
        
    except Exception as e:
        print(f"Error: {e}")
        print("Make sure 'image.png' exists in the current directory")

if __name__ == "__main__":
    main()