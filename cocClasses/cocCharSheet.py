import occupations
from cocSkillSheet import cocSkillSheet
class cocSheet:
  def __init__(self, charName = "", occupation = occupations.Occupation()):
    #set occupation?
    self.name = charName
    self.Str = 0
    self.Dex = 0
    self.Pow = 0
    self.Con = 0
    self.App = 0
    self.Edu = 0
    self.Siz = 0
    self.Int = 0
    self.Luc = 0
    self.Edu = 0
    self.Hp = 0

    self.occPoints = occupation.getOccPoints
    self.skillSheet = cocSkillSheet()
    self.hobbyPoints = 0

    self.updateHobby()
    self.updateStatArr()
    self.updateMP()
    self.updateSan()
  
  #statArr should be in format of [[Siz, Edu, int], [Str, Con, Dex, App, Pow, Luck]]
  def updateStatArr(self):
    self.statArr = [[self.Siz, self.Edu, self.Int], [self.Str, self.Con, self.Dex, self.App, self.Pow, self.Luc]]
    
    self.updateHobby()
    self.updateMP()
    self.updateSan()
    return
  
  def updateMP(self):
    self.MP = self.Pow / 5
    return
  
  def getMP(self):
    return self.MP
  
  def updateSan(self):
    self.san = self.Pow
    return
  
  def getSan(self):
    return self.san

   #statArr should be in format of [[Siz, Edu, int], [Str, Con, Dex, App, Pow, Luck]]
  def setStats(self, statArr):
    #TODO: input checking
    self.Siz = int(statArr[0][0])
    self.Edu = int(statArr[0][1])
    self.Int = int(statArr[0][2])
    self.Str = int(statArr[1][0])
    self.Con = int(statArr[1][1])
    self.Dex = int(statArr[1][2])
    self.App = int(statArr[1][3])
    self.Pow = int(statArr[1][4])
    self.Luc = int(statArr[1][5])

    self.updateStatArr()
    return
  
  def getStats(self):
    return self.statArr
  
  def updateHobby(self):
    self.hobbyPoints = self.Int * 2
  
  def getHobby(self):
    return self.hobbyPoints
  
  
  

    