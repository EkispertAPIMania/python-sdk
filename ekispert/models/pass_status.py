from ..utils import Utils

class PassStatus(Utils):
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
      case "kind":
        self.kind = value
      case "selected":
        if value == "true":
          self.selected = True
        else:
          self.selected = False
      case "fromlineindex":
        self.from_line_index = int(value)
      case "tolineindex":
        self.to_line_index = int(value)
      case "teiki1index":
        self.teiki1_index = int(value)
      case "teiki3index":
        self.teiki3_index = int(value)
      case "teiki6index":
        self.teiki6_index = int(value)
      case "teiki12index":
        self.teiki12_index = int(value)
      case "comment":
        self.comment = value
      case "name":
        self.name = value
      case "type":
        self.type = value
      case _:
        raise ValueError(f"key: {key} is not defined in PassStatus")