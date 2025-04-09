from datetime import datetime

from ekispert.models.repayment_list import RepaymentList
from ekispert.models.teiki_route import TeikiRoute
from ..base import Base
from ..models.point import Point
from typing import List, Literal

ValidityPeriod = Literal[1, 3, 6, 12]
class CourseRepaymentQuery(Base):
  base_path: str = '/v1/json/course/repayment'

  def __init__(self, client):
    super().__init__()
    self.client = client

    self.serializeData : str = ''
    self.checkEngineVersion : bool = True
    self.startDate : datetime = datetime.now()
    self.buyDate : datetime = datetime.now()
    self.repaymentDate : datetime = datetime.now()
    self.validityPeriod : ValidityPeriod = 6
    self.changeSection : bool = False
    self.separator : str = ''

  def execute(self) -> List[Point]:
    data = self.client.get(self.base_path, self.generate_params())
    result_set = data['ResultSet']
    repayment_list = result_set['RepaymentList']
    teiki_route = result_set['TeikiRoute']
    if repayment_list is None and teiki_route is None:
      return {
        'repayment_list': None,
        'teiki_route': None,
      }
    return {
      'repayment_list': RepaymentList(repayment_list),
      'teiki_route': TeikiRoute(teiki_route),
    }

  def generate_params(self) -> dict:
    params = {
      'key': self.client.api_key,
    }
    if self.serializeData == '':
      raise ValueError('serializeData is required')
    params['serializeData'] = self.serializeData
    params['checkEngineVersion'] = self.get_as_boolean_string(self.checkEngineVersion)
    if self.startDate:
      params['startDate'] = self.startDate.strftime('%Y%m%d')
    if self.buyDate:
      params['buyDate'] = self.buyDate.strftime('%Y%m%d')
    if self.repaymentDate:
      params['repaymentDate'] = self.repaymentDate.strftime('%Y%m%d')
    if self.validityPeriod:
      params['validityPeriod'] = self.validityPeriod
    params['changeSection'] = self.get_as_boolean_string(self.changeSection)
    if self.separator:
      params['separator'] = self.separator
    return params
