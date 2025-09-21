import numpy as np
import cv2
import matplotlib.pyplot as plt
import os

def build_heatmap(track_history, player_id=None, court_img=None, out_path="data/processed/heatmap.png"):
    """
    Строит тепловую карту по траекториям игроков.
    """
    h, w = 720, 1280
    heatmap = np.zeros((h, w), dtype=np.float32)

    ids = [player_id] if player_id else track_history.keys()
    for pid in ids:
        if pid not in track_history:
            continue
        for (x, y) in track_history[pid]:
            if 0 <= int(y) < h and 0 <= int(x) < w:
                heatmap[int(y), int(x)] += 1

    heatmap = cv2.GaussianBlur(heatmap, (0, 0), sigmaX=25, sigmaY=25)
    heatmap = heatmap / (heatmap.max() + 1e-6)

    plt.figure(figsize=(12, 7))
    if court_img and os.path.exists(court_img):
        img = cv2.cvtColor(cv2.imread(court_img), cv2.COLOR_BGR2RGB)
        plt.imshow(img, alpha=0.6)
    plt.imshow(heatmap, cmap='jet', alpha=0.5)
    plt.axis('off')
    plt.savefig(out_path, bbox_inches='tight')
    plt.close()
    print(f"✅ Heatmap saved to {out_path}")
