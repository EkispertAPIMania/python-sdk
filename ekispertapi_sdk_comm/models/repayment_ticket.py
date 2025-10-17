from ..utils import Utils

class RepaymentTicket(Utils):
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
      case "feepricevalue":
        if value is not None:
          self.fee_price_value = int(value)
      case "repaypricevalue":
        if value is not None:
          self.repay_price_value = int(value)
      case "state":
        if value is not None:
          self.state = int(value)
      case "usedpricevalue":
        if value is not None:
          self.used_price_value = int(value)
      case "calculatetarget":
        if value is not None:
          self.calculate_target = bool(value)
      case "toteikiroutesectionindex":
        if value is not None:
          self.to_teiki_route_section_index = int(value)
      case "fromteikiroutesectionindex":
        if value is not None:
          self.from_teiki_route_section_index = int(value)
      case "validityperiod":
        if value is not None:
          self.validity_period = int(value)
      case "paypricevalue":
        if value is not None:
          self.pay_price_value = int(value)
      case "changeablesection":
        if value is not None:
          self.changeable_section = bool(value)
      case _:
        raise ValueError(f"key: {key} is not defined in RepaymentTicket")
