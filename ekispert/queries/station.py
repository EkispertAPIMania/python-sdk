from ..base import Base
from ..models.point import Point
from typing import List, Literal

TrafficType = Literal["train", "plane", "ship", "bus", "walk", "strange"]
Direction = Literal["up", "down", "none"]
Gcs = Literal["tokyo", "wgs84"]

class StationQuery(Base):
  base_path: str = '/v1/json/station'

  def __init__(self, client):
    super().__init__()
    self.client = client
    self.name : str = None
    self.oldName : str = None
    self.code : int = None
    self.corporationName : str = None
    self.railName : str = None
    self.operationLineCode : str = None
    self.types : List[TrafficType] = None
    self.prefectureCodes : List[int] = None
    self.offset : int = 1
    self.limit : int = 100
    self.direction : Direction = 'up'
    self.corporationBinds : List[str] = None
    self.addGateGroup : bool = False
    self.communityBus : str = 'contain'
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
    if self.oldName:
      params['oldName'] = self.oldName
    if self.code:
      params['code'] = self.code
    if self.corporationName:
      params['corporationName'] = self.corporationName
    if self.railName:
      params['railName'] = self.railName
    if self.operationLineCode:
      params['operationLineCode'] = self.operationLineCode
    if self.types:
      params['type'] = ':'.join(self.types)
    if self.prefectureCodes:
      params['prefectureCode'] = ':'.join(map(str, self.prefectureCodes))
    if self.offset:
      params['offset'] = self.offset
    if self.limit:
      params['limit'] = self.limit
    if self.direction:
      params['direction'] = self.direction
    if self.corporationBinds:
      params['corporationBind'] = ':'.join(self.corporationBinds)
    params['addGateGroup'] = self.get_as_boolean_string(self.addGateGroup)
    if self.communityBus:
      params['communityBus'] = self.communityBus
    if self.gcs:
      params['gcs'] = self.gcs
    return params