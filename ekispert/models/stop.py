from ekispert.models.operational_state import OperationalState
from ekispert.models.point import Point
from ..base import Base

class Stop(Base):
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
      case "arrivalstate":
        self.arrival_state = OperationalState(value)
      case "departurestate":
        self.departure_state = OperationalState(value)
      case "point":
        self.point = Point(value)
      case _:
        raise ValueError(f"key: {key} is not defined in Stop")
