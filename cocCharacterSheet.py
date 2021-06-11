from occupations import strToOcc
class characterSheet:
  #TODO: add stat modifications for age
  #TODO: add occupations
  #TODO: add skills
  #TODO: add wildcard skills and subskills like art(acting)
  #implement checking skills (to later roll improvement)
  #make choosing class easier on user by messing with the cases
  #implement improvement rolls
  def __init__(self, name):
    self.name = name
    self.statDict = {"STR" : 50, "DEX" : 50, "POW" : 50, "CON" : 50, "APP" :50, "EDU" : 50, "SIZ" : 50,"INT" : 50, "Luck" : 50}
    self.maxSan = 100
    self.updateHP()
    self.updateDBandBuild()
    self.updateMov()
    self.updateMP()
    self.san = self.statDict["POW"]
    self.age = 20
    self.occupation = None
    self.occupationName = "None"
    self.skillDict = {"ACCOUNTING" :5, "ANTHROPOLOGY" : 1, "APPRAISE" : 5, "ARCHAEOLOGY" : 1, "ART/CRAFT" : 5, "CHARM" : 15, "CLIMB":20, "CREDIT RATING": 0, "CTHULHU MYTHOS": 0, "DISGUISE":5, "DODGE":self.statDict["DEX"] / 2, "DRIVE AUTO":20, "ELEC. REPAIR" : 10, "FAST TALK": 5, "FIGHTING(BRAWL)" : 25, "FIREARMS(HANDGUN)":20, "FIREARMS(RIFLE/SHOTGUN)": 25, "FIRST AID" : 30, "HISTORY": 5, "INTIMIDATE":15, "JUMP":20, "LANGUAGE(OTHER)" :1, "LANGUAGE(OWN)":self.statDict["EDU"], "LAW":5, "LIBRARY USE":20, "LISTEN":20, "LOCKSMITH":1, "MECH. REPAIR": 10, "MEDICINE":1, "NATURAL WORLD":10, "NAVIGATE" :10, "OCCULT":5, "OP. HEAV. MACHINE": 1,"PERSUADE": 10, "PILOT":1, "PSYCHOLOGY":10, "PSYCHOANALYSIS":1, "RIDE":5, "SCIENCE":1, "SLEIGHT OF HAND":10, "SPOT HIDDEN": 25, "STEALTH":20, "SURVIVAL":10, "SWIM":20, "THROW":20, "TRACK": 10 }
    

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
    if self.statDict["DEX"] < self.statDict["SIZ"] and self.statDict["STR"] < self.statDict["SIZ"]:
      self.mov = 7
    elif self.statDict["DEX"] >= self.statDict["SIZ"] and self.statDict["STR"] >= self.statDict["SIZ"]:
      self.mov = 9
    else:
      self.mov = 8
    return


  def updateHP(self):
    self.hp = (self.statDict["SIZ"] + self.statDict["CON"]) // 10
    return
  
  def updateMP(self):
    self.mp = self.statDict["POW"] // 5

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
    
    if amt >= 100:
      return "Attributes must be less than 100"
    
    self.statDict[statName.upper()] = amt
    self.updateDBandBuild()
    self.updateHP()
    self.updateMov()
    self.updateMP()
    return statName.upper() + " is now set to " + str(amt)
  
  def updateMaxSan(self):
    self.maxSan = 100 - self.skillDict["Cthulhu Mythos"]
  
  def setOcc(self, occName):
    try:
      self.occupation = strToOcc(occName)(self)
    except:
      return occName + " is not an occupation"

    self.occupationName = self.occupation.name
    #print (self.name)
    print(self.occupation.occPoints)
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
    skill = skillName.upper()
    if self.occupation == None:
      return "You need an occupation first, use /cocsetocc [occupation]"

    try:
      amt = abs(int(amount))
    except:
      return amount + " is not a number"

    if amt > self.occupation.occPoints:
      return "you don't have enough occupation points!"

    if skill not in self.occupation.occSkills:
      if "Other" not in self.occupation.occSKills:
        return "You don't have access to this skill"
      self.occupation.occSkills.remove("Other")
      self.occupation.occSkills.append(skill)

    if self.skillDict[skill] + amt >= 100:
      return "skills must be less than 100"
    
    self.skillDict[skill] += amt
    self.occupation.occPoints -= amt
    return skillName + " is now at " + self.skillDict[skill]


  
    
  

