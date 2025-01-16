"""
用于对数据集中的label进行可视化,检查标注是否正确
"""

import cv2
import os
import random

def visualize_yolo_labels(image_folder, label_folder, output_folder=None, class_names=None):
    """
    Visualize YOLO format labels on images.
    
    Parameters:
    - image_folder: str, path to the folder containing images
    - label_folder: str, path to the folder containing YOLO label files
    - output_folder: str, path to save the visualized images (optional)
    - class_names: list, names of classes (optional)
    """
    colors = {}
    num_classes = len(class_names)
    for i in range(num_classes):
        colors[i] = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    if output_folder and not os.path.exists(output_folder):
        os.makedirs(output_folder)
        
    for label_file in os.listdir(label_folder):
        if label_file.endswith(".txt"):
            image_file = label_file.replace(".txt", ".jpg")  # Assumes images are .jpg; adjust if necessary
            image_path = os.path.join(image_folder, image_file)
            label_path = os.path.join(label_folder, label_file)
            
            # Load image
            image = cv2.imread(image_path)
            if image is None:
                print(f"Image {image_file} not found.")
                continue
            
            height, width, _ = image.shape
            
            # Read labels
            with open(label_path, "r") as f:
                for line in f:
                    elements = line.strip().split()
                    class_id = int(elements[0])
                    x_center, y_center, w, h = map(float, elements[1:])
                    
                    # Convert YOLO format to bounding box coordinates
                    x1 = int((x_center - w / 2) * width)
                    y1 = int((y_center - h / 2) * height)
                    x2 = int((x_center + w / 2) * width)
                    y2 = int((y_center + h / 2) * height)
                    
                    color = colors.get(class_id, (0, 255, 0))
                    cv2.rectangle(image, (x1, y1), (x2, y2), color, 2)
                    
                    # Put class label
                    label = class_names[class_id] if class_names and class_id < len(class_names) else str(class_id)
                    cv2.putText(image, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
            
            # Display or save image
            if output_folder:
                output_path = os.path.join(output_folder, image_file)
                cv2.imwrite(output_path, image)

if __name__ == "__main__":

    image_folder = "E:/DeepLearning/0_DataSets/006-rope/003-rope1+2/YOLO_Format/images/test"
    label_folder = "E:/DeepLearning/0_DataSets/006-rope/003-rope1+2/YOLO_Format/labels/test"
    output_folder = "E:/DeepLearning/0_DataSets/006-rope/003-rope1+2/YOLO_Format/visualize" 
    class_names = ["broken", "warp", "scatter","rust","wear"]  # 可选: 类别名称

    visualize_yolo_labels(image_folder, label_folder, output_folder, class_names)
