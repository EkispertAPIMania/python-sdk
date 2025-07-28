from datetime import datetime

from ekispert.models.repayment_list import RepaymentList
from ekispert.models.teiki_route import TeikiRoute
from ..utils import Utils
from typing import List, Literal

class CourseRepaymentResponse:
  repayment_list: RepaymentList
  teiki_route: TeikiRoute
  def __init__(self, repayment_list: RepaymentList, teiki_route: TeikiRoute):
    self.repayment_list = repayment_list
    self.teiki_route = teiki_route

ValidityPeriod = Literal[1, 3, 6, 12]
class CourseRepaymentQuery(Utils):
  base_path: str = '/v1/json/course/repayment'

  def __init__(self, client):
    super().__init__()
    self.client = client

    self.serialize_data : str = ''
    self.check_engine_version : bool = True
    self.start_date : datetime = datetime.now()
    self.buy_date : datetime = datetime.now()
    self.repayment_date : datetime = datetime.now()
    self.validity_period : ValidityPeriod = 6
    self.change_section : bool = False
    self.separator : List[str] = []

  def execute(self) -> CourseRepaymentResponse:
    data = self.client.get(self.base_path, self.generate_params())
    result_set = data['ResultSet']
    repayment_list = result_set['RepaymentList']
    teiki_route = result_set['TeikiRoute']
    if repayment_list is None and teiki_route is None:
      return CourseRepaymentResponse(
        repayment_list=None,
        teiki_route=None,
      )
    return CourseRepaymentResponse(
      repayment_list=RepaymentList(repayment_list),
      teiki_route=TeikiRoute(teiki_route),
    )

  def generate_params(self) -> dict:
    params = {
      'key': self.client.api_key,
    }
    if self.serialize_data == '':
      raise ValueError('serialize_data is required')
    params['serializeData'] = self.serialize_data
    params['checkEngineVersion'] = self.get_as_boolean_string(self.check_engine_version)
    if self.start_date:
      params['startDate'] = self.start_date.strftime('%Y%m%d')
    if self.buy_date:
      params['buyDate'] = self.buy_date.strftime('%Y%m%d')
    if self.repayment_date:
      params['repaymentDate'] = self.repayment_date.strftime('%Y%m%d')
    if self.validity_period:
      params['validityPeriod'] = self.validity_period
    params['changeSection'] = self.get_as_boolean_string(self.change_section)
    if self.separator is not None:
      params['separator'] = ','.join(self.separator)
    return params
