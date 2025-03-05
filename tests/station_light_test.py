from pathlib import Path
import sys
sys.path.append(str(Path(__file__).resolve().parent.parent))
from dotenv import load_dotenv
import os
import pytest
from ekispert.client import Ekispert

@pytest.fixture(autouse=True, scope='session')
def load_env():
  load_dotenv()

class TestStationLightQuery:
  def test_query(self):
    client = Ekispert(os.getenv('API_KEY'))
    query = client.stationLightQuery()
    points = query.execute()
    assert len(points) > 0
    assert points[0].station.name is not None
    assert points[0].prefecture is not None

  def test_query_tokyo(self):
    client = Ekispert(os.getenv('API_KEY'))
    query = client.stationLightQuery()
    query.name = '東京'
    points = query.execute()
    assert len(points) > 0
    assert points[0].station.name == '東京'
    assert points[0].prefecture.name == '東京都'
    assert points[0].prefecture.code == 13

