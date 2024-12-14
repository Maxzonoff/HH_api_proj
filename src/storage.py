import json
from abc import ABC, abstractmethod

from src.vacancy import Vacancy


class StorageException(Exception):
    pass


class Storage(ABC):

    @abstractmethod
    def load(self) -> list[Vacancy]:
        pass

    @abstractmethod
    def add_vacancy(self, vacancy: Vacancy) -> None:
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy: Vacancy) -> None:
        pass


class JsonStorage(Storage):

    def __init__(self, file_name: str = "data.json"):
        self._file_name = file_name

    def _save(self, vacancies: list[Vacancy]) -> None:
        """Сохранить список вакансий в json файл"""
        vacancy_dicts = []
        for vacancy in vacancies:
            vacancy_dicts.append(vacancy.to_dict())
        with open(self._file_name, "w") as f:
            f.write(json.dumps(vacancy_dicts, ensure_ascii=False))

    def load(self) -> list[Vacancy]:
        with open(self._file_name, "r") as f:
            json_vacancies = json.loads(f.read() or "[]")
        vacancies = []
        for vacancy_dict in json_vacancies:
            vacancies.append(Vacancy.from_dict(vacancy_dict))
        return vacancies

    def add_vacancy(self, vacancy) -> None:
        vacancies = self.load()
        if vacancy in vacancies:
            return
        vacancies.append(vacancy)
        self._save(vacancies)

    def delete_vacancy(self, vacancy):
        vacancies = self.load()
        for i, vac in enumerate(vacancies):
            if vacancy == vac:
                vacancies.pop(i)
                break
        self._save(vacancies)
