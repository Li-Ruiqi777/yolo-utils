import os
from PIL import Image

# 定义文件夹路径
folder_path = 'E:\BaiduSyncdisk\DLPWeld\dataset_angleSteel\yolo-utils\VOC\JPEGImages'  # 替换为你要转换的文件夹路径

# 创建输出文件夹，存储转换后的图像
output_folder = os.path.join(folder_path, "./")
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 遍历文件夹中的所有文件
for filename in os.listdir(folder_path):
    if filename.endswith('.bmp'):
        # 获取完整文件路径
        bmp_path = os.path.join(folder_path, filename)
        
        # 打开BMP图像并转换为JPG
        with Image.open(bmp_path) as img:
            # 移除文件扩展名，得到纯文件名
            jpg_filename = os.path.splitext(filename)[0] + '.jpg'
            jpg_path = os.path.join(output_folder, jpg_filename)
            
            # 保存为JPG格式
            img.convert('RGB').save(jpg_path, 'JPEG')
        
        print(f"已将 {filename} 转换为 {jpg_filename}")

print("所有图片已转换完成！")
