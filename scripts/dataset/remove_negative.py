"""
    根据标注结果,删掉切片后没有bbox的图片(用于COCO数据集)
"""
import os
import json

def delete_unlabeled_images(json_file, images_folder):
    # 读取COCO数据集的json文件
    with open(json_file, 'r', encoding='utf-8') as f:
        coco_data = json.load(f)
    
    # 获取所有已标注的图片的文件名
    labeled_images = set()
    for annotation in coco_data['annotations']:
        image_id = annotation['image_id']
        for image in coco_data['images']:
            if image['id'] == image_id:
                labeled_images.add(image['file_name'])
                break
    
    # 获取指定目录下的所有图片文件名
    all_image_files = set(os.listdir(images_folder))
    
    # 过滤掉非图片文件（例如非JPG, PNG等格式的文件）
    image_extensions = {'.jpg', '.jpeg', '.png', '.bmp', '.gif'}
    all_image_files = {file for file in all_image_files if any(file.lower().endswith(ext) for ext in image_extensions)}
    
    # 找出所有未标注的图片文件
    unlabeled_image_files = all_image_files - labeled_images
    
    # 删除未标注的图片
    for image_file in unlabeled_image_files:
        image_path = os.path.join(images_folder, image_file)
        if os.path.exists(image_path):
            os.remove(image_path)
            print(f"Deleted {image_path}")
        else:
            print(f"File {image_path} not found")

images_dir = 'E:/DeepLearning/0_DataSets/006-rope/005-rope1+2-sliced/'   # COCO 数据集中的 images 目录路径
json_file = 'E:/DeepLearning/0_DataSets/006-rope/005-rope1+2-sliced/val_coco.json'  # COCO 数据集中的标注文件路径

if __name__ == '__main__':
    delete_unlabeled_images(json_file, images_dir)
