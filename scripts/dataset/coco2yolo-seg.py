import os
import json

coco_dir = "E:/DeepLearning/0_DataSets/002-ship-segment/001-mix/COCO_Format/labels/val"
txt_dir = "E:/DeepLearning/0_DataSets/002-ship-segment/001-mix/YOLO_Format/labels/val"

# 类别映射，假设项目中有不同的标签，并为每个标签分配一个class_id
label_map = {
    "boat": 0,
}

# 确保输出目录存在
os.makedirs(txt_dir, exist_ok=True)

# 遍历输入目录中的所有文件
for filename in os.listdir(coco_dir):
    if filename.endswith(".json"):
        json_path = os.path.join(coco_dir, filename)

        # 读取 LabelMe 标注的 JSON 文件
        with open(json_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        # 获取图片的宽度和高度
        image_path = os.path.join(coco_dir, data["imagePath"])
        img_width = data["imageWidth"]
        img_height = data["imageHeight"]

        # YOLO 格式输出文件
        output_path = os.path.join(txt_dir, filename.replace(".json", ".txt"))

        with open(output_path, "w") as out_file:
            # 遍历每个标注对象
            for shape in data["shapes"]:
                # 获取类别标签
                label = shape["label"]

                # 检查是否在label_map中
                if label in label_map:
                    class_id = label_map[label]
                else:
                    print(f"警告：未找到类别 '{label}' 的映射，请检查标签映射。")
                    continue  # 跳过未映射的标签

                # 提取多边形点
                points = shape["points"]

                # 将多边形点的坐标标准化（相对于图像宽高）
                normalized_points = []
                for x, y in points:
                    normalized_x = x / img_width
                    normalized_y = y / img_height
                    normalized_points.append(f"{normalized_x} {normalized_y}")

                # 将数据写入到YOLO格式文件中
                yolo_format = f"{class_id} " + " ".join(normalized_points) + "\n"
                out_file.write(yolo_format)

print("转换完成！")
