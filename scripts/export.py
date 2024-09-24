from ultralytics import YOLO

if __name__ == '__main__':
    # Load a model
    model = YOLO("E:/BaiduSyncdisk/yolo-utils/best.pt")  # load a custom trained model

    # Export the model
    model.export(format="onnx")