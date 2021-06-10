class characterSheet:
  #TODO: add stat modifications for age
  def __init__(self, name):
    self.name = name
    self.statDict = {"STR" : 50, "DEX" : 50, "POW" : 50, "CON" : 50, "APP" :50, "EDU" : 50, "SIZ" : 50,"INT" : 50, "Luck" : 50}

    self.updateHP()
    self.updateDBandBuild()
    self.updateMov()
    self.san = self.statDict["POW"]
    self.age = 20

  def __str__(self):
    return self.printCharSheet()
  
  def __repr__(self):
    return self.name

  def printCharSheet(self):
    return ("Name: " + self.name + " Age: " + str(self.age) + "\n"+ str(self.statDict) 
    +"\n" + "Hp: " + str(self.hp) + "  San: " + str(self.san)
    +"\n" + "Mov: " + str(self.mov) + "  DB: " + str(self.db) + " Build:  " + str(self.build) )
  
  def updateMov(self):
    if self.statDict["DEX"] < self.statDict["SIZ"] and self.statDict["STR"] < self.statDict["SIZ"]:
      self.mov = 7
    elif self.statDict["DEX"] >= self.statDict["SIZ"] and self.statDict["STR"] >= self.statDict["SIZ"]:
      self.mov = 9
    else:
      self.mov = 8
    return


  def updateHP(self):
    self.hp = (self.statDict["SIZ"] + self.statDict["CON"]) / 10
    return
  
  def updateDBandBuild(self):
    temp = (self.statDict["SIZ"] + self.statDict["STR"])
    if temp <= 64:
      self.db, self.build = -2,-2
    elif 64 < temp <= 84:
      self.db, self.build = -1,-1
    elif 84 < temp <= 124:
      self.db, self.build = 0,0
    elif 124 < temp <= 164:
      self.db, self.build = "1d4", 1
    else:
      self.db, self.build = "1d6", 2
    return

  def setStat(self, statName, statVal):
    if statName.upper() not in self.statDict:
      return (statName + " is not a valid stat. Please choose a stat from the following:\n" +
              str(self.statDict.items()))
    
    try:
      amt = int(statVal)
      amt = abs(amt)
    except:
      return amt + " is not a valid number"
    
    if amt > 100:
      return "Amount must be less than 100"
    
    self.statDict[statName.upper()] = amt
    return statName.upper() + " is now set to " + str(amt)

