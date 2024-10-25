import os
import cv2

# 输入文件夹路径
input_folder = 'E:/DeepLearning/0_DataSets/WireRope-New/imgs'
# 输出文件夹路径
output_folder = 'E:/DeepLearning/0_DataSets/WireRope-New/crop'

# 创建输出文件夹（如果不存在）
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 遍历文件夹中的所有图片文件
for filename in os.listdir(input_folder):
    # 构建完整文件路径
    file_path = os.path.join(input_folder, filename)

    # 检查文件是否为图片（通过文件扩展名判断）
    if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp')):
        # 读取图片
        image = cv2.imread(file_path)

        # 获取图片的高度和宽度
        height, width = image.shape[:2]

        # 检查图片宽度是否为2048
        if width == 2048:
            # 计算裁剪的起始和结束位置，保留中间1024宽度的部分
            start_x = (width - 1024) // 2
            end_x = start_x + 1024
            cropped_image = image[:, start_x:end_x]

            # 保存裁剪后的图片到输出文件夹
            output_path = os.path.join(output_folder, filename)
            cv2.imwrite(output_path, cropped_image)
            print(f"已处理并保存图片: {filename}")
        else:
            print(f"跳过图片(宽度不是2048): {filename}")

print("所有图片处理完毕。")
