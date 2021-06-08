import random

numberOfStats = 6
''''
def messageHandler(message):
  if message.startswith('/roll'):
    

  return
'''
#given a number of dice (int) and how many faces (int) will sum num rolls of dice
def diceRoller(number, size):
  print(number)
  print(size)
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
  print(dNum)
  print(dSize)
  for i in range(0,dNum):
    sum += random.randint(1,dSize)
  
  return str(sum)

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

