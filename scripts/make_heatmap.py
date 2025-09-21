import cv2
import os
import argparse
from src.detect import detect_people
from src.track import init_tracker, update_tracks
from src.heatmap import build_heatmap

parser = argparse.ArgumentParser()
parser.add_argument("--input", type=str, default="data/raw/sample_short.mp4")
parser.add_argument("--player_id", type=int, default=None)
parser.add_argument("--court", type=str, default=None)
args = parser.parse_args()

os.makedirs("data/processed", exist_ok=True)

cap = cv2.VideoCapture(args.input)
if not cap.isOpened():
    raise FileNotFoundError(f"Не удалось открыть видео {args.input}")

tracker = init_tracker()
track_history = {}

while True:
    ret, frame = cap.read()
    if not ret:
        break

    detections = detect_people(frame)
    tracks = update_tracks(tracker, detections)

    for (x1, y1, x2, y2, track_id) in tracks:
        cx = int((x1 + x2) / 2)
        cy = int((y1 + y2) / 2)
        if track_id not in track_history:
            track_history[track_id] = []
        track_history[track_id].append((cx, cy))

cap.release()

out_path = "data/processed/heatmap.png" if args.player_id is None else f"data/processed/heatmap_player_{args.player_id}.png"
build_heatmap(track_history, player_id=args.player_id, court_img=args.court, out_path=out_path)
