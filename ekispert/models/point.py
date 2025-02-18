from ..model import Model
from .station import Station
from .prefecture import Prefecture
from .geo_point import GeoPoint
from .cost import Cost
from .status import Status

class Point(Model):
  def __init__(self, data = None):
    super().__init__()
    self.costs = []
    if data is None:
      return
    self.sets(data)

  def sets(self, data):
    for key in data:
      self.set(key, data[key])

  def set(self, key: str, value: any):
    match key.lower():
      case "station":
        self.station = Station(value)
      case "prefecture":
        self.prefecture = Prefecture(value)
      case "geopoint":
        self.geo_point = GeoPoint(value)
      case "cost":
        costs = self.get_as_array("costs")
        self.costs = list(map(lambda x: Cost(x), costs))
      case "status":
        self.status = Status(value)
      case "serializedata":
        self.serialize_data = value
      case _:
        raise ValueError(f"key: {key} is not defined in Station")
