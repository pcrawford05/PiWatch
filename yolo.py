from ultralytics import YOLO
import cv2

def runInference(img_path):
    # Load model (choose yolov8n.pt for smallest model)
    model = YOLO("yolov8n.pt")

    # Load Image and Run inference
    results = model(cv2.imread(img_path))

    # Return result
    return results