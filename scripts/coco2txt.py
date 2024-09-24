import os
import json
import shutil

def convert_coco_to_yolo(coco_json_path, images_dir, output_image_dir, output_label_dir):
    # 加载 COCO 数据集的 JSON 文件
    with open(coco_json_path, 'r') as f:
        coco_data = json.load(f)

    # 创建输出目录
    if not os.path.exists(output_label_dir):
        os.makedirs(output_label_dir)
    if not os.path.exists(output_image_dir):
        os.makedirs(output_image_dir)

    # 获取图像和标注信息
    images = {img['id']: img for img in coco_data['images']}
    annotations = coco_data['annotations']
    categories = {cat['id']: cat['name'] for cat in coco_data['categories']}

    # 创建类别名称到类别编号的映射
    category_to_id = {name: idx for idx, (id, name) in enumerate(categories.items())}

    # 处理每一个标注
    for ann in annotations:
        image_id = ann['image_id']
        image_info = images[image_id]

        image_name = image_info['file_name']
        image_width = image_info['width']
        image_height = image_info['height']

        bbox = ann['bbox']  # [x_min, y_min, width, height] in COCO format
        category_id = ann['category_id']

        # 计算 YOLO 格式的归一化边界框 (x_center, y_center, width, height)
        x_min, y_min, box_width, box_height = bbox
        x_center = (x_min + box_width / 2) / image_width
        y_center = (y_min + box_height / 2) / image_height
        box_width /= image_width
        box_height /= image_height

        # YOLO 格式：class_id, x_center, y_center, box_width, box_height
        class_id = category_to_id[categories[category_id]]
        yolo_format = f"{class_id} {x_center:.6f} {y_center:.6f} {box_width:.6f} {box_height:.6f}\n"

        # 输出对应的 YOLO 标签文件
        yolo_label_path = os.path.join(output_label_dir, f"{os.path.splitext(image_name)[0]}.txt")
        with open(yolo_label_path, 'a') as label_file:
            label_file.write(yolo_format)

        # 复制图像文件到 YOLO 的 images 目录
        original_image_path = os.path.join(images_dir, image_name)
        output_image_path = os.path.join(output_image_dir, image_name)
        if not os.path.exists(output_image_path):
            shutil.copy(original_image_path, output_image_path)

    print(f"转换完成, YOLO标签已保存到 {output_label_dir}，图像已保存到 {output_image_dir}")

if __name__ == '__main__':
    # 修改为你的数据集路径
    coco_root = './COCO_Format/annotations'
    images_root = './COCO_Format/images'
    yolo_images_root = './YOLO_Format/yolo/images'
    yolo_labels_root = './YOLO_Format/yolo/labels'

    # 数据集分为 train, val, test
    datasets = {
        'train': 'train.json',
        'val': 'val.json',
        'test': 'test.json'
    }

    for dataset_type, coco_file in datasets.items():
        coco_annotation_path = os.path.join(coco_root, coco_file)
        images_path = images_root

        output_image_dir = os.path.join(yolo_images_root, dataset_type)
        output_label_dir = os.path.join(yolo_labels_root, dataset_type)

        convert_coco_to_yolo(coco_annotation_path, images_path, output_image_dir, output_label_dir)

