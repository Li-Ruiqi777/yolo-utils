from sahi.utils.file import download_from_url
from sahi.utils.yolov8 import download_yolov8s_model
from sahi import AutoDetectionModel
from sahi.predict import get_prediction, get_sliced_prediction
from PIL import Image

if __name__ == "__main__":

    detection_model = AutoDetectionModel.from_pretrained(
        model_type="yolov8",
        model_path="/home/jiahan/Desktop/yolo-utils/runs/detect/yolo11n/weights/best.pt",
        confidence_threshold=0.3,
        device="cuda:0",  # or 'cuda:0'
    )

    # 执行标准预测
    result_standard = get_prediction("./123.png", 
                            detection_model)

    # 导出可视化结果
    result_standard.export_visuals(export_dir="./")

    # 执行切片辅助预测
    # result_sliced = get_sliced_prediction(
    #     "./123.png",
    #     detection_model,
    #     slice_height=256,
    #     slice_width=256,
    #     overlap_height_ratio=0.2,
    #     overlap_width_ratio=0.2,
    # )

    # result_sliced.export_visuals(export_dir="./")

    # # Access the object prediction list
    # object_prediction_list = result_sliced.object_prediction_list

    # # Convert to COCO annotation, COCO prediction, imantics, and fiftyone formats
    # result_sliced.to_coco_annotations()[:3]
    # result_sliced.to_coco_predictions(image_id=1)[:3]
    # result_sliced.to_imantics_annotations()[:3]
    # result_sliced.to_fiftyone_detections()[:3]