from ultralytics import YOLO

if __name__ == '__main__':
    # Load a model
    model = YOLO("./best.pt")  # load a custom trained model

    # Export the model
    model.export(format="onnx",opset=11, simplify=True)