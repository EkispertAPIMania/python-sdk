from ..utils import Utils

class GeoPoint(Utils):
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
      case "gcs":
        self.gcs = value
      case "lati_d":
        self.lati_d = float(value)
      case "longi_d":
        self.longi_d = float(value)
      case "lati":
        self.lati = value
      case "longi":
        self.longi = value
      case _:
        raise ValueError(f"key: {key} is not defined in GeoPoint")
