import numpy as np
import cv2
def detectCircles():
# 加载图像
    image = cv2.imread('D:/fingerprintImg/test/16.jpg')
    output = image.copy()
    # 转换成灰度图像
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# 	cv2.imshow('gray',gray)
# 	cv2.waitKey(0)
    # 检测圆
    circles = cv2.HoughCircles(gray,cv2.HOUGH_GRADIENT,1,100,param1=100,param2=30,minRadius=100,maxRadius=130)
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
        print(num)
# 		cv2.imshow('output', np.hstack([image, output]))
        cv2.imshow('output',output)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    return