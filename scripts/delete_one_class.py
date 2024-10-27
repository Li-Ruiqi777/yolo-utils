'''
此文件用于删掉YOLO数据集中某个类别(阿拉伯数字)的所有标签
'''
import os

# 定义一个函数，用于处理单个文件
def process_txt_file(file_path, categories_to_filter):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # 过滤掉以指定类别开头的行
    filtered_lines = [
        line for line in lines 
        if not any(line.strip().startswith(category) for category in categories_to_filter)
    ]

    with open(file_path, 'w') as file:
        file.writelines(filtered_lines)

# 定义一个函数，用于处理整个文件夹
def process_folder(folder_path, categories_to_filter):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".txt"):
                file_path = os.path.join(root, file)
                process_txt_file(file_path, categories_to_filter)
                print(f"Processed: {file_path}")

if __name__=='__main__':
    # 指定要处理的文件夹目录
    folder_to_process = "/home/jiahan/Desktop/yolo-utils/YOLO_Format/labels" 

    # 手动设置需要过滤的类别
    categories_to_filter = ["2"] 

    # 调用函数来处理文件夹中的txt文件
    process_folder(folder_to_process, categories_to_filter)
