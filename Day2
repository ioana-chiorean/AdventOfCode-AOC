# Using readlines() 
inputList = open('input.txt', 'r') 
lines = inputList.readlines()
nrPass = 0

for i in lines:
    minVal = i.split("-",1)[0]
    restVal = i.split("-",1)[1]
    maxVal = restVal.split(" ",1)[0]
    restVal = restVal.split(" ",1)[1]
    charVal = restVal.split(": ",1)[0]
    passVal = restVal.split(": ",1)[1]
    # print(minVal,maxVal, charVal, passVal)  

    countChar = passVal.count(charVal)
    # print(countChar)

    minVal = int(minVal)
    maxVal = int(maxVal)
   
    if countChar >= minVal and countChar <= maxVal:
        nrPass += 1
print(nrPass)

