from ..utils import Utils
from collections import namedtuple

Means = namedtuple('Means', 'type')

class Car(Utils):
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
      case "index":
        self.index = int(value)
      case "number":
        self.number = value
      case "means":
        self.means = Means(
          type = value["Type"])
      case _:
        raise ValueError(f"key: {key} is not defined in Car")
