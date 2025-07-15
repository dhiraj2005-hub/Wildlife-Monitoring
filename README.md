# 🐾 Wildlife Monitoring & Conservation Project

This Python project uses AI (YOLOv8) to detect animals in camera trap images and logs their appearances. It also includes a Streamlit dashboard for visualization.

## 🔧 Setup

1. Install dependencies:
```
pip install ultralytics pandas streamlit
```

2. Add your animal image as `sample.jpg` in the project folder.

3. Run detection:
```
python detect.py
```

4. Launch dashboard:
```
streamlit run app.py
```

## 📁 Files
- `detect.py` – Runs detection using YOLOv8
- `app.py` – Shows dashboard with logs
- `wildlife_log.csv` – Stores animal detection records
