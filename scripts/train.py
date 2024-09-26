from ultralytics import YOLO
import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

if __name__ == '__main__':
    # Load a model
    model = YOLO('yolov8n.yaml')
    model.load('yolov8n.pt') 

    # Train the model
    model.train(cfg='./cfgs/rope_cfg.yaml',
                data='./datasets/rope_dataset.yaml', 
                epochs=150, 
                imgsz=1024)
