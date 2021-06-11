from occupations import strToOcc
class characterSheet:
  #TODO: add stat modifications for age
  #TODO: add occupations
  #TODO: add handling of wildcard skills and subskills like art(acting)
  #implement checking skills (to later roll improvement)
  #make choosing occupation easier on user by messing with the cases of string
  #implement improvement rolls
  #TODO: add the undoing of skill purchases
  #implement showing min and max cr
  #implement way to improve cthulhu mythos
  def __init__(self, name):
    self.name = name
    self.statDict = {"Str" : 50, "Dex" : 50, "Pow" : 50, "Con" : 50, "App" :50, "Edu" : 50, "Siz" : 50,"Int" : 50, "Luck" : 50}
    self.maxSan = 100
    self.updateHP()
    self.updateDBandBuild()
    self.updateMov()
    self.updateMP()
    self.updateHobby()
    self.san = self.statDict["Pow"]
    self.age = 20
    self.occupation = None
    self.occupationName = "None"
    self.skillDict = {"Accounting" :5, "Anthropology" : 1, "Appraise" : 5, "Archaeology" : 1, "Art" : 5, "Charm" : 15, "Climb":20, "Credit Rating": 0, "Cthulhu Mythos": 0, "Disguise":5, "Dodge":self.statDict["Dex"] / 2, "Drive Auto":20, "Elec. Repair" : 10, "Fast Talk": 5, "Fighting(brawl)" : 25, "Firearms(handgun)":20, "Firearms(rifle/shotgun)": 25, "First Aid" : 30, "History": 5, "Intimidate":15, "Jump":20, "Language(other)" :1, "Language(Own)":self.statDict["Edu"], "Law":5, "Library Use":20, "Listen":20, "Locksmith":1, "Mech. Repair": 10, "Medicine":1, "Natural World":10, "Navigate" :10, "Occult":5, "Op. Heav. Machine": 1,"Persuade": 10, "Pilot":1, "Psychology":10, "Psychoanalysis":1, "Ride":5, "Science":1, "Sleight Of Hand":10, "Spot Hidden": 25, "Stealth":20, "Survival":10, "Swim":20, "Throw":20, "Track": 10 }
    

  def __str__(self):
    return self.printCharSheet()
  
  def __repr__(self):
    return self.name

  def printCharSheet(self):
    return ("Name: " + self.name + " Age: " + str(self.age) +  "  Occupation:  " + self.occupationName
    + "\n"+ str(self.statDict) 
    +"\n" + "Hp: " + str(self.hp) + "  San: " + str(self.san) + "Mp: " + str(self.mp)
    +"\n" + "Mov: " + str(self.mov) + "  DB: " + str(self.db) + " Build:  " + str(self.build) +"\n\n" + str(self.skillDict))
  
  def updateMov(self):
    if self.statDict["Dex"] < self.statDict["Siz"] and self.statDict["Str"] < self.statDict["Siz"]:
      self.mov = 7
    elif self.statDict["Dex"] >= self.statDict["Siz"] and self.statDict["Str"] >= self.statDict["Siz"]:
      self.mov = 9
    else:
      self.mov = 8
    return


  def updateHP(self):
    self.hp = (self.statDict["Siz"] + self.statDict["Con"]) // 10
    return
  
  def updateMP(self):
    self.mp = self.statDict["Pow"] // 5

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

  def updateHobby(self):
    self.hobbyPoints = self.statDict["Int"] * 2
    return
  
  def showHobbyPoints(self):
    return "You have " + str(self.hobbyPoints) + " hobbypoints left"

  def setStat(self, statName, statVal):
    if statName.title() not in self.statDict:
      return (statName + " is not a valid stat. Please choose a stat from the following:\n" +
              str(self.statDict.items()))
    
    try:
      amt = int(statVal)
      amt = abs(amt)
    except:
      return amt + " is not a valid number"
    
    if amt >= 100:
      return "Attributes must be less than 100"
    
    self.statDict[statName.title()] = amt
    self.updateDBandBuild()
    self.updateHP()
    self.updateMov()
    self.updateMP()
    self.updateHobby()
    return statName.title() + " is now set to " + str(amt)
  
  def updateMaxSan(self):
    self.maxSan = 100 - self.skillDict["Cthulhu Mythos"]
  
  def setOcc(self, occName):
    try:
      self.occupation = strToOcc(occName.title())(self)
    except:
      return occName + " is not an occupation"

    self.occupationName = self.occupation.name
    self.skillDict["Credit Rating"] = self.occupation.minCR
    self.occupation.occPoints -= self.occupation.minCR
    return "occupation is now " + occName
  
  def showOccPoints(self):
    if self.occupation == None:
      return "You don't have an occupation"
    return "You have " + str(self.occupation.occPoints) + " occupation points left"
  
  def showOccSkills(self):
    if self.occupation == None:
      return "You don't have an occupation"
    return "Your occupation skills are " + str(self.occupation.occSkills)
  
  def buyOccSkill(self, skillName, amount):
    skill = skillName.title()
    if self.occupation == None:
      return "You need an occupation first, use /cocsetocc [occupation]"

    try:
      amt = abs(int(amount))
    except:
      return amount + " is not a number"

    if amt > self.occupation.occPoints:
      return "you don't have enough occupation points!"
    
    if skill == "Credit Rating" and self.skillDict[skill] + amt > self.occupation.maxCR:
      return "You cannot go over your occupation's max Credit Rating"

    if skill not in self.occupation.occSkills:
      if "Other" not in self.occupation.occSKills:
        return "You don't have access to this skill"
      self.occupation.occSkills.remove("Other")
      self.occupation.occSkills.append(skill)

    if self.skillDict[skill] + amt >= 100:
      return "skills must be less than 100"
    
    self.skillDict[skill] += amt
    self.occupation.occPoints -= amt
    return skillName + " is now at " + str(self.skillDict[skill])
  
  def buyHobbySkill(self, skillName, amount):
    skill = skillName.title()
    try:
      amt = abs(int(amount))
    except:
      return amount + " is not a number"

    if skill == "Cthulhu Mythos":
      return "A mere mortal cannot learn about the unseen forces in their free time!"

    if amt > self.hobbyPoints:
      return "you don't have enough occupation points!"
    
    if skill == "Credit Rating" and self.skillDict[skill] + amt > self.occupation.maxCR:
      return "You cannot go over your occupation's max Credit Rating"

    if self.skillDict[skill] + amt >= 100:
      return "skills must be less than 100"
    
    self.skillDict[skill] += amt
    self.hobbyPoints-= amt
    return skillName + " is now at " + str(self.skillDict[skill])

  
    
  

