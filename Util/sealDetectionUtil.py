from Util import pdf2ImgUtil
from Util import sealInfo
from Util import houghCircleUtil
from Util import sealNumIsCorrectUtil
def sealDetection(pdfName,pdfSrc):
    #获取该文件的印章参数
    sealInfoList=sealInfo.SealInfo(pdfName)
    minDist=sealInfoList[0]
    minRadius=sealInfoList[1]
    maxRadius=sealInfoList[2]
    #将该文件转化为JPG
    imglist = pdf2ImgUtil.pdf2Img(pdfSrc)
    #将Jpg输入基尔霍夫
    numlist=houghCircleUtil.detectCircles(imglist, minDist, minRadius,maxRadius)
    print(numlist)
    result = []
    if sealNumIsCorrectUtil.sealNumIsCorrect(pdfName, numlist, len(imglist))==False:
        checkResult={
            "result": pdfName + "缺少印章",
            "context": ""
        }
        result = {
            "checkDocName": pdfName,
            "checkResult":checkResult
        }
    return result