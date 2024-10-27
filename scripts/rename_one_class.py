'''
用于在删掉一个类的标签后,调整此类之后的类的idx
'''
import os
import re

# 定义一个函数，用于处理单个文件
def process_txt_file(file_path, original_number, replacement_number):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    modified_lines = []

    for line in lines:
        if re.match(rf'^{original_number}', line.strip()):
            # 找到以指定数字开头的行，替换第一个数字
            parts = line.strip().split(' ')
            if len(parts) > 1:
                parts[0] = replacement_number
                modified_line = ' '.join(parts)
                modified_lines.append(modified_line + '\n')
            else:
                # 行中只有一个数字，不作处理
                modified_lines.append(line)
        else:
            modified_lines.append(line)

    with open(file_path, 'w') as file:
        file.writelines(modified_lines)

# 定义一个函数，用于处理整个文件夹
def process_folder(folder_path, original_number, replacement_number):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".txt"):
                file_path = os.path.join(root, file)
                process_txt_file(file_path, original_number, replacement_number)
                print(f"Processed: {file_path}")

if __name__ =='__main__':
    # 指定要处理的文件夹目录
    folder_to_process = "/home/jiahan/Desktop/yolo-utils/YOLO_Format/labels"  # 替换成你的文件夹路径

    # 用户输入需要替换的数字
    original_number = '3'
    replacement_number = '0'

    process_folder(folder_to_process, original_number, replacement_number)
