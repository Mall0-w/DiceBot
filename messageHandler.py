import Dice
import cocCharacterSheet

playerCharSheets = {}

def messageHandler(message):
  messageContents = message.content
  newMessage = messageContents.split(" ")
  if(messageContents.startswith("/roll")):
    del newMessage[0]
    if 'd' not in newMessage[0]:
      return "Dice should be inputed as /roll [num]d[dice size]"
    return Dice.diceRoller(''.join(newMessage[0].split('d')[0]), ''.join(newMessage[0].split('d')[1]))
  
  elif(messageContents.startswith("/statroll")):
    return Dice.statRoller()
  
  elif(messageContents.startswith("/cocstatroll")):
    return Dice.cocStatRoller()
  
  elif(messageContents.startswith("/cocshow")):
    if message.author not in playerCharSheets:
      return "You don't have any character sheets"
    if len(newMessage) > 1:
      if newMessage[1] in playerCharSheets[message.author]:
        return str(playerCharSheets[message.author][newMessage[1]])
      else:
        return "You don't have a character sheet named " + newMessage[1]
    
    return str(list((playerCharSheets[message.author]).keys()))
  
  elif(messageContents.startswith("/coccreate")):
    
    if(len(newMessage) < 2):
      return "I need a name for your sheet"
    temp = cocCharacterSheet.characterSheet(newMessage[1])
    if message.author not in playerCharSheets:
      playerCharSheets[message.author]= {}
      playerCharSheets[message.author][temp.name] = temp
    return str(temp)
  
  #TODO: need to find a way to store user char sheets and check if one exists
  #elif(message.startswith("/cocstatset")):

  
  return None
    