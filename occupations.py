import sys

def strToOcc(str):
    try:
      return getattr(sys.modules[__name__], str)
    except:
      return None

class Antiquarian():
  def __init__(self, charSheet):
    self.name = "Antiquarian"
    self.occPoints = charSheet.statDict["EDU"] * 4
    self.minCR = 30
    self.maxCR = 70
    #arts/crafts is a wildcard
    #any other LANGUAGE
    #one other interpersonal skill
    self.occSkills = ["APPRAISE", "ART", "HISTORY" "LIBRARY USE", "LANGUAGE(OTHER)" "INTERPERSONAL", "SPOT HIDDEN", "OTHER"]