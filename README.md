# Basketball Tracking & Analytics

This project demonstrates how **computer vision** can be applied to sports analytics.  
The system automatically **detects basketball players**, assigns **unique tracking IDs**, and generates **heatmaps** to visualize movement patterns on the court.

## Features
- Player detection using YOLOv8  
- Multi-object tracking with consistent IDs  
- Processed game footage with bounding boxes and IDs  
- Heatmap generation for activity analysis  

## Project Structure
```plaintext
player-tracker/
│
├── src/                  # Core modules
│   ├── detect.py         # Player detection (YOLOv8)
│   ├── track.py          # Multi-object tracking
│   └── heatmap.py        # Heatmap generation
│
├── scripts/              # Example scripts
│   ├── test_track_video.py   # Run tracking on video
│   ├── test_detect_video.py  # Run detection only
│   └── make_heatmap.py       # Generate heatmap from tracked video
│
├── data/
│   ├── raw/              # Input videos
│   └── processed/        # Processed results
│
├── requirements.txt      # Dependencies
└── README.md             # Project description
```

## Installation
```bash
# Clone the repository
git clone https://github.com/wa1thyy/basketball-tracking-analytics.git
cd basketball-tracking-analytics

# Create and activate virtual environment
python -m venv .venv
.venv\Scripts\activate   # On Windows

# Install dependencies
pip install -r requirements.txt
```
# Usage
```
Run player tracking
bash
Копировать код
python -m scripts.test_track_video
Generate heatmap
bash
Копировать код
python -m scripts.make_heatmap --input data/processed/tracked.mp4
```

# Project Goal
This project was developed to demonstrate skills in:

Computer Vision (YOLOv8, OpenCV)

Data Analysis & Visualization

Applied AI for Sports Analytics

# Heatmap and screenshots

<img width="950" height="543" alt="heatmap" src="https://github.com/user-attachments/assets/6e13ba0b-476d-4914-b5a1-97b0e039c7c5" width="600" />

<img width="1366" height="768" alt="image" src="https://github.com/user-attachments/assets/5f44df0a-4a85-4954-977d-bb262b95a809" width="600"/>

##  Demo

![demo](https://github.com/user-attachments/assets/bc54536e-09f9-4ee4-a7cc-dbc2226dd4d0)












