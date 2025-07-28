from ekispert.models.line import Line
from ekispert.models.point import Point
from ..utils import Utils

class Route(Utils):
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
      case "distance":
        self.distance = int(value)
      case "exhaustco2":
        self.exhaust_co2 = int(value)
      case "exhaustco2atpassengercar":
        self.exhaust_co2_at_passenger_car = int(value)
      case "timeOnboard":
        self.time_on_board = int(value)
      case "timeother":
        self.time_other = int(value)
      case "timewalk":
        self.time_walk = int(value)
      case "transfercount":
        self.transfer_count = int(value)
      case "line":
        value = self.get_as_array(value)
        self.lines = []
        for v in value:
          if v is not None:
            self.lines.append(Line(v))
      case "point":
        value = self.get_as_array(value)
        self.points = []
        for v in value:
          if v is not None:
            self.points.append(Point(v))
      case "timeonboard":
        self.time_on_board = int(value)
      case _:
        raise ValueError(f"key: {key} is not defined in Route")