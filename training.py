from ultralytics import YOLO
model = YOLO("yolov8m.pt")
model.train(task="detect", mode='train', epochs=30, data='data_custom.yaml', model='yolov8m.pt', imgsz=640, batch=8)