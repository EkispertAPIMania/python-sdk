from ..utils import Utils

class SectionSeparator(Utils):
  def __init__(self, data = None):
    super().__init__()
    if data is None:
      return
    self.sets(data)

  def sets(self, data: dict):
    for key in data:
      self.set(key, data[key])

  def set(self, key: str, value: any):
    match key.lower():
      case "divided":
        if value is not None:
          self.divided = bool(value)
      case "changeable":
        if value is not None:
          self.changeable = bool(value)
      case _:
        raise ValueError(f"key: {key} is not defined in SectionSeparator")
