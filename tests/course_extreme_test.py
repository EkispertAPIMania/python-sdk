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

class TestCoursePlainQuery:
  def test_query(self):
    client = Ekispert(os.getenv('API_KEY'))
    query = client.courseExtremeQuery()
    query.via_list = ['22671', '22741']
    query.answer_count = 1
    courses = query.execute()
    assert len(courses) == 1
    assert courses[0].serialize_data is not None
    assert courses[0].teiki.serialize_data is not None
    assert courses[0].routes[0].lines[0].train_id is not None
    assert courses[0].pass_statuses[0].name is not None
    assert courses[0].pass_statuses[0].kind is not None
    assert courses[0].prices[0].kind == "ChargeSummary"
    assert courses[0].routes[0].distance == 58
    assert courses[0].routes[0].exhaust_co2 == 116