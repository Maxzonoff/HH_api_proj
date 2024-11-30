import abc

import requests


class HeadHunterAPIBase(abc.ABC):
    @abc.abstractmethod
    def get_vacancies(self, keyword):
        pass


class HeadHunterAPI(HeadHunterAPIBase):
    def __init__(self):
        self.url = "https://api.hh.ru/vacancies"
        self.headers = {"User-Agent": "HH-User-Agent"}
        self.params = {"text": "", "page": 0, "per_page": 100}
        self.vacancies = []

    def get_vacancies(self, keyword):
        """Получение вакансии с hh.ru"""
        # https://api.hh.ru/openapi/redoc#tag/Poisk-vakansij/operation/get-vacancies
        self.params["text"] = keyword
        while self.params.get("page") != 20:
            response = requests.get(self.url, headers=self.headers, params=self.params)
            vacancies = response.json()["items"]
            self.vacancies.extend(vacancies)
            self.params["page"] += 1
