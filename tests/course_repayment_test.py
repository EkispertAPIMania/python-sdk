from datetime import datetime
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

class TestCourseRepaymentQuery:
  def test_query(self):
    client = Ekispert(os.getenv('API_KEY'))
    query = client.courseRepaymentQuery()
    query.separator = ['1', 'true']
    query.check_engine_version = False
    query.serialize_data = 'VkV4QaECp9nIAsMCpgEz76YDpgEz76UEkcIBQwAAAAKmATPvpQPKAQECAQMBBAEHAQgBCgIPQv9_EKX_9xSRpVjVBZfBAqVYj8ECpVjVwQKlWXvBAqVZLMECpVkPwQKlWvHBAqVXwAaSwwEBAgEDxwGlWFoCDQMPBQMGRDk0NlQHBAgDwwEBAgEDxgGmAAIwMwIVAxYFAwcGCAUHksUBpgEz76gDpQJfBKUCZgUACADGAaYBM||oAgEDpQJwBKUCcQUACAAIksQEAQUBB6RtCAHGAgEEAgUBBgEHpQEvCAIJksEDAcMBAQIBAwEPkcUBkwABAgKSwwEAAgADAMMBAQIBAwEDksMBAAIAAwDDAQECAQMBBJIAAQWSAAA*--T3221233232319:F332112212000:A23121141:--88eed71f6168dfe5ab30b8cc5e938621dd3806a7--0--0--0--284'
    results = query.execute()
    assert results.repayment_list is not None
    assert results.teiki_route is not None
    assert results.repayment_list.repayment_date is not None
    assert results.repayment_list.repayment_tickets is not None
    assert results.repayment_list.repayment_tickets[0].fee_price_value is not None
    assert results.repayment_list.repayment_tickets[0].repay_price_value is not None
    assert results.repayment_list.repayment_tickets[0].state is not None
    assert results.repayment_list.repayment_tickets[0].used_price_value is not None
    assert results.repayment_list.repayment_tickets[0].calculate_target is not None
    assert results.teiki_route.section_separator is not None
    assert results.teiki_route.teiki_route_sections is not None
    assert results.teiki_route.teiki_route_sections[0].points is not None
    assert results.teiki_route.teiki_route_sections[0].points[0].station.name is not None
    assert results.teiki_route.teiki_route_sections[0].points[0].prefecture is not None

  def test_demo_query(self):
    client = Ekispert(os.getenv('API_KEY'))
    query = client.coursePlainQuery()
    query.from_ = '高円寺'
    query.to = '東京'
    query.date = datetime.now()
    results = query.execute()
    assert results is not None

    query2 = client.courseRepaymentQuery()
    query2.serialize_data = results[0].serialize_data
    query2.separator = ['1', 'true']
    results2 = query2.execute()
    assert results2 is not None
    assert results2.repayment_list is not None
    assert results2.repayment_list.validity_period == 6
    assert results2.repayment_list.repayment_tickets[0].fee_price_value == 220
    assert results2.teiki_route.teiki_route_sections[0].points[0].prefecture.name == '東京都'
    assert results2.teiki_route.teiki_route_sections[0].points[0].station.name == '高円寺'
    assert results2.teiki_route is not None
