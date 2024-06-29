
import requests
import json

class GetPrograms:
  
  def get_programs(self):
    headers = {}
    URL = "https://data.cityofnewyork.us/resource/2j8u-wtju.json"

    response = requests.get(URL, headers = headers)
    return response.content

  def program_agencies(self):
        programs_list = []
        programs = json.loads(self.get_programs())
        for program in programs:
            programs_list.append(program["government_agency"])

        return programs_list

#programs = GetPrograms().get_programs()
#print(programs)

programs = GetPrograms()
agencies = programs.program_agencies()

for agency in set(agencies):
    print(agency)