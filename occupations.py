import sys

#Ik this is bad coding practice but im too lazy to figure out python abstraction

def strToOcc(str):
    try:
      return getattr(sys.modules[__name__], str)
    except:
      return None

class Antiquarian():
  def __init__(self, charSheet):
    self.name = "Antiquarian"
    self.occPoints = charSheet.statDict["Edu"] * 4
    self.minCR = 30
    self.maxCR = 70
    #arts/crafts is a wildcard
    #any other LANGUAGE
    #one other interpersonal skill
    self.occSkills = ["Appraise", "Art", "History" "Library Use", "Language(other)" "Interpersonal", "Spot Hidden", "Other", "Credit Rating"]

class Author():
  def __init__(self, charSheet):
    self.name = "Author"
    self.occPoints = charSheet.statDict["Edu"] * 4
    self.minCR = 9
    self.maxCR = 30
    #any other LANGUAGE
    #Natural world OR occult
    self.occSkills = ["Art(literature)", "History" ,"Library Use", "Natural World", "Occult" "Language(other)", "Language(own)", "Psychology", "Other", "Credit Rating"]

class Dilettante():
  def __init__(self, charSheet):
    self.name = "Dilettante"
    self.occPoints = charSheet.statDict["Edu"] * 2 + charSheet.staDict["App"] * 2
    self.minCR = 50
    self.maxCR = 99
    #any other LANGUAGE
    #Any arts and craft
    #any firearm
    #all other languages
    #one interpersonal skill
    self.occSkills = ["Art","Firearms","Language(other)","Ride", "Interpersonal","Credit Rating","Other", "Other", "Other"]

class Doctor():
  def __init__(self, charSheet):
    self.name = "Doctor of Medicine"
    self.occPoints = charSheet.statDict["Edu"] * 4
    self.minCR = 30
    self.maxCR = 80
    
    self.occSkills = ["First Aid", "Language(latin)", "Medicine", "Psychology", "Science(biology)", "Science(pharmacy)", "Other", "Other", "Credit Rating"]

class Journalist():
  def __init__(self, charSheet):
    self.name = "Journalist"
    self.occPoints = charSheet.statDict["Edu"] * 4
    self.minCR = 9
    self.maxCR = 30
    #one interpersonal
    self.occSkills = ["Art(photography)", "History", "Library Use", "Language(own)", "Interpersonal", "Psychology", "Other", "Other","Credit Rating"]

class Librarian():
  def __init__(self, charSheet):
    self.name = "Librarian"
    self.occPoints = charSheet.statDict["Edu"] * 4
    self.minCR = 9
    self.maxCR = 35
    #one other LANGUAGE
    self.occSkills = ["Accounting", "Library Use", "Language(other)", "Language(own)", "Other", "Other", "Other", "Other", "Credit Rating"]

class Detective():
  def __init__(self, charSheet):
    self.name = "Police Detective"
    self.occPoints = charSheet.statDict["Edu"] * 2 + max(charSheet.statDict["Str"], charSheet.statDict["Dex"]) *2
    self.minCR = 20
    self.maxCR = 50
    #acting or disguise
    #all firearms
    #one interpersonal
    self.occSkills = ["Art(acting)", "Disguise", "Firearms", "Law", "Listen", "Interpersonal", "Psychology", "Spot Hidden", "Other", "Credit Rating"]

class Professor():
  def __init__(self, charSheet):
    self.name = "Professor"
    self.occPoints = charSheet.statDict["Edu"] * 4
    self.minCR = 20
    self.maxCR = 70
    #one other LANGUAGE
    self.occSkills = ["Libarary Use", "Language(other)", "Language(own)", "Psychology", "Other", "Other", "Other", "Other", "Credit Rating"]

