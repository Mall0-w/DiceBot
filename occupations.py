import sys

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