from datetime import datetime
from ekispert.models.cource import Course
from ..utils import Utils
from typing import List, Literal

Gcs = Literal["tokyo", "wgs84"]
SearchType = Literal["departure", "arrival", "lastTrain", "firstTrain", "plain"]
Sort = Literal["ekispert", "price", "time", "teiki", "transfer", "co2", "teiki1", "teiki3", "teiki6"]
OffpeakTeikiMode = Literal["offpeakTime", "peakTime"]

class CourseExtremeQuery(Utils):
  base_path: str = '/v1/json/search/course/extreme'

  def __init__(self, client):
    super().__init__()
    self.client = client
    self.via_list : List[str] = []
    self.exclude_same_line_station : bool = False
    self.fixed_rail_list : List[str] = []
    self.fixed_rail_direction_list : List[str] = []
    self.date : datetime = datetime.today()
    self.time : datetime = datetime.now()
    self.search_type : SearchType = 'departure'
    self.sort : Sort = 'ekispert'
    self.answer_count : int = 5
    self.search_count : int = 5
    self.condition_detail : List[str] = ['T32212332323191', 'F332112212000010', 'A23121141']
    self.corporation_bind : List[str] = []
    self.interrupt_corporation_list : List[str] = []
    self.interrupt_rail_list : List[str] = []
    self.interrupt_operation_line_code_list : List[str] = []
    self.interrupt_transfer_station_code_list : List[str] = []
    self.result_detail : str = None
    self.add_operation_line_pattern : bool = False
    self.check_engine_version : bool = True
    self.assign_teiki_serialize_data : str = None
    self.assign_route : List[str] = []
    self.assign_detail_route : List[str] = []
    self.offpeak_teiki_mode : OffpeakTeikiMode = None
    self.assign_pass_class_index : int = None
    self.coupon : str = None
    self.bring_assignment_error : bool = None
    self.add_assign_status : bool = None
    self.add_change : bool = None
    self.add_stop : bool = None
    self.add_seat_type : bool = None
    self.gcs : Gcs = 'tokyo'

  def execute(self) -> List[Course]:
    data = self.client.get(self.base_path, self.generate_params())
    result_set = data['ResultSet']
    courses = self.get_as_array(result_set['Course'])
    if len(courses) == 0:
      return []
    results = []
    for course in courses:
      results.append(Course(course))
    return results

  def generate_params(self) -> dict:
    params = {
      'key': self.client.api_key,
    }
    if len(self.via_list) > 0:
      params['viaList'] = ':'.join(self.via_list)
    if self.exclude_same_line_station is not None:
      params['excludeSameLineStation'] = self.get_as_boolean_string(self.exclude_same_line_station)
    if len(self.fixed_rail_list) > 0:
      params['fixedRailList'] = ':'.join(self.fixed_rail_list)
    if len(self.fixed_rail_direction_list) > 0:
      params['fixedRailDirectionList'] = ':'.join(self.fixed_rail_direction_list)
    if self.date is not None: 
      params['date'] = self.date.strftime('%Y%m%d')
    if self.time is not None:
      params['time'] = self.time.strftime('%H%M')
    if self.search_type is not None:
      params['searchType'] = self.search_type
    if self.sort is not None:
      params['sort'] = self.sort
    if self.answer_count is not None:
      params['answerCount'] = self.answer_count
    if self.search_count is not None:
      params['searchCount'] = self.search_count
    if len(self.condition_detail) > 0:
      params['conditionDetail'] = ':'.join(self.condition_detail)
    if len(self.corporation_bind) > 0:
      params['corporationBind'] = ':'.join(self.corporation_bind)
    if len(self.interrupt_corporation_list) > 0:
      params['interruptCorporationList'] = ':'.join(self.interrupt_corporation_list)
    if len(self.interrupt_rail_list) > 0:
      params['interruptRailList'] = ':'.join(self.interrupt_rail_list)
    if len(self.interrupt_operation_line_code_list) > 0:
      params['interruptOperationLineCodeList'] = ':'.join(self.interrupt_operation_line_code_list)
    if len(self.interrupt_transfer_station_code_list) > 0:
      params['interruptTransferStationCodeList'] = ':'.join(self.interrupt_transfer_station_code_list)
    if self.result_detail is not None:
      params['resultDetail'] = self.result_detail
    if self.add_operation_line_pattern is not None:
      params['addOperationLinePattern'] = self.get_as_boolean_string(self.add_operation_line_pattern)
    if self.check_engine_version is not None:
      params['checkEngineVersion'] = self.get_as_boolean_string(self.check_engine_version)
    if self.assign_teiki_serialize_data is not None:
      params['assignTeikiSerializeData'] = self.assign_teiki_serialize_data
    if len(self.assign_route) > 0:
      params['assignRoute'] = ':'.join(self.assign_route)
    if len(self.assign_detail_route) > 0:
      params['assignDetailRoute'] = ':'.join(self.assign_detail_route)
    if self.offpeak_teiki_mode is not None:
      params['offpeakTeikiMode'] = self.offpeak_teiki_mode
    if self.assign_pass_class_index is not None:
      params['assignPassClassIndex'] = self.assign_pass_class_index
    if self.coupon is not None:
      params['coupon'] = self.coupon
    if self.bring_assignment_error is not None:
      params['bringAssignmentError'] = self.get_as_boolean_string(self.bring_assignment_error)
    if self.add_assign_status is not None:
      params['addAssignStatus'] = self.get_as_boolean_string(self.add_assign_status)
    if self.add_change is not None:
      params['addChange'] = self.get_as_boolean_string(self.add_change)
    if self.add_stop is not None:
      params['addStop'] = self.get_as_boolean_string(self.add_stop)
    if self.add_seat_type is not None:
      params['addSeatType'] = self.get_as_boolean_string(self.add_seat_type)
    if self.gcs is not None:
      params['gcs'] = self.gcs
    return params