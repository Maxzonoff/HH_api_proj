from src import hh_api
import json

api = hh_api.HeadHunterAPI()
api.get_vacancies('Python')
print(json.dumps(api.vacancies[0], indent=2, ensure_ascii=False).encode('utf-8').decode())
