# 使用说明

> 以下所有脚本的执行路径都在此项目的根目录



1.创建VOC和YOLO格式的数据集的文件夹

```bash
python ./scripts/makedirs.py
```

执行后会得到如下目录结构：

```
├───VOC
│   ├───Annotations
│   └───JPEGImages
└───YOLO_Format
    ├───images
    │   ├───test
    │   ├───train
    │   └───val
    └───labels
        ├───test
        ├───train
        └───val
```



2.将标注图片放到`VOC/JPEGImages`中（提前把图片转成`.jpg`格式）



3.调用脚本`scripts\rename.py`对所有图片重命名



4.打开`eiseg`软件进行标注（通过`pip install eiseg`可以直接下载），数据格式选择XML



5.标注之前，先在右侧标签列表添加标签，如下图所示：

![alt text](<imgs/屏幕截图 2024-09-23 110945.png>)

并点击工具栏->标注->导出标签列表，导出的标签文件如下图所示：

![alt text](<imgs/屏幕截图 2024-09-23 111703.png>)
![alt text](<imgs/屏幕截图 2024-09-23 110017.png>)

下次标注相同任务时，直接点击工具栏->标注->载入标签列表，以确保标签的名称和顺序完全一致



6.标注好后，将label文件夹内的所有`.xml`文件放到`VOC/Annotations`下



7.调用脚本`scripts\xml2txt.py`将标签的格式转为YOLO格式。需要注意的是，此脚本中的“classes”列表需要按照标注时候的顺序填写标签名称，如下图所示：

![alt text](<imgs/屏幕截图 2024-09-24 171707.png>)



8.调用脚本`scripts\split_data.py`将数据集划分为训练集、验证集、测试集



9.修改`data.yaml`中的`path`和`names`字段：

- `path`：`YOLO_Format`文件夹的绝对路径
- `names`：需要与用eiseg进行标注时，各个label的顺序一直



10.调用脚本`scripts\train.py`即可开始训练YOLOv8模型

11.调用脚本`scripts\export.py`导出onnx格式的模型