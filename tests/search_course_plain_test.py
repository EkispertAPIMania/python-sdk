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

class TestSearchCoursePlainQuery:
  def test_query(self):
    client = Ekispert(os.getenv('API_KEY'))
    query = client.searchCoursePlainQuery()
    query.from_ = 25077
    query.to = 29090
    courses = query.execute()
    assert len(courses) > 0
    assert courses[0].routes[0] is not None
    assert courses[0].prices[0].kind == "ChargeSummary"
    assert courses[0].prices[0].one_way == 2530
    assert courses[0].prices[0].round == 5060
    assert courses[0].routes[0].lines is not None
    assert courses[0].search_type == 'plain'
    assert courses[0].prices[1].kind == "Charge"
    assert courses[0].prices[1].type == "Reserved"
    assert courses[0].prices[1].one_way == 3270
    assert courses[0].teiki is not None
    assert courses[0].teiki.display_route == "名古屋--ＪＲ東海道新幹線--新大阪--OsakaMetro御堂筋線--なんば(地下鉄)"
    assert courses[0].routes[0].time_other == 17
    assert courses[0].routes[0].time_on_board == 64
    assert courses[0].routes[0].exhaust_co2 == 3884
    assert courses[0].routes[0].lines[0].direction == "Down"
    assert courses[0].routes[0].lines[0].color == "051102255"
    assert courses[0].routes[0].points[0].station.name == "名古屋"
    assert courses[0].routes[0].points[1].station.name == "新大阪"
