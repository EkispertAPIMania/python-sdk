from ekispert.models.formation import Formation
from ..utils import Utils

class Change(Utils):
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
      case "nextlinedirection":
        self.next_line_direction = value
      case "openside":
        self.open_side = value
      case "formation":
        self.formation = Formation(value)
      case _:
        raise ValueError(f"key: {key} is not defined in Change")

