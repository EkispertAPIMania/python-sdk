from datetime import datetime

from ekispert.models.repayment_ticket import RepaymentTicket
from ..utils import Utils

class RepaymentList(Utils):
  def __init__(self, data = None):
    super().__init__()
    if data is None:
      return
    self.sets(data)

  def sets(self, data: dict):
    for key in data:
      self.set(key, data[key])

  def set(self, key: str, value: any):
    match key.lower():
      case "repaymentdate":
        # str to datetime
        if value is not None:
          self.repayment_date = datetime.strptime(value, '%Y-%m-%d')
      case "validityperiod":
        # str to int
        if value is not None:
          self.validity_period = int(value)
      case "startdate":
        # str to datetime
        if value is not None:
          self.start_date = datetime.strptime(value, '%Y-%m-%d')
      case "buydate":
        # str to datetime
        if value is not None:
          self.buy_date = datetime.strptime(value, '%Y-%m-%d')
      case "repaymentticket":
        repayment_tickets = self.get_as_array(value)
        if repayment_tickets is not None and len(repayment_tickets) > 0:
          self.repayment_tickets = []
          for repayment_ticket in repayment_tickets:
            self.repayment_tickets.append(RepaymentTicket(repayment_ticket))
      case _:
        raise ValueError(f"key: {key} is not defined in RepaymentList")
