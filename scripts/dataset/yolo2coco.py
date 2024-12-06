import os
import json
import shutil
from PIL import Image

def convert_yolo_to_coco(yolo_image_dir, yolo_label_dir, class_names, output_coco_path, merged_image_dir):
    """
    将 YOLO 格式数据转换为 COCO 格式，同时将所有图片复制到一个目录
    :param yolo_image_dir: YOLO 格式的图像目录
    :param yolo_label_dir: YOLO 格式的标签目录
    :param class_names: 类别名称列表
    :param output_coco_path: 输出的 COCO JSON 文件路径
    :param merged_image_dir: 合并后的图像目录
    """
    # 确保合并的图像目录存在
    os.makedirs(merged_image_dir, exist_ok=True)

    coco_data = {
        "images": [],
        "annotations": [],
        "categories": []
    }

    # 添加类别信息
    for i, class_name in enumerate(class_names):
        coco_data["categories"].append({"id": i, "name": class_name, "supercategory": "none"})

    annotation_id = 1
    for image_id, image_name in enumerate(os.listdir(yolo_image_dir)):
        if not image_name.endswith(('.jpg', '.png')):
            continue

        # 获取图片尺寸
        image_path = os.path.join(yolo_image_dir, image_name)
        with Image.open(image_path) as img:
            width, height = img.size

        # 复制图片到合并目录
        merged_image_path = os.path.join(merged_image_dir, image_name)
        if not os.path.exists(merged_image_path):
            shutil.copy(image_path, merged_image_path)

        # 添加图片信息到 COCO
        coco_data["images"].append({
            "id": image_id,
            "file_name": image_name,
            "width": width,
            "height": height
        })

        # 获取对应的 YOLO 标签文件
        label_file = os.path.join(yolo_label_dir, os.path.splitext(image_name)[0] + ".txt")
        if not os.path.exists(label_file):
            continue

        # 解析 YOLO 标签
        with open(label_file, 'r') as f:
            for line in f:
                class_id, x_center, y_center, box_width, box_height = map(float, line.split())

                # 转换为 COCO 格式的 bbox (x_min, y_min, width, height)
                x_min = (x_center - box_width / 2) * width
                y_min = (y_center - box_height / 2) * height
                box_width *= width
                box_height *= height

                # 添加标注信息到 COCO
                coco_data["annotations"].append({
                    "id": annotation_id,
                    "image_id": image_id,
                    "category_id": int(class_id),
                    "bbox": [x_min, y_min, box_width, box_height],
                    "area": box_width * box_height,
                    "iscrowd": 0
                })
                annotation_id += 1

    # 保存为 COCO JSON
    with open(output_coco_path, 'w') as json_file:
        json.dump(coco_data, json_file, indent=4)

    print(f"YOLO 格式转换为 COCO 格式完成，文件保存为 {output_coco_path}")
    print(f"所有图片已复制到 {merged_image_dir}")

if __name__ == '__main__':
    # 输入 YOLO 数据集路径
    yolo_images_root = 'E:/DeepLearning/0_DataSets/006-rope/003-rope1+2/YOLO_Format/images'
    yolo_labels_root = 'E:/DeepLearning/0_DataSets/006-rope/003-rope1+2/YOLO_Format/labels'

    # 定义类别名称列表
    class_names = ['broken', 'warp', 'scatter', 'rust', 'wear']  # 根据你的类别修改

    # 输出 COCO 格式路径
    coco_output_root = 'E:/DeepLearning/0_DataSets/006-rope/003-rope1+2/COCO_Format/annotations'
    os.makedirs(coco_output_root, exist_ok=True)

    # 合并图像目录
    merged_image_dir = 'E:/DeepLearning/0_DataSets/006-rope/003-rope1+2/COCO_Format/images'
    os.makedirs(merged_image_dir, exist_ok=True)

    # 数据集分为 train, val, test
    datasets = ['train', 'val', 'test']
    for dataset_type in datasets:
        yolo_image_dir = os.path.join(yolo_images_root, dataset_type)
        yolo_label_dir = os.path.join(yolo_labels_root, dataset_type)
        coco_output_path = os.path.join(coco_output_root, f"{dataset_type}.json")

        convert_yolo_to_coco(yolo_image_dir, yolo_label_dir, class_names, coco_output_path, merged_image_dir)
