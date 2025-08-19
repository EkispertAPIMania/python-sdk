from pathlib import Path
import sys
sys.path.append(str(Path(__file__).resolve().parent.parent))
from dotenv import load_dotenv
import os
import pytest
from ekispert.client import Ekispert
from ekispert.models.point import Point

@pytest.fixture(autouse=True, scope='session')
def load_env():
  load_dotenv()

class TestGeoStationQuery:
  def test_query(self):
    client = Ekispert(os.getenv('API_KEY'))
    query = client.geoStationQuery()
    query.set_geo_point(langitude="35.6783055555556", longitude="139.770441666667", radius=1000, geodetic='tokyo')
    points = query.execute()
    assert(len(points) > 0)
    assert(isinstance(points[0], Point))
    assert(points[0].station.name is not None)
    assert(points[0].prefecture is not None)
    assert(points[0].prefecture.name is not None)
    assert(points[0].prefecture.code is not None)
    print(points[0].distance)

    print(points[0].station.name)
    print(points[0].prefecture)
    print(points[0].prefecture.name)
    print(points[0].prefecture.code)
