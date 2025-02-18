from .query import Query
from urllib.parse import urljoin, urlencode
import requests

class Ekispert:
  base_url = 'https://api.ekispert.jp'

  def __init__(self, api_key):
    self.api_key = api_key
    Query.client = self
	
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
