# Finger Counter

A real-time finger detection and counting application using OpenCV. Detects hands in your camera feed and counts the number of raised fingers.

## Features

- **Real-time Detection**: Live finger counting from webcam feed
- **Hand Detection**: Uses HSV color space for skin segmentation
- **Finger Counting**: Analyzes hand contours to count raised fingers
- **Visual Feedback**: Displays finger count as overlay on video
- **No ML Models Required**: Uses pure OpenCV image processing
- **Adjustable**: Works with different lighting conditions and hand positions

## Requirements

- Python 3.7+
- OpenCV (cv2)
- NumPy

## Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

Or install manually:
```bash
pip install opencv-python numpy
```

2. Run the script:
```bash
python finger_counter.py
```

## Usage

Simply run the script and position your hand in the blue box on the screen:

```bash
python finger_counter.py
```

### Controls

- `q` - Quit the application

## How It Works

The finger counter uses the following approach:

1. **Skin Detection**: 
   - Converts frame to HSV color space
   - Applies color range thresholding to isolate skin

2. **Hand Segmentation**:
   - Uses morphological operations to clean up the mask
   - Finds contours of detected hand regions

3. **Finger Counting**:
   - Calculates convex hull of hand contour
   - Analyzes convexity defects (valleys between fingers)
   - Counts defects deeper than a threshold
   - Limits count to 0-5 fingers

4. **Display**:
   - Draws hand contour in green
   - Displays finger count in overlay box
   - Shows a blue box indicating detection area

## Example Output

```
Fingers Detected: 5
Place hand in blue box
```

The script will display:
- Live video feed from your camera
- Blue rectangle showing the detection region
- Green hand contour outline
- Black box with white text showing detected finger count
- Instructions for operation

## Tips for Best Results

- **Lighting**: Use good, even lighting without harsh shadows
- **Background**: Use a contrasting background (plain wall or solid color)
- **Hand Position**: Keep your hand within the blue detection box
- **Skin Tone**: Works best with clearly visible skin color
- **Camera Distance**: Position camera 30-60cm away from your hand
- **Hand Orientation**: Keep palm facing camera for best detection

## Limitations

- Works best with single hands
- Requires visible skin color in HSV range
- May have issues with:
  - Low light conditions
  - Very dark or very light skin tones
  - Complex backgrounds
  - Hand partially out of frame

## Troubleshooting

### Camera not opening
```bash
# On Linux, grant camera permissions:
sudo usermod -aG video $USER
# Log out and back in
```

### No hand detected
- Improve lighting
- Move hand to center of blue box
- Use simpler background
- Adjust hand angle

### Inaccurate finger count
- Ensure good lighting
- Keep hand steady
- Stay within the detection region
- Try moving the hand closer or farther from camera

### Slow performance
- Check if other applications are using the camera
- Close unnecessary applications
- Try reducing camera resolution

## Files

- `finger_counter.py` - Main script
- `requirements.txt` - Python dependencies

## Performance

- **Real-time Processing**: ~30 FPS on modern hardware
- **CPU Usage**: Moderate (no GPU acceleration needed)
- **Memory**: ~100-200 MB

## Future Improvements

- Multi-hand detection support
- Palm detection and orientation
- Gesture recognition
- Finger tracking across frames
- MediaPipe integration for better accuracy

## License

MIT - Open source for educational use

---

**Version**: 1.0  
**Last Updated**: February 19, 2026

https://github.com/user-attachments/assets/8a476e6a-023e-41d4-a464-c8f9d516d72f

