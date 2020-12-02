def sealNumIsCorrect(pdfName,numList,pdfPageCount):
    sealNum=0
    for i in range(len(numList)):
        sealNum=sealNum+numList[i]
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
    print(sealNum)
    if pdfName=="逮捕证":
        for i in range(len(numList)):
            if numList[i]<1:
                return False
        return True

    if sealNum>=sealNumList.get(pdfName).get('sealNum'):
        return True
    return False