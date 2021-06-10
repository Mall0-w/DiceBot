import random

numberOfStats = 6
''''
def messageHandler(message):
  if message.startswith('/roll'):
    

  return
'''
#given a number of dice (int) and how many faces (int) will sum num rolls of dice
def diceRoller(number, size):
  try:
    dNum = int(number)
  except:
    return "I can't do this; " + number + " is not a number"
  dNum = abs(dNum)
  try:
    dSize = int(size)
  except:
    return "I can't do this; " + size + " is not a number"
  dSize = abs(dSize)
  
  sum = 0
  allRolls = []
  for i in range(0,dNum):
    allRolls.append(random.randint(1,dSize))
    sum+= allRolls[i]
  
  return str(allRolls) + "\n" +str(sum)

def statRoller():
  startArr = []
  #large value, a d6 will never be greater than 9 
  for i in range(0, numberOfStats):
    tempSum = 0
    lowest = 0
    # roll 4d6
    for j in range(0, 4):
      tempRoll = int(diceRoller("1","6"))
      if lowest == 0 or tempRoll < lowest:
        tempSum += lowest
        lowest = tempRoll
      else:
        tempSum += tempRoll
    startArr.append(str(tempSum))
  
  return str(startArr)

def cocStatRoller():
  statArr = [[],[]]
  #number of stats = 2d6+6
  for i in range (3):
    statArr[0].append((int(diceRoller("2","6")) + 6)*5)
  
  for j in range(6):
    statArr[1].append(int(diceRoller("3","6"))*5)
  
  return statArr
  
    


