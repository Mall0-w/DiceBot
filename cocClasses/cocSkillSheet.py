from cocCharSheet import cocSheet
class cocSkillSheet:
  def __init__(self, charSheet = cocSheet()):
    self.SkillMap = {}
    self.SkillMap["Accounting"]= 5
    self.SkillMap["Anthropology"] = 1
    self.SkillMap["Appraise"] = 5
    self.SkillMap["Archaeology"] = 1
    self.SkillMap["Art"] = 5
    self.SkillMap["Charm"] = 15
    self.SkillMap["Climb"] = 20
    
    
    self.SkillMap["Credit Rating"] = charSheet.occupation.getMinCR()
    charSheet.occPoints -= charSheet.occupation.getMinCR()

    self.SkillMap["Cthulhu Mythos"] = 0
    self.SkillMap["Disguise"] = 5

    #should be charSheet should be a coc sheet
    self.SkillMap["Dodge"] = charSheet.Dex/2
    self.SkillMap["Drive Auto"] = 20
    self.SkillMap["Elec. Rep"] = 10
    self.SkillMap["Fast Talk"] = 5
    self.SkillMap["Fighting(Brawl)"] = 25
    self.SkillMap["Firearms(Handgun)"] = 20
    self.SkillMap["Firearms Rifle"] = 25
    self.SkillMap["First Aid"] = 30
    self.SkillMap["History"] = 5
    self.SkillMap["Intimidate"] = 15
    self.SkillMap["Jump"] = 20
    self.SkillMap["Language(Other)"] = 1
    self.SkillMap["Language(Own)"] = charSheet.Edu
    self.SkillMap["Law"] = 5
    self.SkillMap["Library Use"] = 20
    self.SkillMap["Listen"] = 20
    self.SkillMap["Locksmith"] = 1
    self.SkillMap["Mech. Repair"] = 10
    self.SkillMap["Medicine"] = 1
    self.SkillMap["Natural World"] = 10
    self.SkillMap["Navigate"] = 10
    self.SkillMap["Occult"] = 5
    self.SkillMap["Op. Hv. Machine"] = 1
    self.SkillMap["Persuade"] = 10
    self.SkillMap["Pilot"] = 1
    self.SkillMap["Psychology"] = 10
    self.SkillMap["Psychonalysis"] = 1
    self.SkillMap["Ride"] = 5
    self.SkillMap["Science"] = 1
    self.SkillMap["Sleight Of Hand"] = 10
    self.SkillMap["Spot Hidden"] = 25
    self.SkillMap["Stealth"] = 20
    self.SkillMap["Survival"] = 10
    self.SkillMap["Swim"] = 20
    self.SkillMap["Throw"] = 20
    self.SkillMap["Track"] = 10

  def buyHobbySkill(self, skill, amt):
    if skill == "Cthulhu Mythos":
      return "A lowly mortal cannot learn about the unseen as a hobby"

    if skill not in self.SkillMap:
      return skill + " is not a skill"
    
    if amt > self.charSheet.hobbyPoints:
      return "I can't do this; you only have " + str(self.charSheet.hobbyPoints) + " hobby points left"
    
    if self.SkillMap[skill] + amt > 99:
      return "skills can only have a maximum of 99"
    
    self.SkillMap[skill] += amt
    self.charSheet.hobbyPoints -= amt

    return str(amt) + " hobby points spent! Your remaining balance is: " + self.charSheet.hobbyPoints + "\n" + skill + " is now at " + self.SkillMap[skill] 

  def buyOccSkill(self, skill, amt):
    if skill not in self.charSheet.occupation.occSkills:
      return "You cannot invest occupation points into this skill only in: " + str(self.charSheet.occupation.occSkills)
    
    if amt > self.charSheet.occPoints:
      return "I can't do this; you only have " + str(self.charSheet.occPoints) + " Occupational points left"
    
    if self.SkillMap[skill] + amt > 99:
      return "skills can only have a maximum of 99"
    self.SkillMap[skill] += amt
    self.charSheet.occPoints -= amt

    return str(amt) + " Occupational points spent! Your remaining balance is: " + self.charSheet.occPoints + "\n" + skill + " is now at " + self.SkillMap[skill] 

  #TODO: improvement rolls, coc improvement, undoing bought points
    

    
