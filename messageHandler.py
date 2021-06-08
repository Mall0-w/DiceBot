import Dice
import characterSheet

def messageHandler(message):
  if(message.startswith("/roll")):
    newMessage = message.split(" ")
    del newMessage[0]
    if 'd' not in newMessage[0]:
      return "Dice should be inputed as /roll [num]d[dice size]"
    return Dice.diceRoller(''.join(newMessage[0].split('d')[0]), ''.join(newMessage[0].split('d')[1]))
  
  return None
    