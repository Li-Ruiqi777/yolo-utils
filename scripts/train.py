from ultralytics import YOLO

if __name__ == '__main__':
    # Load a model
    model = YOLO('yolov8n.yaml').load('yolov8n.pt')  # build from YAML and transfer weights

    # Train the model
    model.train(data='./data.yaml', epochs=10, imgsz=1024)


# from ultralytics import YOLO
# import os
# os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

# if __name__ == '__main__':
#     model = YOLO("yolov8n.pt")

#     model.train(data="./data.yaml", epochs=70, imgsz=1024)