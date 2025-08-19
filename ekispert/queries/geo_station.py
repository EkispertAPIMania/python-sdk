from datetime import datetime
from ekispert.models.point import Point
from ekispert.models.base import Base
from ..utils import Utils
from typing import List

class GeoStationQuery(Utils):
  base_path: str = '/v1/json/geo/station'

  def __init__(self, client):
    super().__init__()
    self.client = client
    self.geo_point: str = None
    self.type: str = None
    self.corporation_binds: List[str] = None
    self.add_gate_group: bool = False
    self.exclude_same_line_station: bool = False
    self.station_count: int = None
    self.community_bus: str = None
    self.gcs: str = None
  
  def set_geo_point(self, langitude: str, longitude: str, radius: int = None, geodetic = 'tokyo'):
    keyword = f"{langitude},{longitude}"
    if geodetic:
      keyword += f",{geodetic}"
    if radius:
      keyword += f",{radius}"
    self.geo_point = keyword
    return self
  def execute(self) -> dict:
    data = self.client.get(self.base_path, self.generate_params())
    result_set = data['ResultSet']
    points = self.get_as_array(result_set['Point'])
    results = []
    for point in points:
      results.append(Point(point))
    return results

  def generate_params(self) -> dict:
    params = {
      'key': self.client.api_key,
    }
    if not self.geo_point:
      raise ValueError("geo_point is required")
    params['geoPoint'] = self.geo_point
    if self.type:
      params['type'] = self.type
    if self.corporation_binds:
      params['corporationBind'] = ':'.join(map(str, self.corporation_binds))
    if self.add_gate_group:
      params['addGateGroup'] = self.get_as_boolean_string(self.add_gate_group)
    if self.exclude_same_line_station:
      params['excludeSameLineStation'] = self.get_as_boolean_string(self.exclude_same_line_station)
    if self.station_count is not None:
      params['stationCount'] = self.station_count
    if self.community_bus:
      params['communityBus'] = self.community_bus
    if self.gcs:
      params['gcs'] = self.gcs
    return params