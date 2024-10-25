'''
本文件的作用：使用已经训练好的模型对新采集的数据做个初次标注,并且剔除完全没有目标对象的图片
'''

from ultralytics import YOLO
import os
import shutil

#--------------------------- CONFIG ---------------------------#
Projet_name = "make_label_ship_outside" 
weights_dir = 'yolov8n-shipinside.pt'
dataset_dir = 'F:/DeepLearning/0_DataSets/inside_new'
origin_imgs_dir = '' # 存放有目标的原图的目录(不需要自己写,后边代码会填充)
#--------------------------- CONFIG ---------------------------#

model = YOLO(weights_dir)

# 好像不能通过改cfg文件来修改配置,必须显式地写传入函数
results = model.predict(source=dataset_dir,
                        conf=0.4,
                        iou=0.6,
                        show_labels=True,
                        show_conf=True,
                        #line_width=1,
                        save=True,
                        save_txt=True,
                        name=Projet_name # 保存结果的文件夹名
                        )

# results[0].save_dir:由框架自动决定的保存路径,在`runs`下
origin_imgs_dir = os.path.join(results[0].save_dir,'origin_imgs')
os.mkdir(origin_imgs_dir)

######################## 把 "有目标物体的原始图片" 移到origin_imgs_dir路径下 ##################
i = 0
for r in results:
    # 这个条件应该根据实际需求来动态改变，以过滤掉不符合的
    if len(r.boxes)!=0 and r.boxes.cls[0].item()==0: #0:ship
        shutil.copy2(r.path,origin_imgs_dir)
        i=i+1


print(f'总共{len(results)}张图片')
print(f'共移动{i}张图片')

############################# 删掉多余的label #############################

# 获取label文件夹中的所有文件名（不带后缀）
label_dir = os.path.join(results[0].save_dir,'labels')
label_files = set([os.path.splitext(file)[0] for file in os.listdir(label_dir)])

# 获取origin_imgs文件夹中的所有文件名（不带后缀）
imgs_files = set([os.path.splitext(file)[0] for file in os.listdir(origin_imgs_dir)])

# 需要删除的文件列表
delete_files = label_files - imgs_files

# 删除文件
for file in delete_files:
    file_path = os.path.join(label_dir, file)+'.txt'
    os.remove(file_path)
    print(f"删除文件: {file_path}")
print("删除操作完成")

############################# 移动预测结果到pridict文件夹中 #############################
pridict_dir = os.path.join(results[0].save_dir,'pridcit')
if not os.path.exists(pridict_dir):
    os.makedirs(pridict_dir)

# 获取源文件夹中所有图片文件
image_files = [f for f in os.listdir(results[0].save_dir) if os.path.isfile(os.path.join(results[0].save_dir, f)) and f.lower().endswith(('.jpg'))]

# 移动图片文件到目标文件夹
for image_file in image_files:
    source_path = os.path.join(results[0].save_dir, image_file)
    target_path = os.path.join(pridict_dir, image_file)
    shutil.move(source_path, target_path)
    print(f"移动文件: {source_path} 到 {target_path}")
print("移动操作完成")