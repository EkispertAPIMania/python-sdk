from datetime import datetime
from ekispert.models.cource import Course
from ..utils import Utils
from typing import List, Literal

Gcs = Literal["tokyo", "wgs84"]

class CoursePlainQuery(Utils):
  base_path: str = '/v1/json/search/course/plain'

  def __init__(self, client):
    super().__init__()
    self.client = client
    self.from_ : str | int = None
    self.to : str | int = None
    self.via : str | int = None
    self.date : datetime = datetime.today()
    self.plane : bool = True
    self.shinkansen : bool = True
    self.limited_express : bool = True
    self.bus : bool = True
    self.gcs : Gcs = 'tokyo'

  def execute(self) -> List[Course]:
    data = self.client.get(self.base_path, self.generate_params())
    result_set = data['ResultSet']
    courses = self.get_as_array(result_set['Course'])
    if len(courses) == 0:
      return []
    results = []
    for course in courses:
      results.append(Course(course))
    return results

  def generate_params(self) -> dict:
    params = {
      'key': self.client.api_key,
    }
    if self.from_ is None:
      raise ValueError("from is required")
    params['from'] = self.from_
    
    if self.to is None:
      raise ValueError("to is required")
    params['to'] = self.to
    if self.via:
      params['via'] = self.via
    if self.date:
      params['date'] = self.date.strftime('%Y%m%d')
    if self.gcs:
      params['gcs'] = self.gcs
    params['plane'] = self.get_as_boolean_string(self.plane)
    params['shinkansen'] = self.get_as_boolean_string(self.shinkansen)
    params['limitedExpress'] = self.get_as_boolean_string(self.limited_express)
    params['bus'] = self.get_as_boolean_string(self.bus)
    params['gcs'] = self.gcs
    return params