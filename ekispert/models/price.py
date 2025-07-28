from ekispert.models.trip_option import TripOption
from ..utils import Utils

from collections import namedtuple

Rate = namedtuple('Rate', 'text area')

class Price(Utils):
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
      case "farerevisionstatus":
        self.fare_revision_status = value
      case "fromlineindex":
        self.from_line_index = int(value)
      case "index":
        self.index = int(value)
      case "kind":
        self.kind = value
      case "nikukanteikiindex":
        self.nikukanteiki_index = int(value)
      case "offpeakteiki":
        self.offpeak_teiki = value
      case "passclassindex":
        self.pass_class_index = int(value)
      case "relationindex":
        self.relation_index = int(value)
      case "selected":
        if value == "true":
          self.selected = True
        else:
          self.selected = False
      case "tolineindex":
        self.to_line_index = int(value)
      case "vehicleindex":
        self.vehicle_index = int(value)
      case "name":
        self.name = value
      case "oneway":
        # if value is string, it is not array
        if isinstance(value, str):
          self.one_way = int(value)
        else:
          self.one_way = TripOption(value)
      case "rate":
        self.rate = Rate(
          text = value["text"],
          area = value["area"]
        )
      case "revisionstatus":
        self.revision_status = value
      case "revisionstatuscomment":
        self.revision_status_comment = value
      case "round":
        if isinstance(value, str):
          self.round = int(value)
        else:
          self.round = TripOption(value)
      case "type":
        self.type = value
      case _:
        raise ValueError(f"key: {key} is not defined in Price")