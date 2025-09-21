import cv2
from src.detect import detect_people


def test_blank():
frame = cv2.imread("data/raw/sample.jpg") if cv2.haveImageReader("data/raw/sample.jpg") else None
if frame is None:
import numpy as np
frame = np.zeros((480,640,3), dtype=np.uint8)
detections = detect_people(frame)
assert isinstance(detections, list)
