from ..utils import Utils
from ..models.point import Point
from typing import List, Literal

TrafficType = Literal["train", "plane", "ship", "bus", "walk", "strange"]
NameMatchType = Literal["forward", "partial"]

class StationLightQuery(Utils):
  base_path: str = '/v1/json/station/light'

  def __init__(self, client):
    super().__init__()
    self.client = client
    self.name : str = None
    self.name_match_type: NameMatchType = 'partial'
    self.code : int = None
    self.types : List[TrafficType] = None
    self.prefecture_codes : List[int] = None
    self.corporation_binds : List[str] = None
    self.community_bus : str = 'contain'

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
    if self.name_match_type:
      params['nameMatchType'] = self.name_match_type
    if self.code:
      params['code'] = self.code
    if self.types:
      params['type'] = ':'.join(self.types)
    if self.prefecture_codes:
      params['prefectureCode'] = ':'.join(map(str, self.prefecture_codes))
    if self.corporation_binds:
      params['corporationBind'] = ':'.join(self.corporation_binds)
    if self.community_bus:
      params['communityBus'] = self.community_bus
    return params