from ..utils import Utils

from collections import namedtuple

Type = namedtuple('Type', 'text detail')

class Station(Utils):
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
      case "code":
        self.code = int(value)
      case "name":
        self.name = value
      case "oldname":
        self.old_name = value
      case "yomi":
        self.yomi = value
      case "type":
        # value is string or not
        if isinstance(value, str):
          self.type = Type(
            text = value,
            detail = None)
        else:
          self.type = Type(
            text = value["text"],
            detail = value["detail"])
      case _:
        raise ValueError(f"key: {key} is not defined in Station")