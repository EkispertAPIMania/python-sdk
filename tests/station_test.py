from pathlib import Path
import sys
sys.path.append(str(Path(__file__).resolve().parent.parent))
from dotenv import load_dotenv
import os
import pytest
from ekispert.client import Ekispert
from ekispert.queries.station import StationQuery

@pytest.fixture(autouse=True, scope='session')
def load_env():
  load_dotenv()
  Ekispert(os.getenv('API_KEY'))

class TestStationQuery:
  def test_query(self):
    query = StationQuery()
    points = query.execute()
    assert len(points) > 0
    assert points[0].station.name is not None
    assert points[0].geo_point is not None
    assert points[0].prefecture is not None

  def test_query(self):
    query = StationQuery()
    query.code = 22828
    points = query.execute()
    assert len(points) == 1
    assert points[0].station.name == '東京'
    assert points[0].geo_point.lati_d == 35.678083
    assert points[0].prefecture.name == '東京都'
    assert points[0].prefecture.code == 13

