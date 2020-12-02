import json
# 不同文书对应的印章个数、以及一些基尔霍夫参数
# 8、拘留通知书（分局印共1个）
# 10、拘留证（分局印共1个）
# 12、立案告知书（分局印共1个）
# 14、受案登记表（分局印共1个）
# 16、搜查证（分局印共1个）
# 17、调取证据清单（分局印共1个）
# 18、调取证据通知书（分局印共1个）
# 28、传唤证（及传唤证副本）（每个犯罪嫌疑人各有一页，每页各有1个分局印）
# 31、扣押清单（分局印共1个） ？？
# 35、提请批准逮捕书（分局印共1个）
# 36、批准逮捕决定书（分局印共1个）
# 37、逮捕证（分局印共1个）

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