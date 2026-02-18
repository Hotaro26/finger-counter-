import cv2
import numpy as np

# Simple finger counting without MediaPipe
# Uses basic hand shape detection with OpenCV

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Webcam failed.")
    exit()

print("Simple Finger Counter - Raise fingers! Press 'q' to quit.")
print("Note: This uses simple color detection. For accurate detection:")
print("  Download: https://storage.googleapis.com/mediapipe-tasks/python/hand_landmarker.task")
print("  And place in this directory for full finger tracking.")
print()

frame_count = 0
while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    # Flip for mirror effect
    frame = cv2.flip(frame, 1)
    
    # Get frame dimensions
    height, width, _ = frame.shape
    
    # Define ROI (Region of Interest) - right side of screen
    roi_x, roi_y, roi_w, roi_h = 100, 50, 300, 300
    roi = frame[roi_y:roi_y+roi_h, roi_x:roi_x+roi_w]
    
    # Convert to HSV for better skin color detection
    hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
    
    # Skin color range in HSV
    lower_skin = np.array([0, 20, 70], dtype=np.uint8)
    upper_skin = np.array([20, 255, 255], dtype=np.uint8)
    
    # Create mask for skin
    mask = cv2.inRange(hsv, lower_skin, upper_skin)
    
    # Apply morphological operations
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    
    # Find contours
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    finger_count = 0
    if contours:
        # Get largest contour (likely the hand)
        cnt = max(contours, key=cv2.contourArea)
        
        if cv2.contourArea(cnt) > 1000:  # Minimum hand size threshold
            # Approximate contour
            epsilon = 0.02 * cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, epsilon, True)
            
            # Count convexity defects (spaces between fingers)
            hull = cv2.convexHull(cnt, returnPoints=False)
            
            if len(hull) > 3:
                defects = cv2.convexityDefects(cnt, hull)
                
                if defects is not None:
                    # Count deep defects (finger valleys)
                    finger_count = 1  # Start with 1 for the hand
                    
                    for i in range(defects.shape[0]):
                        s, e, f, d = defects[i, 0]
                        if d > 5000:  # Depth threshold for finger detection
                            finger_count += 1
                    
                    # Limit to reasonable count (0-5 fingers)
                    finger_count = min(finger_count, 5)
            
            # Draw contour
            cv2.drawContours(roi, [cnt], 0, (0, 255, 0), 2)
    
    # Draw ROI rectangle and display
    frame_display = frame.copy()
    cv2.rectangle(frame_display, (roi_x, roi_y), (roi_x+roi_w, roi_y+roi_h), (255, 0, 0), 2)
    
    # Display finger count
    cv2.rectangle(frame_display, (10, 10), (300, 80), (0, 0, 0), -1)
    cv2.putText(frame_display, f'Fingers Detected: {finger_count}', (20, 50), 
               cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 255, 0), 2)
    cv2.putText(frame_display, 'Place hand in blue box', (20, 70), 
               cv2.FONT_HERSHEY_SIMPLEX, 0.6, (100, 100, 255), 1)
    
    cv2.imshow('Finger Counter (q quit)', frame_display)
    cv2.imshow('Mask (Skin Detection)', mask)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
    frame_count += 1

cap.release()
cv2.destroyAllWindows()
print("Done!")
