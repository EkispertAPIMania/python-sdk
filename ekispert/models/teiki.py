from ..utils import Utils

class Teiki(Utils):
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
      case "serializedata":
        self.serialize_data = value
      case "detailroute":
        self.detail_route = value
      case "displayroute":
        self.display_route = value
      case _:
        raise ValueError(f"key: {key} is not defined in Cost")
