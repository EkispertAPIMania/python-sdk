class Query:
  client = None
  def get_as_array(self, data) -> list:
    if isinstance(data, list):
      return data
    else:
      return [data]
