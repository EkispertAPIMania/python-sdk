from ekispert.models.pass_status import PassStatus
from ekispert.models.price import Price
from ekispert.models.relation import Relation
from ekispert.models.route import Route
from ekispert.models.teiki import Teiki
from ..utils import Utils

class Course(Utils):
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
      case "searchtype":
        self.search_type = value
      case "datatype":
        self.data_type = value
      case "serializedata":
        self.serialize_data = value
      case "passstatus":
        # check value is array or not
        value = self.get_as_array(value)
        self.pass_statuses = []
        for v in value:
          if v is not None:
            self.pass_statuses.append(PassStatus(v))
      case "price":
        value = self.get_as_array(value)
        self.prices = []
        for v in value:
          if v is not None:
            self.prices.append(Price(v))
      case "relation":
        # value is array or not
        value = self.get_as_array(value)
        self.relations = []
        for v in value:
          if v is not None:
            self.relations.append(Relation(value))
      case "teiki":
        self.teiki = Teiki(value)
      case "route":
        value = self.get_as_array(value)
        self.routes = []
        for v in value:
          if v is not None:
            self.routes.append(Route(v))
      case _:
        raise ValueError(f"key: {key} is not defined in Course")