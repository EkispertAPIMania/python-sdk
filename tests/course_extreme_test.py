from pathlib import Path
import sys
import datetime
sys.path.append(str(Path(__file__).resolve().parent.parent))
from dotenv import load_dotenv
import os
import pytest
from ekispertapi_sdk_comm.client import Ekispert

@pytest.fixture(autouse=True, scope='session')
def load_env():
  load_dotenv()

class TestCourseExtremeQuery:
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
    assert courses[0].routes[0].exhaust_co2 == 98

  def test_query2(self):
    client = Ekispert(os.getenv('API_KEY'))
    query = client.courseExtremeQuery()
    query.via_list.append('八王子')
    query.via_list.append('新宿')
    courses = query.execute()
    assert courses[0].serialize_data is not None
  def test_query3(self):
    client = Ekispert(os.getenv('API_KEY'))
    Ekispert.debug = True
    query = client.courseExtremeQuery()
    query.via_list.append('新宿')
    query.via_list.append('恵比寿')
    query.assign_teiki_serialize_data = "VkV4QaECp_rHAQEDpgEz7osEk8EBpViPwQGlWNXBAaVYuwWSwwEBA6RtBKVY1cQBAQIBA6RxBKVYuweRxQGlWI8CpVi7AwAEAQUACAEKAQ**--2ffa318938ac7a409fec1643d23af692c573ee53--0--79"
    query.check_engine_version = False
    courses = query.execute()
    with_teiki = list(filter(lambda x: hasattr(x, 'type') and x.type == "withTeiki", courses[0].prices))

  def test_query4(self):
    client = Ekispert(os.getenv('API_KEY'))
    query = client.courseExtremeQuery()
    query.add_assign_status = True
    query.search_type = "plain"
    query.via_list.append("長万部")
    query.via_list.append("中ノ沢")
    query.date = datetime.datetime(2024, 3, 1)
    courses = query.execute()
    assert len(courses) > 0, "No courses returned from API"
    assert courses[0].teiki.detail_route is not None

  def test_query4_assign_status(self):
    client = Ekispert(os.getenv('API_KEY'))
    query = client.courseExtremeQuery()
    query.add_assign_status = True
    query.via_list.append("浅草")
    query.via_list.append("とうきょうスカイツリー")
    query.assign_detail_routes.append("浅草")
    query.assign_detail_routes.append("東武伊勢崎線区間準急")
    query.assign_detail_routes.append("Down")
    query.assign_detail_routes.append("業平橋")
    query.date = datetime.datetime(2025, 1, 15, 10, 0, 0)
    courses = query.execute()
    assert len(courses) > 0, "No courses returned from API"
    assert courses[0].assign_status is not None, "assign_status is missing"
    assert isinstance(courses[0].assign_status.require_update, bool), "require_update should be a boolean"
    assert isinstance(courses[0].assign_status.code, int), "code should be an integer"

  def test_query5(self):
    client = Ekispert(os.getenv('API_KEY'))
    Ekispert.debug = True
    query = client.courseExtremeQuery()
    query.via_list.append("高円寺")
    query.via_list.append("渋谷")
    query.search_type = "plain"

    courses = query.execute()
    assert courses[0].teiki.serialize_data is not None
    assert courses[0].teiki.display_route is not None
