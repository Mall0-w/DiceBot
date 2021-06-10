class characterSheet:
  #TODO: add stat modifications for age
  def __init__(self, name):
    self.name = name
    self.statDict = {"Str" : 50, "Dex" : 50, "Pow" : 50, "Con" : 50, "App" :50, "Edu" : 50, "Siz" : 50,"Int" : 50, "Luck" : 50}

    self.updateHP()
    self.updateDBandBuild()
    self.updateMov()
    self.san = self.statDict["Pow"]
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
    if self.statDict["Dex"] < self.statDict["Siz"] and self.statDict["Str"] < self.statDict["Siz"]:
      self.mov = 7
    elif self.statDict["Dex"] >= self.statDict["Siz"] and self.statDict["Str"] >= self.statDict["Siz"]:
      self.mov = 9
    else:
      self.mov = 8
    return


  def updateHP(self):
    self.hp = (self.statDict["Siz"] + self.statDict["Con"]) / 10
    return
  
  def updateDBandBuild(self):
    temp = (self.statDict["Siz"] + self.statDict["Str"])
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
    if statName not in self.statDict:
      return (statName + " is not a valid stat. Please choose a stat from the following:\n" +
              str(self.statDict.items()))
    
    try:
      amt = int(statVal)
      amt = abs(amt)
    except:
      return amt + " is not a valid number"
    
    if amt > 100:
      return "Amount must be less than 100"
    
    self.statDict[statName] = amt
    return statName + " is now set to " + amt

