'''
为每个图片创建一个xml,即使该图片中没有正样本
'''
import os
import glob
import cv2
import threading
import queue

class CreateXml:
    def __init__(self,JpgPath: str, XmlPath: str):
        # 指定作为背景图片的图片路径
        self.JpgPath = JpgPath
        # 即将生成的xml存放路径
        self.XmlPath = XmlPath  
        # 创建读图线程以及处理线程，防止读图时间过长影响处理
        self.readimageThread = threading.Thread(target=self.readImg)
        self.createThread = threading.Thread(target=self.create)              
        # 获取所有图片的列表
        self.imglist = os.listdir(self.JpgPath)
        # 最大长度设定为列表总长度
        self.imgQueue = queue.Queue(maxsize=len(self.imglist))

    
    def readImg(self):
        for jpgFile in self.imglist:
            #不加后缀，用以拼接xml
            jpg_prefix = os.path.splitext(jpgFile)[0]
            # 图片全路径
            jpg_full_path = os.path.join(self.JpgPath, jpgFile)
            img = cv2.imread(jpg_full_path)
            width, height,channel = img.shape
            array = [jpgFile,jpg_prefix,jpg_full_path,width,height,channel]
            self.imgQueue.put(array) 
        print("写入图片线程已结束")


    def create(self):
        # 为了保险起见，所有图片都要被读完
        count = 0
        while True:
        # 如果数组不为空则进行处理
            try:
                imgArray = self.imgQueue.get(block=False)
                xmlFilepath = os.path.join(self.XmlPath, imgArray[1] + '.xml')
                with open(xmlFilepath,'w') as f:
                    f.write('<annotation>\n')
                    f.write('\t<folder>JPEGImages</folder>\n')
                    f.write('\t<filename>' + str(imgArray[0]) + '</filename>\n')
                    f.write('\t<path>' + str(imgArray[2]) + '</path>\n')
                    f.write('\t<source>\n')
                    f.write('\t\t<database>' + 'Unknown' + '</database>\n')
                    f.write('\t</source>\n')
                    f.write('\t<size>\n')
                    f.write('\t\t<width>' + str(imgArray[3]) + '</width>\n')
                    f.write('\t\t<height>' + str(imgArray[4]) + '</height>\n')
                    f.write('\t\t<depth>'+ str(imgArray[5])+'</depth>\n')
                    f.write('\t</size>\n')
                    f.write('\t<segmented>0</segmented>\n') 
                    f.write('</annotation>')
                print(f"{xmlFilepath} 已写入")
                count += 1

            except queue.Empty :
                # print("queue get失败，即将再次尝试")
                if count == len(self.imglist):
                    break

        print("写入xml线程已结束")

    def run(self):
        # 开始读图、处理线程
        self.readimageThread.start()
        self.createThread.start()      

if __name__ == "__main__": 
    Annotation = CreateXml(JpgPath='E:/DeepLearning/yolo-utils/VOC/JPEGImages',
                            XmlPath ='E:/DeepLearning/yolo-utils/temp')

    Annotation.run()
