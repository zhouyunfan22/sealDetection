from Util import sealDetectionUtil

pdfSrc = "D:/fingerprintImg/test/113.pdf"
pdfName="调取证据清单"
if __name__ == '__main__':
   print(sealDetectionUtil.sealDetection(pdfName, pdfSrc))

