import os
import shutil

def remove_common_files(folder_a, folder_b):
    """
    从文件夹A中移除与文件夹B中同名的文件。

    :param folder_a: 文件夹A的路径
    :param folder_b: 文件夹B的路径
    """
    # 获取文件夹A和B中的文件名集合
    files_in_a = set(os.listdir(folder_a))
    files_in_b = set(os.listdir(folder_b))

    # 找到两者的交集，即同名文件
    common_files = files_in_a.intersection(files_in_b)

    # 从文件夹A中移除同名文件
    for file_name in common_files:
        file_path = os.path.join(folder_a, file_name)
        if os.path.isfile(file_path):
            print(f"Removing: {file_path}")
            os.remove(file_path)
        elif os.path.isdir(file_path):
            print(f"Skipping directory: {file_path}")

if __name__ == "__main__":
    folder_a = "E:/DeepLearning/0_DataSets/006-rope/007-unsupervised/good"
    folder_b = "E:/DeepLearning/0_DataSets/006-rope/007-unsupervised/bad"

    if not os.path.exists(folder_a):
        print(f"Error: Folder A does not exist: {folder_a}")
    elif not os.path.exists(folder_b):
        print(f"Error: Folder B does not exist: {folder_b}")
    else:
        remove_common_files(folder_a, folder_b)
        print("Process completed.")
