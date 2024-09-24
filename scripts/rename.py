import os

def rename_images_in_folder(folder_path):
    # 获取文件夹内的所有文件
    files = os.listdir(folder_path)

    # 过滤出需要排序的文件
    image_extensions = [".jpg", ".jpeg", ".png", ".bmp", ".gif", ".tiff", ".txt", ".xml"]
    images = [f for f in files if os.path.splitext(f)[1].lower() in image_extensions]

    # 对图片进行排序并从00001开始重命名
    for idx, image in enumerate(sorted(images), start=157):
        new_name = f"{idx:06d}{os.path.splitext(image)[1].lower()}"

        # 原文件路径和新文件路径
        old_file = os.path.join(folder_path, image)
        new_file = os.path.join(folder_path, new_name)

        # 重命名文件
        os.rename(old_file, new_file)
        print(f"Renamed: {old_file} -> {new_file}")

if __name__ == "__main__":
    folder_path = "E:/BaiduSyncdisk/yolo-utils/VOC/Annotations"
    rename_images_in_folder(folder_path)
