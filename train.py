from ultralytics import YOLO
import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

if __name__ == '__main__':
    model = YOLO("yolov8n.pt")

    model.train(data="E:/BaiduSyncdisk/yolo-utils/data.yaml", 
                epochs=80,
                imgsz=1024)

