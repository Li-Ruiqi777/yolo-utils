from ultralytics import YOLO

# Load a model
model = YOLO("C:/Users/18005/Desktop/123/runs/detect/train8/weights/best.pt")  # load a custom trained model

# Export the model
model.export(format="onnx")