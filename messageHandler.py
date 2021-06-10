import Dice
import cocCharacterSheet

playerCharSheets = {}
activeCharSheets = {}

def messageHandler(message):
  #passed message getting its contents (string version)
  messageContents = message.content
  #splitting string into its sperate words
  newMessage = messageContents.split(" ")
  #if statements looking for commands
  if(messageContents.startswith("/roll")):
    del newMessage[0]
    #checking to see if command meets requirements
    if len(newMessage) == 0 or 'd' not in newMessage[0]:
      return "Dice should be inputed as /roll [num]d[dice size]"
      #if so call diceroller function and return its string to the bot
    return Dice.diceRoller(''.join(newMessage[0].split('d')[0]), ''.join(newMessage[0].split('d')[1]))
  
  elif(messageContents.startswith("/statroll")):
    return Dice.statRoller()
  
  elif(messageContents.startswith("/cocstatroll")):
    return Dice.cocStatRoller()
  
  elif(messageContents.startswith("/cocshow")):
    
    if message.author not in playerCharSheets:
      return "You don't have any character sheets"
    #if given a name, display that character sheet otherwise list all char sheets
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
    if temp.name in playerCharSheets[message.author]:
      return "You already have a character sheet named " + temp.name
    playerCharSheets[message.author][temp.name] = temp
    activeCharSheets[message.author] = temp.name
    return str(temp)
  
  elif(messageContents.startswith("/showactive")):
    if message.author not in activeCharSheets:
      return "you have no active character sheet"
    return "Your active character is: " + activeCharSheets[message.author]
  
  elif(messageContents.startswith("/changeactive")):
    if message.author not in playerCharSheets:
      return "You don't own any character sheets"
    if len(newMessage) < 2:
      return "I need the name of a character sheet you own"
    if newMessage[1] in playerCharSheets[message.author]:
      activeCharSheets[message.author] =  playerCharSheets[message.author][newMessage[1]].name
      return  activeCharSheets[message.author] + " is now your active character sheet"
    return "You don't own a character sheet by the name of " + newMessage[1]
  #TODO: need to find a way to store user char sheets and check if one exists
  #elif(message.startswith("/cocstatset")):

  
  return None
    