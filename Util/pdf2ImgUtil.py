import fitz
import cv2
import numpy as np
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
    return imglist















        # print("list.len")
        # print(len(list))
        # # print(img_cv)
        # print("数组形状：", img_cv.shape)
        # num=houghCircleUtil.detectCircles(img_cv)



















        # return num
        # 保存为图片测试看看
        # cv2.imwrite('test\\m1.png', img_cv)
        # cv2.imshow('img_cv',img_cv)
        # cv2.waitKey(0)

        # pm.writePNG('D:/fingerprintImg/test/222.png')

