from ultralytics import YOLO
import cv2
model=YOLO("yolov8n.pt")
results=model("https://ultralytics.com/images/bus.jpg")
for r in results:
    r.show()