from ekispert.models.car import Car
from ..utils import Utils

class Formation(Utils):
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
      case "number":
        self.number = int(value)
      case "car":
        self.car = Car(value)
      case _:
        raise ValueError(f"key: {key} is not defined in Cost")
