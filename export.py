from ultralytics import YOLO

# Load a model
model = YOLO("E:/BaiduSyncdisk/yolo-utils/best.pt")  # load a custom trained model

# Export the model
model.export(format="onnx")