from ..utils import Utils

class TripOption(Utils):
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
      case "fullremark":
        self.full_remark = value
      case "remark":
        self.remark = value
      case "expectedfullremark":
        self.expected_full_remark = value
      case "expectedremark":
        self.expected_remark = value
      case "includedincharge":
        self.included_in_charge = True
      case "rate":
        self.rate = value
      case _:
        raise ValueError(f"key: {key} is not defined in Cost")