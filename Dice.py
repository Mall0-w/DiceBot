import random

numberOfStats = 6
''''
def messageHandler(message):
  if message.startswith('/roll'):
    

  return
'''
#given a number of dice (int) and how many faces (int) will sum num rolls of dice
def diceRoller(number, size):
  dNum = abs(number)
  dSize = abs(size)
  
  sum = 0
  for i in range(dNum):
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
      tempRoll = diceRoller("1","6")
      if lowest == 0 or tempRoll < lowest:
        tempSum += lowest
        lowest = tempRoll
      else:
        tempSum += tempRoll
    startArr.append(tempSum)
  
  return str(startArr)

