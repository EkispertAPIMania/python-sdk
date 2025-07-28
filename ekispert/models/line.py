from ekispert.models.change import Change
from ekispert.models.operational_state import OperationalState
from ekispert.models.stop import Stop
from ..utils import Utils

from collections import namedtuple

Comment = namedtuple('Comment', 'type')
LineSymbol = namedtuple('LineSymbol', 'code name')
Type = namedtuple('Type', 'text detail')
class Line(Utils):
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
      case "chargeindex":
        self.charge_index = value
      case "direction":
        self.direction = value
      case "distance":
        self.distance = int(value)
      case "exhaustco2":
        self.exhaust_co2 = int(value)
      case "exhaustco2atpassengercar":
        self.exhaust_co2_at_passenger_car = int(value)
      case "fareindex":
        self.fare_index = value
      case "stopstationcount":
        self.stop_station_count = int(value)
      case "teiki1index":
        self.teiki1_index = value
      case "teiki3index":
        self.teiki3_index = value
      case "teiki6index":
        self.teiki6_index = value
      case "teiki12index":
        self.teiki12_index = value
      case "timeonboard":
        self.time_on_board = int(value)
      case "track":
        self.track = value
      case "cars":
        self.cars = int(value)
      case "arrivalstate":
        self.arrival_state = OperationalState(value)
      case "departurestate":
        self.departure_state = OperationalState(value)
      case "change":
        self.change = Change(value)
      case "color":
        self.color = value
      case "comment":
        self.comment = Comment(
          type = value["type"])
      case "destination":
        self.destination = value
      case "linesymbol":
        self.line_symbol = LineSymbol(
          code = value["code"],
          name = value["Name"])
      case "name":
        self.name = value
      case "number":
        self.number = value
      case "timereliability":
        self.time_reliability = value
      case "type":
        if isinstance(value, str):
          self.type = Type(
            text = value,
            detail = None)
        else:
          self.type = Type(
            text = value["text"],
            detail = value["detail"])
      case "typicalname":
        self.typical_name = value
      case "stop":
        self.stop = Stop(value)
      case "trainid":
        self.train_id = value
      case _:
        raise ValueError(f"key: {key} is not defined in Line")

