import occupations



class cocSheet:
  def __init__(self, charName = ""):
    
    #TODO: reserve setting occpoints and hobbyPoints for when stats are set

    #set occupation?
    #Init with stat array makes most sense
    #need to figure out how to init occ given name of occ
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
    #TODO: need to do something if occupation DNE
    self.occupation = None
    self.occPoints = 0
    self.hobbyPoints = 0

    self.updateHobby()
    self.updateStatArr()
    self.updateMP()
    self.updateSan()
  
  def setOcc(self, occ = "Antiquarian"):
    temp = occupations.addOcc(occ)
    if temp == None:
      return occ + " is an invalid occupation"
    self.occupation = temp
    
    self.occPoints = self.occupation.occPoints
    return "Occupation set to " + occ


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
  
  def updateSan(self):
    self.san = self.Pow
    return

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
  
  
  def updateHobby(self):
    self.hobbyPoints = self.Int * 2
  
  
  
  
  

    