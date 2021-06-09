from cocCharSheet import cocSheet
class Occupation:
  def __init__(self, charSheet = cocSheet()):
    self.occPoints = charSheet.Edu * 2
      
  @property
  def name(self):
    raise NotImplementedError
  
  @property
  def occSkills(self):
    raise NotImplementedError
  
  @property
  def occPoints(self):
    raise NotImplementedError
  
  @property
  def minCR(self):
    raise NotImplementedError
  
  @property
  def maxCR(self):
    raise NotImplementedError
  
  def getOccPoints(self):
    return self.occPoints
  
  def getMinCR(self):
    return self.minCR
  
  def getMaxCR(self):
    return self.maxCR

