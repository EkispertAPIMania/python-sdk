from ekispert.models.point import Point
from ..utils import Utils

class TeikiRouteSection(Utils):
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
      case "repaymentticketindex":
        if value is not None:
          self.repayment_ticket_index = int(value)
      case "point":
        points = self.get_as_array(value)
        if points is not None and len(points) > 0:
          self.points = []
          for point in points:
            self.points.append(Point(point))
      case _:
        raise ValueError(f"key: {key} is not defined in TeikiRouteSection")
