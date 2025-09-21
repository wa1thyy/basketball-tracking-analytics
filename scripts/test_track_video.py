import cv2
import os
from src.detect import detect_people
from src.track import init_tracker, update_tracks

INPUT_PATH = "data/raw/sample_short.mp4"
OUTPUT_PATH = "data/processed/tracked.mp4"

os.makedirs("data/processed", exist_ok=True)

cap = cv2.VideoCapture(INPUT_PATH)
if not cap.isOpened():
    raise FileNotFoundError(f"Не удалось открыть видео {INPUT_PATH}")

fps = cap.get(cv2.CAP_PROP_FPS) or 25
w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
out = cv2.VideoWriter(OUTPUT_PATH, fourcc, fps, (w, h))

tracker = init_tracker()
frame_count = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    detections = detect_people(frame)
    
    tracks = update_tracks(tracker, detections)


    for (x1, y1, x2, y2, track_id) in tracks:
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(frame, f"ID {track_id}", (x1, y1 - 5),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    out.write(frame)
    frame_count += 1
    if frame_count % 30 == 0:
        print(f"Processed {frame_count} frames...")

cap.release()
out.release()
print(f"✅ Готово! Сохранил результат в {OUTPUT_PATH}")
