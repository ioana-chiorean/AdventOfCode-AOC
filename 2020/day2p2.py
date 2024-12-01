# Using readlines() 
inputList = open('input.txt', 'r') 
lines = inputList.readlines()
nrPass = 0

def policy(passVal,minVal, maxVal, charVal):
    return (passVal[minVal-1] == charVal) ^ (passVal[maxVal-1] == charVal)

for i in lines:
    minVal = i.split("-",1)[0]
    restVal = i.split("-",1)[1]
    maxVal = restVal.split(" ",1)[0]
    restVal = restVal.split(" ",1)[1]
    charVal = restVal.split(": ",1)[0]
    passVal = restVal.split(": ",1)[1]
    # print(minVal,maxVal, charVal, passVal)  
    minVal = int(minVal)
    maxVal = int(maxVal)
    if policy(passVal,minVal, maxVal, charVal):
        nrPass += 1
print(nrPass)

