from cocCharSheet import cocSheet
import sys

def str_to_class(classname):
    return getattr(sys.modules[__name__], classname)

def addOcc(name, charSheet):
  try:
    return str_to_class(name)(charSheet)
  except:
    return None


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

#TODO: Implement more occupation, currently only have lovecraftian implemented
#TODO: Implement skill wildcards
#Todo: implement choosing only one interpersonal
class Antiquarian(Occupation):
  def __init__(self, charSheet = cocSheet()):
    Occupation.__init__(self)
    self.occPoints = self.occPoints + charSheet.Edu * 2
    self.name = "Antiquarian"
    #Note: should only have access to one interpersonal skill of choice
    #note art should be wildcard
    self.occSkills = ["Appraise", "Art", "History", "Library Use", "Language(Other)", "Interpersonal", "Spot Hidden", "Other"]

    self.minCR = 30
    self.maxCr = 70

class Author(Occupation):
  def __init__(self, charSheet = cocSheet()):
    Occupation.__init__(self)
    self.occPoints = self.occPoints + charSheet.Edu * 2
    self.name = "Author"
    #note Art should be literature
    #nat world or occult
    self.occSkills = ["Art", "History", "Library Use", "Natural World", "Occult", "Language(Other)", "Language(Own)", "Psychology", "Other"]

    self.minCR = 9
    self.maxCR = 30

class Dilettante(Occupation):
  def __init__(self, charSheet = cocSheet()):
    Occupation.__init__(self)
    self.occPoints = self.occPoints + charSheet.App * 2
    self.name = "Dilettante"
    #Art should be wildcard
    #Firearm should be wildcard
    #all other languages
    self.occSkills = ["Art", "Firearms", "Language(Other)", "Ride", "Interpersonal", "Other", "Other", "Other"]

    self.minCR = 50
    self.maxCr = 99

class Doctor(Occupation):
  def __init__(self, charSheet = cocSheet()):
    Occupation.__init__(self)
    self.Occpoints = self.occPoints + charSheet.Edu * 2
    self.name = "Doctor of Medicine"
    #Other Language should be Latin
    #science is biology and pharmacy

    self.occSkills = ["First Aid", "Language(Other)", "Medicine", "Psychology", "Science", "Science", "Other", "Other"]

    self.minCR = 50
    self.maxCR = 99

class Journalist(Occupation):
  def __init__(self, charSheet = cocSheet()):
    Occupation.__init__(self)
    self.OccPoints = self.occPoints + charSheet.Edu * 2
    self.name = "Journalist"
    #art should be photography
    self.occSkills = ["Art", "History", "Library Use", "Language(Own)", "Interpersonal", "Psychology", "Other", "Other"]

    self.minCR = 9
    self.maxCR = 30

class Librarian(Occupation):
  def __init__(self, charSheet = cocSheet()):
    Occupation.__init__(self)
    self.occPoints = self.occPoints + charSheet.Edu * 2
    self.name = "Librarian"

    self.occSkills = ["Accounting", "Library Use", "Language(Other)", "Language(Own)", "Other", "Other", "Other", "Other"]

    self.minCR = 9
    self.maxCR = 35

class Detective(Occupation):
  def __Init__(self, charSheet = cocSheet()):
    Occupation.__init__(self)
    self.occPoints = self.occPoints + max(charSheet.Str, charSheet.Dex) * 2
    self.name = "Police Detective"
    #either art(acting) or disguise
    #all firearms
    self.occSkills = ["Art", "Disguise", "Firearms", "Law", "Listen", "Interpersonal", "Psychology", "Spot Hidden", "Other"]

    self.minCR = 20
    self.maxCR = 50

class Proffesor(Occupation):
  def __Init__(self, charSheet = cocSheet()):
    Occupation.__Init__(self)
    self.occPoints = self.occPoints + charSheet.Edu * 2
    self.name = "Proffesor"

    #Other language is wildcard
    self.occSkills = ["Library Use", "Language(Other)", "Language(Own)", "Psychology", "Other", "Other", "Other","Other"]

    self.minCR = 20
    self.maxCR = 70

