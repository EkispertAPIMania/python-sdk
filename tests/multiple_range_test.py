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

class TestMultipleRangeQuery:
  def test_query(self):
    client = Ekispert(os.getenv('API_KEY'))
    query = client.multipleRangeQuery()
    query.base_list = [22828]
    query.upper_minute = [15]
    response = query.execute()
    assert(response['base'].point is not None)
    assert(isinstance(response['base'].point, Point))
    assert(len(response['points']) > 0)
    assert(isinstance(response['points'][0], Point))
    assert(response['points'][0].station.name is not None)
    assert(response['points'][0].prefecture is not None)
    assert(response['points'][0].prefecture.name is not None)
    assert(response['points'][0].prefecture.code is not None)
    