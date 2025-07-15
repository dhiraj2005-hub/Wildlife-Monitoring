from ultralytics import YOLO
import pandas as pd
from datetime import datetime
import os

# Load YOLOv8 model
model = YOLO("yolov8n.pt")  # Pre-trained model

# Image path (put your own animal image here)
image_path = r"sample_image.jpg"


# Perform detection
results = model(image_path)

# Extract detection data
detections = results[0].boxes
class_names = results[0].names

# Prepare CSV logging
log_file = "wildlife_log.csv"
rows = []

for det in detections:
    cls_id = int(det.cls[0])
    conf = round(float(det.conf[0]), 2)
    species = class_names[cls_id]

    row = {
        "Date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "Animal": species,
        "Confidence": conf,
        "Image": image_path
    }
    rows.append(row)

# Save to CSV
df = pd.DataFrame(rows)

if os.path.exists(log_file):
    df.to_csv(log_file, mode='a', index=False, header=False)
else:
    df.to_csv(log_file, index=False)

print("Detection complete. Results saved to wildlife_log.csv")
