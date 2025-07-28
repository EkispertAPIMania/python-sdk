from ..utils import Utils
from ..models.point import Point
from typing import List, Literal

TrafficType = Literal["train", "plane", "ship", "bus", "walk", "strange"]
Direction = Literal["up", "down", "none"]
Gcs = Literal["tokyo", "wgs84"]

class StationQuery(Utils):
  base_path: str = '/v1/json/station'

  def __init__(self, client):
    super().__init__()
    self.client = client
    self.name : str = None
    self.old_name : str = None
    self.code : int = None
    self.corporation_name : str = None
    self.rail_name : str = None
    self.operation_line_code : str = None
    self.types : List[TrafficType] = None
    self.prefecture_codes : List[int] = None
    self.offset : int = 1
    self.limit : int = 100
    self.direction : Direction = 'up'
    self.corporation_binds : List[str] = None
    self.add_gate_group : bool = False
    self.community_bus : str = 'contain'
    self.gcs : Gcs = 'tokyo'

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
    if self.old_name:
      params['oldName'] = self.old_name
    if self.code:
      params['code'] = self.code
    if self.corporation_name:
      params['corporationName'] = self.corporation_name
    if self.rail_name:
      params['railName'] = self.rail_name
    if self.operation_line_code:
      params['operationLineCode'] = self.operation_line_code
    if self.types:
      params['type'] = ':'.join(self.types)
    if self.prefecture_codes:
      params['prefectureCode'] = ':'.join(map(str, self.prefectureCodes))
    if self.offset:
      params['offset'] = self.offset
    if self.limit:
      params['limit'] = self.limit
    if self.direction:
      params['direction'] = self.direction
    if self.corporation_binds:
      params['corporationBind'] = ':'.join(self.corporation_binds)
    params['addGateGroup'] = self.get_as_boolean_string(self.add_gate_group)
    if self.community_bus:
      params['communityBus'] = self.community_bus
    if self.gcs:
      params['gcs'] = self.gcs
    return params