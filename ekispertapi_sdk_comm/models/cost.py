from ..utils import Utils

class Cost(Utils):
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
      case "minute":
        self.minute = int(value)
      case "transfercount":
        self.transfer_count = int(value)
      case "baseindex":
        self.base_index = int(value)
      case _:
        raise ValueError(f"key: {key} is not defined in Cost")