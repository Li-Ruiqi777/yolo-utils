from ultralytics import YOLO
import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

if __name__ == '__main__':

    model = YOLO('/home/jiahan/Desktop/yolo-utils/runs/detect/train5/weights/best.pt')

    model.val(cfg='./cfgs/rope_cfg.yaml',
                data='./datasets/rope_dataset.yaml', 
                imgsz=1024)
