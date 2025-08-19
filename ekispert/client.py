from urllib.parse import urljoin, urlencode

from ekispert.queries.course_repayment import CourseRepaymentQuery
from ekispert.queries.course_plain import CoursePlainQuery
from .queries.station import StationQuery
from .queries.station_light import StationLightQuery
from .queries.course_extreme import CourseExtremeQuery
from .queries.multiple_range import MultipleRangeQuery
from .queries.geo_station import GeoStationQuery
from ekispert.queries.multiple_range import MultipleRangeQuery
import requests

class Ekispert:
  base_url = 'https://api.ekispert.jp'
  debug = False

  def __init__(self, api_key):
    self.api_key = api_key
	
  def get(self, path, params):
    # requst to Ekispert API
    full_url = urljoin(self.base_url, path)
    # クエリパラメータをエンコード
    query_string = urlencode(params)
    # クエリパラメータを含む完全なURLを作成
    full_url_with_params = f"{full_url}?{query_string}"
    # print(full_url_with_params)
    headers = {'Accept': 'application/json'}
    if Ekispert.debug:
      print(full_url_with_params)
    response = requests.get(full_url_with_params, headers=headers)
    if response.status_code == 200:
      try:
        data = response.json()  # JSONレスポンスを辞書型に変換
        return data
      except ValueError:
        print("Response content is not valid JSON")
    else:
      print(f"Request failed with status code {response.text}")

  def stationQuery(self) -> StationQuery:
    return StationQuery(self)

  def stationLightQuery(self) -> StationLightQuery:
    return StationLightQuery(self)

  def coursePlainQuery(self) -> CoursePlainQuery:
    return CoursePlainQuery(self)

  def courseRepaymentQuery(self) -> CourseRepaymentQuery:
    return CourseRepaymentQuery(self)

  def courseExtremeQuery(self) -> CourseExtremeQuery:
    return CourseExtremeQuery(self)

  def multipleRangeQuery(self) -> MultipleRangeQuery:
    return MultipleRangeQuery(self)
  
  def geoStationQuery(self) -> GeoStationQuery:
    return GeoStationQuery(self)
