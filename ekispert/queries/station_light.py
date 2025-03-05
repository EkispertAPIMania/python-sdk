from ..base import Base
from ..models.point import Point
from typing import List, Literal

TrafficType = Literal["train", "plane", "ship", "bus", "walk", "strange"]
NameMatchType = Literal["forward", "partial"]

class StationLightQuery(Base):
  base_path: str = '/v1/json/station/light'

  def __init__(self, client):
    super().__init__()
    self.client = client
    self.name : str = None
    self.nameMatchType: NameMatchType = 'partial'
    self.code : int = None
    self.types : List[TrafficType] = None
    self.prefectureCodes : List[int] = None
    self.corporationBinds : List[str] = None
    self.communityBus : str = 'contain'

  def execute(self) -> List[Point]:
    data = self.client.get(self.base_path, self.generate_params())
    result_set = data['ResultSet']
    points = self.get_as_array(result_set['Point'])
    if len(points) == 0:
      return []
    results = []
    for point in points:
      results.append(Point(point))
    return results

  def generate_params(self) -> dict:
    params = {
      'key': self.client.api_key,
    }
    if self.name:
      params['name'] = self.name
    if self.nameMatchType:
      params['nameMatchType'] = self.nameMatchType
    if self.code:
      params['code'] = self.code
    if self.types:
      params['type'] = ':'.join(self.types)
    if self.prefectureCodes:
      params['prefectureCode'] = ':'.join(map(str, self.prefectureCodes))
    if self.corporationBinds:
      params['corporationBind'] = ':'.join(self.corporationBinds)
    if self.communityBus:
      params['communityBus'] = self.communityBus
    return params