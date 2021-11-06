def checkLuhn(cardNo):
    nDigits = len(cardNo)
    nSum = 0
    isSecond = False
    for i in range(nDigits - 1, -1, -1):
        d = ord(cardNo[i]) - ord('0')
        if (isSecond == True):
            d = d * 2
        nSum += d // 10
        nSum += d % 10
        isSecond = not isSecond
    if (nSum % 10 == 0):
    	return True
    else:
    	return False
if __name__=="__main__":
    cardNo = "5178059711741695"
    if (checkLuhn(cardNo)):
        print("This is a valid card")
    else:
        print("This is not a valid card")