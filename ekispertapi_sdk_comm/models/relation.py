from ..utils import Utils

from collections import namedtuple

PriceRelation = namedtuple('PriceRelation', 'kind')

class Relation(Utils):
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
      case "name":
        self.name = value
      case "pricerelation":
        # value is array or not
        value = self.get_as_array(value)
        self.price_relations = []
        for v in value:
          if v is not None:
            self.price_relations.append(PriceRelation(
              kind = v["kind"]
            ))
      case _:
        raise ValueError(f"key: {key} is not defined in Relation")