# -*- coding:utf-8 -*-
import io
import sys
import json
import numpy as np
import cv2
import fitz




sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
class SealCheck():
    def __init__(self,RootPath):
         self.RootPath = RootPath
    def file_name(self,RootPath):
         for root, dirs, files in os.walk(RootPath):
             return list(files)

    #不同文书对应的印章基尔霍夫参数
    def SealInfo(pdfName):
        result = []
        sealSizeList = {
            '拘留证': {'minDist': 100, 'minRadius': 100, 'maxRadius': 130},
            '拘留证': {'minDist': 100, 'minRadius': 100, 'maxRadius': 130},
            '立案告知书': {'minDist': 100, 'minRadius': 100, 'maxRadius': 130},
            '受案登记表': {'minDist': 100, 'minRadius': 100, 'maxRadius': 130},
            '搜查证': {'minDist': 100, 'minRadius': 100, 'maxRadius': 130},
            '调取证据清单': {'minDist': 100, 'minRadius': 100, 'maxRadius': 130},
            '调取证据通知书': {'minDist': 100, 'minRadius': 100, 'maxRadius': 130},
            '扣押清单': {'minDist': 100, 'minRadius': 100, 'maxRadius': 130},
            '提请批准逮捕书': {'minDist': 100, 'minRadius': 100, 'maxRadius': 130},
            '批准逮捕决定书': {'minDist': 100, 'minRadius': 100, 'maxRadius': 130},
            '逮捕证': {'minDist': 100, 'minRadius': 100, 'maxRadius': 130},
            '传唤证': {'minDist': 100, 'minRadius': 100, 'maxRadius': 130}
        }

        result.append(sealSizeList.get(pdfName).get('minDist'))
        result.append(sealSizeList.get(pdfName).get('minRadius'))
        result.append(sealSizeList.get(pdfName).get('maxRadius'))
        return result

    #校验印章个数是否符合规定
    def sealNumIsCorrect(pdfName,numList,pdfPageCount):
        sealNum=0
        for i in range(len(numList)):
            sealNum=sealNum+numList[i]
        print("印章总个数")
        print(sealNum)
        sealNumList = {
            '拘留证': {'sealNum': 1},
            '拘留证': {'sealNum': 1},
            '立案告知书': {'sealNum': 1},
            '受案登记表': {'sealNum': 1},
            '搜查证': {'sealNum': 1},
            '调取证据清单': {'sealNum': 1},
            '调取证据通知书': {'sealNum': 1},
            '扣押清单': {'sealNum': 1},
            '提请批准逮捕书': {'sealNum': 1},
            '批准逮捕决定书': {'sealNum': 1},
            '逮捕证': {'sealNum': pdfPageCount}
        }
        if pdfName=="逮捕证":
            for i in range(len(numList)):
                if numList[i]<1:
                    return False
            return True

        if sealNum>=sealNumList.get(pdfName).get('sealNum'):
            print("印章完整")
            return True
        print("缺少印章")
        return False

    #单个pdf转jpg
    def pdf2Img(src):
        doc = fitz.open(src)
        imglist = []
        for pg in range(doc.pageCount):
            page = doc[pg]
            rotate = int(0)
            # 每个尺寸的缩放系数为2，这将为我们生成分辨率提高四倍的图像。
            zoom_x = 2.0
            zoom_y = 2.0
            trans = fitz.Matrix(zoom_x, zoom_y).preRotate(rotate)
            pm = page.getPixmap(matrix=trans, alpha=False)
            getpngdata = pm.getImageData(output="png")
            image_array = np.frombuffer(getpngdata, dtype=np.uint8)
            img_cv = cv2.imdecode(image_array, cv2.IMREAD_ANYCOLOR)
            imglist.append(img_cv)
        #返回单个pdf转jpg之后的图片列表
        return imglist

    #图片列表基尔霍夫画圆
    def detectCircles(imglist, minDist, minRadius, maxRadius):
        numlist=[]
        # 加载图像
        # image = cv2.imread('D:/fingerprintImg/test/16.jpg')
        for i in range(len(imglist)):
            output = imglist[i].copy()
            # 转换成灰度图像
            gray = cv2.cvtColor(imglist[i], cv2.COLOR_BGR2GRAY)
            # 检测圆
            circles = cv2.HoughCircles(gray,cv2.HOUGH_GRADIENT,1,minDist,param1=100,param2=30,minRadius=minRadius,maxRadius= maxRadius)
            # 确保至少找到一个圆
            num=0
            if circles is not None:
                # 将圆(x, y)坐标和半径转换成int
                circles = np.round(circles[0, :]).astype('int')
                for (x, y, r) in circles:
                    num=num+1
                    # 绘制圆和半径矩形到output
                    cv2.circle(output, (x, y), r, (0, 255, 0), 4)
                    cv2.rectangle(output, (x-5, y-5), (x+5, y+5), (0, 128, 255), -1)

                output = cv2.resize(output, (800, 800))
                cv2.imshow('result',output)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
            numlist.append(num)
        return numlist

    #单个pdf印章检测
    def sealDetection(pdfName,pdfSrc):
        #获取该文件的印章参数
        sealInfoList=SealCheck.SealInfo(pdfName)
        minDist=sealInfoList[0]
        minRadius=sealInfoList[1]
        maxRadius=sealInfoList[2]
        #将该文件转化为JPG
        imglist = SealCheck.pdf2Img(pdfSrc)
        #将Jpg输入基尔霍夫
        numlist=SealCheck.detectCircles(imglist, minDist, minRadius,maxRadius)
        # print(SealCheck.sealNumIsCorrect(pdfName, numlist, len(imglist)))
        print("印章列表")
        print(numlist)
        result = []
        if SealCheck.sealNumIsCorrect(pdfName, numlist, len(imglist))==False:
            checkResult={
                "result": pdfName + "缺少印章",
                "context": ""
            }
            result = {
                "checkDocName": pdfName,
                "checkResult":checkResult
            }
        print("检验结果")
        print(result)
        return result


if __name__ == "__main__":
    pdfSrc = "D:/fingerprintImg/test/113.pdf"
    pdfName="调取证据清单"
    SealCheck.sealDetection(pdfName,pdfSrc)

