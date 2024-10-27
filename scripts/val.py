from ultralytics import YOLO
import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

if __name__ == '__main__':
    model = YOLO('E:/DeepLearning/yolo-utils/runs/detect/train2/weights/best.pt')

    model.val(cfg='./cfgs/rope_cfg.yaml',
                data='./datasets/rope_dataset.yaml', 
                imgsz=1024)
