import os

# 指定根目录
root_dir = "./"  # 替换为你实际的根目录路径

# 定义要创建的目录结构
dirs = [
    "VOC/Annotations",
    "VOC/JPEGImages",
    "YOLO_Format/images/test",
    "YOLO_Format/images/train",
    "YOLO_Format/images/val",
    "YOLO_Format/labels/test",
    "YOLO_Format/labels/train",
    "YOLO_Format/labels/val"
]

# 在根目录下创建目录结构
for dir_path in dirs:
    full_path = os.path.join(root_dir, dir_path)
    os.makedirs(full_path, exist_ok=True)
    print(f"Created: {full_path}")

print("目录结构创建完成。")
