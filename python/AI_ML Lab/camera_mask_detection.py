#!/usr/bin/env python3
"""
Face Mask Detection with Camera
===============================
Real-time face mask detection using trained model
"""

import cv2
import numpy as np
import os
from pathlib import Path

def main():
    print("🎭 FACE MASK DETECTION - CAMERA TEST")
    print("=" * 40)
    
    # Look for the trained model
    model_paths = [
        "face_mask_detector_ready.h5",
        "../face_mask_detector_ready.h5", 
        "../../face_mask_detector_ready.h5"
    ]
    
    model = None
    model_path = None
    
    for path in model_paths:
        if Path(path).exists():
            model_path = path
            print(f"✅ Found model: {path}")
            break
    
    if model_path:
        try:
            import tensorflow as tf
            print("🔄 Loading model...")
            model = tf.keras.models.load_model(model_path)
            print("✅ Model loaded successfully!")
            print(f"📊 Model input shape: {model.input_shape}")
        except Exception as e:
            print(f"⚠️  Could not load model: {e}")
            model = None
    else:
        print("⚠️  No trained model found - using face detection only")
    
    # Initialize OpenCV
    print("\n📹 Setting up camera and face detection...")
    
    # Load face cascade
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    
    # Initialize camera
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        print("❌ Cannot open camera")
        return
    
    # Set camera resolution
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    
    print("✅ Camera ready!")
    print("\n🎮 CONTROLS:")
    print("   - Press 'q' to quit")
    print("   - Press 's' to save screenshot") 
    print("   - Press SPACE to toggle info display")
    
    show_info = True
    frame_count = 0
    
    print("\n🚀 Starting real-time detection...")
    
    while True:
        ret, frame = cap.read()
        
        if not ret:
            break
            
        frame_count += 1
        
        # Convert to grayscale for face detection
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # Detect faces
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)
        
        # Process each detected face
        for (x, y, w, h) in faces:
            
            # Extract face region
            face_img = frame[y:y+h, x:x+w]
            
            label = "Face Detected"
            color = (255, 0, 0)  # Blue default
            confidence = 0.0
            
            # If model is loaded, make prediction
            if model is not None:
                try:
                    # Preprocess face for model
                    face_resized = cv2.resize(face_img, (224, 224))
                    face_array = np.expand_dims(face_resized, axis=0)
                    face_array = face_array / 255.0
                    
                    # Make prediction
                    prediction = model.predict(face_array, verbose=0)[0][0]
                    
                    # Interpret result (remember: mask=0, no_mask=1 from training)
                    if prediction < 0.5:  # Mask class
                        label = f"MASK"
                        color = (0, 255, 0)  # Green
                        confidence = 1 - prediction
                    else:  # No mask class
                        label = f"NO MASK"
                        color = (0, 0, 255)  # Red
                        confidence = prediction
                        
                    label += f" ({confidence:.2f})"
                    
                except Exception as e:
                    label = f"Error: {str(e)[:20]}..."
                    color = (0, 255, 255)  # Yellow
            
            # Draw bounding box
            cv2.rectangle(frame, (x, y), (x+w, y+h), color, 2)
            
            # Draw label background
            (text_width, text_height), _ = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.7, 2)
            cv2.rectangle(frame, (x, y-text_height-10), (x+text_width, y), color, -1)
            
            # Draw label text
            cv2.putText(frame, label, (x, y-5), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
        
        # Add info overlay
        if show_info:
            info_y = 30
            cv2.putText(frame, f"Model: {'✅ Active' if model else '❌ Face Only'}", 
                       (10, info_y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 255), 2)
            
            cv2.putText(frame, f"Faces: {len(faces)} | Frame: {frame_count}", 
                       (10, info_y + 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
            
            cv2.putText(frame, "Controls: q=quit, s=save, space=toggle", 
                       (10, frame.shape[0] - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
        
        # Display frame
        cv2.imshow('Face Mask Detection', frame)
        
        # Handle keyboard input
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break
        elif key == ord('s'):
            filename = f"face_mask_detection_{frame_count:06d}.jpg"
            cv2.imwrite(filename, frame)
            print(f"📸 Screenshot saved: {filename}")
        elif key == ord(' '):  # Space bar
            show_info = not show_info
            print(f"ℹ️  Info display: {'ON' if show_info else 'OFF'}")
    
    # Cleanup
    cap.release()
    cv2.destroyAllWindows()
    
    print(f"\n📊 SESSION SUMMARY:")
    print(f"   - Total frames processed: {frame_count:,}")
    print(f"   - AI Model status: {'✅ Active' if model else '❌ Not loaded'}")
    if model:
        print(f"   - Model file: {model_path}")
    print("✅ Face mask detection session completed!")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Detection stopped by user (Ctrl+C)")
    except Exception as e:
        print(f"\n❌ Error occurred: {e}")
        import traceback
        traceback.print_exc()