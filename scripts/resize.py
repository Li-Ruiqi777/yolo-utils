import os
import cv2

def resize_images(source_folder, size):
    # 遍历源文件夹中的所有文件
    for filename in os.listdir(source_folder):
        if filename.endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):  # 只处理图片文件
            img_path = os.path.join(source_folder, filename)
            img = cv2.imread(img_path)

            # 检查图片是否成功读取
            if img is not None:
                # 调整图片大小
                resized_img = cv2.resize(img, size, interpolation=cv2.INTER_AREA)

                # 覆盖保存调整大小后的图片到原文件夹
                cv2.imwrite(img_path, resized_img)

    print("所有图片已调整大小并覆盖保存.")

if __name__ == '__main__':
    source_folder = "E:\DeepLearning\yolo-utils\VOC\JPEGImages"
    resize_size = (1024, 1024)

    resize_images(source_folder, resize_size)
