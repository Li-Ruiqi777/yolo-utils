from ultralytics import YOLO
import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

if __name__ == '__main__':
    # Load a model
    model = YOLO('yolo11n-seg.yaml')
    # model.load('/home/jiahan/Desktop/yolo-utils/runs/detect/train4/weights/last.pt')

    # Train the model
    model.train(cfg='./cfgs/ship-segment_cfg.yaml',
                data='./datasets/ship-segment_dataset.yaml', 
                epochs=350,
                patience=50,
                imgsz=1024)
