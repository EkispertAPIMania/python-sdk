from .formation import Formation
from ..utils import Utils

class AssignStatus(Utils):
  def __init__(self, data = None):
    super().__init__()
    # Initialize attributes with default values
    self.code = None
    self.kind = None
    self.require_update = False
    if data is None:
      return
    self.sets(data)

  def sets(self, data: dict):
    for key in data:
      self.set(key, data[key])

  def set(self, key: str, value: any):
    match key.lower():
      case "code":
        try:
          if value is None:
            raise ValueError("Code value cannot be None")
          self.code = int(value)
        except (ValueError, TypeError) as e:
          raise ValueError(f"Invalid code value '{value}': expected integer or numeric string") from e
      case "kind":
        self.kind = value
      case "requireupdate":
        self.require_update = value == "1"
      case _:
        raise ValueError(f"key: {key} is not defined in AssignStatus")
