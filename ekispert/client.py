from urllib.parse import urljoin, urlencode

from ekispert.queries.search_course_plain import SearchCoursePlainQuery
from .queries.station import StationQuery
from .queries.station_light import StationLightQuery
import requests

class Ekispert:
  base_url = 'https://api.ekispert.jp'

  def __init__(self, api_key):
    self.api_key = api_key
	
  def get(self, path, params):
    # requst to Ekispert API
    full_url = urljoin(self.base_url, path)
    # クエリパラメータをエンコード
    query_string = urlencode(params)
    # クエリパラメータを含む完全なURLを作成
    full_url_with_params = f"{full_url}?{query_string}"
    headers = {'Accept': 'application/json'}
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

  def searchCoursePlainQuery(self) -> SearchCoursePlainQuery:
    return SearchCoursePlainQuery(self)