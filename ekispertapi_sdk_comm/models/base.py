from ..utils import Utils
from .point import Point

class Base(Utils):
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
      case "point":
        self.point = Point(value)
      case _:
        raise ValueError(f"key: {key} is not defined in Base")
