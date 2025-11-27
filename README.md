# Sensitive Content Detection Using Machine Learning (Real-Time AI Agent)

This project is a real-time AI agent that analyzes video streams and flags potentially sensitive / unsafe content.  
It is designed for use cases like classroom monitoring, parental control, and enterprise training safety.

> **Note:** Large datasets and model weights are not stored in this repo to keep it lightweight.  
> Add your own dataset + `.pth` files locally following the paths used in the code.

---

## 🚀 Features

- **Real-time video processing**  
  Streams frames from video inputs and runs ML inference to detect sensitive events.

- **ML-based sensitive content classifier**  
  Uses trained PyTorch models (`*.pth`) to classify frames as safe / unsafe.

- **Web interface**  
  Simple web UI (HTML + CSS templates) to start/stop processing and view status.

- **Modular pipeline**  
  Separate scripts for:
  - loading data  
  - populating the database  
  - processing videos  
  - adding new videos to the system  

---

## 🧠 Tech Stack

- **Language:** Python  
- **ML:** PyTorch (`.pth` model files, loaded in `model.py` / related scripts)  
- **Web:** Likely Flask / FastAPI style app (`app.py` + `templates/` + `static/`)  
- **Data & Processing:**
  - `load_data.py` – data loading utilities  
  - `process_videos.py` – frame extraction & inference pipeline  
  - `dgim_processor.py` – streaming / DGIM-style processing logic  
  - `populate_database.py`, `database.py` – persistence layer

*(If you want, update this list to match your exact libraries and framework.)*

---

## 📁 Project Structure

```text
Active_Version/
├── app.py                   # Main web / entry script
├── model.py                 # Model loading & inference helpers
├── process_videos.py        # Video frame processing and prediction
├── load_data.py             # Dataset loading/preprocessing
├── add_videos_to_db.py      # Utility to add new videos
├── populate_database.py     # Initialize DB with video metadata
├── database.py              # DB models / connection logic
├── dgim_processor.py        # Stream processing / DGIM algorithm
├── test.py                  # Test / debug script
├── train.py                 # Training script for the classifier (uses local dataset)
├── templates/
│   └── index.html           # Web UI
├── styles.css               # Styling for the web UI
└── .gitignore               # Ignores datasets, large models, videos, caches, etc.
