from ekispert.models.section_separator import SectionSeparator
from ekispert.models.teiki_route_section import TeikiRouteSection
from ..utils import Utils

class TeikiRoute(Utils):
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
      case "sectionseparator":
        self.section_separator = SectionSeparator(value)
      case "teikiroutesection":
        teiki_route_sections = self.get_as_array(value)
        if teiki_route_sections is not None and len(teiki_route_sections) > 0:
          self.teiki_route_sections = []
          for teiki_route_section in teiki_route_sections:
            self.teiki_route_sections.append(TeikiRouteSection(teiki_route_section))
      case _:
        raise ValueError(f"key: {key} is not defined in TeikiRoute")
