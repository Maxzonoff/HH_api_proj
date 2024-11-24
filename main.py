from src import hh_api

api = hh_api.HeadHunterAPI()
api.get_vacancies('Python')
print(api.vacancies)