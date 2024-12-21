import json
from abc import ABC, abstractmethod

from src.vacancy import Vacancy


class Storage(ABC):
    """Базовый класс для взаимодействия с хранилищем"""

    @abstractmethod
    def load(self) -> list[Vacancy]:
        """Загрузить данный из хранилища"""
        pass

    @abstractmethod
    def add_vacancy(self, vacancy: Vacancy) -> None:
        """Добавить данные в хранилище"""
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy: Vacancy) -> None:
        """Удалить данные из хранилища"""
        pass


class JsonStorage(Storage):
    """Класс для взаимодействия с хранилищем в виде JSON файлов"""

    def __init__(self, file_name: str = "data.json"):
        self.__file_name = file_name

    def _save(self, vacancies: list[Vacancy]) -> None:
        """Сохранить список вакансий в json файл"""
        vacancy_dicts = []
        for vacancy in vacancies:
            vacancy_dicts.append(vacancy.to_dict())
        with open(self.__file_name, "w") as f:
            f.write(json.dumps(vacancy_dicts, ensure_ascii=False))

    def load(self) -> list[Vacancy]:
        """Загрузить данный из хранилища"""
        with open(self.__file_name, "r") as f:
            json_vacancies = json.loads(f.read() or "[]")
        vacancies = []
        for vacancy_dict in json_vacancies:
            vacancies.append(Vacancy.from_dict(vacancy_dict))
        return vacancies

    def add_vacancy(self, vacancy) -> None:
        """Добавить данные в хранилище"""
        vacancies = self.load()
        if vacancy in vacancies:
            return
        vacancies.append(vacancy)
        self._save(vacancies)

    def delete_vacancy(self, vacancy):
        """Удалить данные из хранилища"""
        vacancies = self.load()
        for i, vac in enumerate(vacancies):
            if vacancy == vac:
                vacancies.pop(i)
                break
        self._save(vacancies)
