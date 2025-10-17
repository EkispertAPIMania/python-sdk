class Utils:
  def get_as_boolean_string(self, data: bool) -> str:
    if data:
      return 'true'
    else:
      return 'false'

  def get_as_array(self, data) -> list:
    if isinstance(data, list):
      return data
    else:
      return [data]
