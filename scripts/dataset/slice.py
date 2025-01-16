'''
将COCO数据集的图片和label同时进行切片
'''
from sahi.utils.coco import Coco, export_coco_as_yolov5
from sahi.slicing import slice_coco

if __name__ == "__main__":
    # # init Coco object
    # train_coco = Coco.from_coco_dict_or_path(
    #     "E:/DeepLearning/0_DataSets/006-rope/001-rope1/COCO_Format/annotations/train.json",
    #     "E:/DeepLearning/0_DataSets/006-rope/001-rope1/COCO_Format/images")
    # val_coco = Coco.from_coco_dict_or_path(
    #     "E:/DeepLearning/0_DataSets/006-rope/001-rope1/COCO_Format/annotations/val.json", 
    #     "E:/DeepLearning/0_DataSets/006-rope/001-rope1/COCO_Format/images")

    # # export converted YoloV5 formatted dataset into given output_dir with given train/val split
    # data_yml_path = export_coco_as_yolov5(
    # output_dir="./123",
    # train_coco=train_coco,
    # val_coco=val_coco
    # )

    slice_coco(
        coco_annotation_file_path="E:/DeepLearning/0_DataSets/006-rope/003-rope1+2/COCO_Format/annotations/val.json",  # 原始标注文件路径
        image_dir="E:/DeepLearning/0_DataSets/006-rope/003-rope1+2/COCO_Format/images",                                           # 原始图片目录
        output_coco_annotation_file_name="val",      # 切片后的标注文件名
        output_dir="E:/DeepLearning/0_DataSets/006-rope/005-rope1+2-sliced",                                         # 切片后的输出目录
        slice_height=256,  # 切片高度
        slice_width=256,   # 切片宽度
        overlap_height_ratio=0,  # 高度方向重叠比例
        overlap_width_ratio=0,   # 宽度方向重叠比例
        min_area_ratio=0.1,        # 切片中物体最小占比
        ignore_negative_samples=True,  # 是否忽略负样本
        out_ext=".jpg"  # 切片后图片格式
    )
