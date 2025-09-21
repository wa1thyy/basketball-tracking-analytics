import numpy as np

class Track:
    def __init__(self, bbox, track_id):
        self.bbox = bbox  # (x1, y1, x2, y2)
        self.id = track_id
        self.hits = 1
        self.no_losses = 0

class Sort:
    def __init__(self, max_age=10, iou_threshold=0.3):
        self.max_age = max_age
        self.iou_threshold = iou_threshold
        self.tracks = []
        self.track_id_count = 0

    def iou(self, bb_test, bb_gt):
        xx1 = np.maximum(bb_test[0], bb_gt[0])
        yy1 = np.maximum(bb_test[1], bb_gt[1])
        xx2 = np.minimum(bb_test[2], bb_gt[2])
        yy2 = np.minimum(bb_test[3], bb_gt[3])
        w = np.maximum(0., xx2 - xx1)
        h = np.maximum(0., yy2 - yy1)
        wh = w * h
        o = wh / ((bb_test[2]-bb_test[0])*(bb_test[3]-bb_test[1]) +
                  (bb_gt[2]-bb_gt[0])*(bb_gt[3]-bb_gt[1]) - wh)
        return o

    def update(self, detections):
        updated_tracks = []
        for det in detections:
            x1, y1, x2, y2, score = det
            matched = False
            for trk in self.tracks:
                iou_score = self.iou(trk.bbox, (x1,y1,x2,y2))
                if iou_score > self.iou_threshold:
                    trk.bbox = (x1,y1,x2,y2)
                    trk.hits += 1
                    trk.no_losses = 0
                    updated_tracks.append(trk)
                    matched = True
                    break
            if not matched:
                self.track_id_count += 1
                new_trk = Track((x1,y1,x2,y2), self.track_id_count)
                updated_tracks.append(new_trk)

        for trk in self.tracks:
            if trk not in updated_tracks:
                trk.no_losses += 1
                if trk.no_losses < self.max_age:
                    updated_tracks.append(trk)

        self.tracks = updated_tracks
        results = []
        for trk in self.tracks:
            x1, y1, x2, y2 = trk.bbox
            results.append((x1,y1,x2,y2,trk.id))
        return results

# глобальный трекер
_tracker = Sort()

def init_tracker():
    global _tracker
    _tracker = Sort()
    return _tracker

def update_tracks(tracker, detections):
    return tracker.update(detections)

if __name__ == "__main__":
    dets = [(100,100,200,200,0.9), (300,300,400,400,0.95)]
    tracker = init_tracker()
    results = update_tracks(tracker, dets)
    print("Tracks:", results)
