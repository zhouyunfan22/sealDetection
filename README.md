
根据文书名称以及文书内容检测是否有印章，目前可检测以下文书\<br>
8、拘留通知书（分局印共1个）\<br>
10、拘留证（分局印共1个）\<br>
12、立案告知书（分局印共1个）\<br>
14、受案登记表（分局印共1个）\<br>
16、搜查证（分局印共1个）\<br>
17、调取证据清单（分局印共1个）\<br>
18、调取证据通知书（分局印共1个）\<br>
28、传唤证（及传唤证副本）（每个犯罪嫌疑人各有一页，每页各有1个分局印）\<br>
31、扣押清单（分局印共1个） \<br>
35、提请批准逮捕书（分局印共1个）\<br>
36、批准逮捕决定书（分局印共1个）\<br>
37、逮捕证（分局印共1个）\<br>


from Util import sealDetectionUtil\<br>
pdfSrc = "D:/fingerprintImg/test/113.pdf"\<br>
pdfName="调取证据清单"\<br>
if __name__ == '__main__':\<br>
   print(sealDetectionUtil.sealDetection(pdfName, pdfSrc))\<br>

