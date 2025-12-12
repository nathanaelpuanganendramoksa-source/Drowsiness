# Drowsiness Detection Project - AI Agent Instructions

## Project Overview
This is a computer vision project for real-time drowsiness detection using YOLOv8. It classifies users as "DROWSY" or "NORMAL" based on yawn and eye closure scores from facial detection.

## Architecture
- **Core Logic**: `main.py` contains `classify_state()` function that thresholds yawn_score (>0.7) and eye_score (>0.8) to determine drowsiness.
- **API**: `api.py` provides FastAPI endpoint `/detect` accepting `yawn_score` and `eye_score` query parameters.
- **Model**: YOLOv8n model trained on custom dataset with "Awake" and "Drowsy" classes (see `YOLO/DrowsyV2/data.yaml`).
- **Inference**: Notebook `Drowsiness.ipynb` demonstrates training, image inference, and real-time webcam detection using OpenCV.

## Key Workflows
- **Training**: Run `model.train(data='YOLO/DrowsyV2/data.yaml', epochs=100)` in notebook; models saved to `runs/detect/train*/weights/best.pt`.
- **Inference**: Load trained model with `YOLO('runs/detect/train27/weights/best.pt')`; call `model(frame)` for detection results.
- **API Server**: Run `uvicorn api:app --reload` to start FastAPI server on localhost:8000.
- **Real-time Detection**: Use OpenCV VideoCapture for webcam feed; annotate frames with `result[0].plot()`.

## Conventions
- **Imports**: Use `from ultralytics import YOLO` for model loading; `import cv2` for image processing.
- **Model Paths**: Reference trained models from `runs/detect/` subfolders (e.g., train27 for latest).
- **Dataset Structure**: Follow YOLO format with images/labels in train/valid/test folders.
- **Thresholds**: Drowsiness triggers at yawn > 0.7 OR eye > 0.8 (see `main.py`).

## Testing
- **Unit Tests**: `tests/test_unit.py` covers basic classification scenarios.
- **Blackbox Tests**: `tests/test_blackbox.py` uses equivalence partitioning and boundary value analysis for thresholds.
- **Coverage Tests**: `tests/test_basis_path.py` and `tests/test_condition.py` ensure comprehensive path/condition coverage.
- Run with `pytest` from project root.

## Performance Testing
- Use K6 scripts in `YOLO/k6/` for load testing the API:
  - `load.js`: 20 virtual users for 30s.
  - `smoke.js`, `spike.js`, `stress.js`: Various load patterns.
- Execute with `k6 run YOLO/k6/load.js` against running API server.

## Dependencies
- Ultralytics for YOLO operations.
- OpenCV for image/video processing.
- FastAPI for web API.
- pytest for testing.
- k6 for performance testing.