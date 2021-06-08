import Dice

class character:

  def __init__(self, charName = "", charClass = "", charSub = ""):
    self.Str = 0
    self.Dex = 0
    self.Con = 0
    self.Int = 0
    self.Wis = 0
    self.Cha = 0
    self.name = charName
    #self.race = charRace
    self.cla = charClass
    self.subCla = charSub
  #funtionality

  def setStats(self,statArr):
    if len(statArr != 6):
      return 1
    self.setStr(statArr[0])
    self.setDex(statArr[1])
    self.setCon(statArr[2])
    self.setInt(statArr[3])
    self.setWis(statArr[4])
    self.setCha(statArr[5])

#####ALL INDIVIDUAL SETTERS/GETTERS###
  def setName(self, newName):
    self.name = newName
    return
  def getName(self):
    return self.name

  def setClass(self, newClass):
    self.cla = newClass
    return
  def getClass(self):
    return self.cla
  
  def setSubCla(self, newSub):
    self.subCla = newSub
    return
  def getSubCla(self):
    return self.subCla

  def setStrength(self, num):
    self.Str = num
    return
  def setDexterity(self, num):
    self.Dex = num
    return
  def setConstitution(self, num):
    self.Con = num
    updateHp(self)
    return
  def setWisdom(self, num):
    self.Wis = num
    return
  def setIntelligence(self, num):
    self.Int = num
    return
  def setCharisma(self, num):
    self.Char = num
    return