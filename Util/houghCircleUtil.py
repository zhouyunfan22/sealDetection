import numpy as np
import cv2


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

# import numpy as np
# import cv2
# def detectCircles(imglist):
#     numlist=[]
#     # 加载图像
#     # image = cv2.imread('D:/fingerprintImg/test/16.jpg')
#     for i in range(len(imglist)):
#         output = imglist[i].copy()
#         # 转换成灰度图像
#         gray = cv2.cvtColor(imglist[i], cv2.COLOR_BGR2GRAY)
#         # 检测圆
#         circles = cv2.HoughCircles(gray,cv2.HOUGH_GRADIENT,1,100,param1=100,param2=30,minRadius=100,maxRadius=130)
#         # 确保至少找到一个圆
#         num=0
#         if circles is not None:
#             # 将圆(x, y)坐标和半径转换成int
#             circles = np.round(circles[0, :]).astype('int')
#             for (x, y, r) in circles:
#                 num=num+1
#                 # 绘制圆和半径矩形到output
#                 cv2.circle(output, (x, y), r, (0, 255, 0), 4)
#                 cv2.rectangle(output, (x-5, y-5), (x+5, y+5), (0, 128, 255), -1)
#
#             output = cv2.resize(output, (800, 800))
#             cv2.imshow('result',output)
#             cv2.waitKey(0)
#             cv2.destroyAllWindows()
#         numlist.append(num)
#     return numlist
