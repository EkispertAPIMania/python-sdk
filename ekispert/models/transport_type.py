from ..model import Model

class TransportType(Model):
  def __init__(self, data = None):
    super().__init__()
    if data is None:
      return
    self.sets(data)

  def sets(self, data):
    for key in data:
      self.set(key, data[key])

  def set(self, key: str, value: any):
    match key.lower():
      case "text":
        self.text = value
      case "detail":
        self.detail = value
      case _:
        raise ValueError(f"key: {key} is not defined in TransportType")
