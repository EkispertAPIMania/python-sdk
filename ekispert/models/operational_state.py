from ekispert.models.geo_point import GeoPoint
from ..utils import Utils
from collections import namedtuple

DateTime = namedtuple('DateTime', 'operation')
Gate = namedtuple('Gate', 'geo_point name')
class OperationalState(Utils):
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
      case "no":
        self.no = value
      case "datetime":
        if value["operation"] is not None:
          self.datetime = DateTime(
            operation = value["operation"])
      case "gate":
        self.gate = Gate(
          geo_point = GeoPoint(value["GeoPoint"]),
          name = value["Name"])
      case "type":
        self.type = value
      case "isstarting":
        self.is_starting = value
      case _:
        raise ValueError(f"key: {key} is not defined in ArrivalState")
