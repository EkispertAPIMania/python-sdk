from datetime import datetime
from ekispert.models.point import Point
from ekispert.models.base import Base
from ..utils import Utils
from typing import List

class MultipleRangeQuery(Utils):
  base_path: str = '/v1/json/search/multipleRange'

  def __init__(self, client):
    super().__init__()
    self.client = client
    self.base_list: List[str] = []
    self.upper_minute: List[int] = []
    self.upper_transfer_count: List[int] = []
    self.plane: bool = True
    self.shinkansen: bool = True
    self.limited_express: bool = True
    self.wait_average_time: bool = True
    self.include_base_station: bool = False
    self.limit: int = 0
    self.date: datetime = datetime.today()

  def execute(self) -> dict:
    data = self.client.get(self.base_path, self.generate_params())
    result_set = data['ResultSet']
    base = Base(result_set['Base'])
    points = self.get_as_array(result_set['Point'])
    results = {
      'base': base,
      'points': []
    }
    for point in points:
      results['points'].append(Point(point))
    return results

  def generate_params(self) -> dict:
    params = {
      'key': self.client.api_key,
    }
    if not self.base_list or len(self.base_list) == 0:
      raise ValueError("base_list is required")
    params['baseList'] = ':'.join(map(str, self.base_list))
    if not self.upper_minute or len(self.upper_minute) == 0:
      raise ValueError("upper_minute is required")
    params['upperMinute'] = ':'.join(map(str, self.upper_minute))
    if len(self.upper_transfer_count) > 0:
      params['upperTransferCount'] = ':'.join(map(str, self.upper_transfer_count))
    params['plane'] = self.get_as_boolean_string(self.plane)
    params['shinkansen'] = self.get_as_boolean_string(self.shinkansen)
    params['limitedExpress'] = self.get_as_boolean_string(self.limited_express)
    params['waitAverageTime'] = self.get_as_boolean_string(self.wait_average_time)
    params['includeBaseStation'] = self.get_as_boolean_string(self.include_base_station)
    if self.limit > 0:
      params['limit'] = self.limit
    if self.date:
      params['date'] = self.date.strftime('%Y%m%d')
    return params