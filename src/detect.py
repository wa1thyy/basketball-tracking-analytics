from ultralytics import YOLO
from typing import List, Tuple
import numpy as np
import cv2

# Загружаем предобученную модель YOLOv8 (маленькая версия)
_model = YOLO("yolov8n.pt")

def detect_people(frame_bgr: np.ndarray, conf: float = 0.4) -> List[Tuple[int, int, int, int, float]]:
    """
    Детектирует людей на кадре.

    Args:
        frame_bgr: np.ndarray — кадр в формате BGR (как из cv2.VideoCapture)
        conf: float — порог уверенности

    Returns:
        List[Tuple[x1, y1, x2, y2, score]]
    """
    results = _model.predict(frame_bgr, conf=conf, verbose=False)[0]
    detections = []

    for box in results.boxes:
        cls_id = int(box.cls)
        if cls_id != 0:  # YOLO class 0 = person
            continue
        x1, y1, x2, y2 = box.xyxy[0].tolist()
        score = float(box.conf[0])
        detections.append((int(x1), int(y1), int(x2), int(y2), score))

    return detections

if __name__ == "__main__":
    # Тест: прогоняем одно изображение (чёрный кадр)
    frame = np.zeros((480, 640, 3), dtype=np.uint8)
    dets = detect_people(frame)
    print("detections:", dets)
