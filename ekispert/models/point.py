from ..utils import Utils
from .station import Station
from .prefecture import Prefecture
from .geo_point import GeoPoint
from .cost import Cost
from collections import namedtuple

Status = namedtuple('Status', 'code')

class Point(Utils):
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
      case "geton":
        self.get_on = value
      case "getoff":
        self.get_off = value
      case "cost":
        costs = self.get_as_array(value)
        self.costs = list(map(lambda x: Cost(x), costs))
      case "status":
        self.status = Status(
          code = value
        )
      case "serializedata":
        self.serialize_data = value
      case "distance":
        self.distance = value
      case _:
        raise ValueError(f"key: {key} is not defined in Point")
