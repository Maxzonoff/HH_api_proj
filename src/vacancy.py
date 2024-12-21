import re


class Vacancy:
    """Класс для работы с вакансиями"""

    __slots__ = (
        "__pk",
        "__name",
        "__url",
        "__salary_from",
        "__salary_to",
        "__currency",
        "__responsibility",
    )

    def __init__(
        self,
        pk: str,
        name: str,
        url: str,
        salary_from: int | None,
        salary_to: int | None,
        currency: str | None,
        responsibility: str | None,
    ) -> None:
        self.__pk = pk
        self.__name = name
        self.__url = url
        self.__salary_from = self.__validate_salary(salary_from)
        self.__salary_to = self.__validate_salary(salary_to)
        self.__currency = currency
        self.__responsibility = self.__validate_responsibility(responsibility)

    @classmethod
    def __validate_salary(cls, salary: int | None) -> int:
        return salary or 0

    @classmethod
    def __validate_responsibility(cls, responsibility: str | None) -> str:
        return responsibility or ""

    @property
    def pk(self):
        return self.__pk

    def __str__(self):
        lines = [
            f"Название вакансии: {self.__name}",
            f"Ссылка на вакансия: {self.__url}",
            f"Зарплата от: {self.__salary_from}",
            f"Зарплата до: {self.__salary_to}",
            f"Валюта: {self.__currency}",
            f"Описание вакансий: {self.__responsibility}",
        ]
        return "\n".join(lines)

    def __lt__(self, other):
        return max(self.__salary_from, self.__salary_to) < max(
            other.__salary_from, other.__salary_to
        )

    def has_words(self, words: list[str]) -> bool:
        """Проверяет есть ли заданные слова в описании"""
        for word in words:
            if re.search(word, self.__responsibility, flags=re.IGNORECASE):
                return True
        return False

    def to_dict(self):
        """Преобразовывает вакансию в словарь"""
        return {
            "pk": self.__pk,
            "name": self.__name,
            "url": self.__url,
            "salary_from": self.__salary_from,
            "salary_to": self.__salary_to,
            "currency": self.__currency,
            "responsibility": self.__responsibility,
        }

    @classmethod
    def from_dict(cls, data):
        """Создает вакансию из словаря"""
        return cls(
            pk=data["pk"],
            name=data["name"],
            url=data["url"],
            salary_from=data["salary_from"],
            salary_to=data["salary_to"],
            currency=data["currency"],
            responsibility=data["responsibility"],
        )

    @classmethod
    def create_from_dict(cls, data: dict):
        """Создает вакансию из словаря полученного из HH"""
        pk = str(data.get("id"))
        name = str(data.get("name"))
        url = str(data.get("alternate__url"))
        salary_dict = data.get("salary") or {}
        salary_from = salary_dict.get("salary_from")
        salary_to = salary_dict.get("salary_to")
        currency = salary_dict.get("currency")
        snippet_dict = data.get("snippet") or {}
        responsibility = snippet_dict.get("responsibility")

        return cls(pk, name, url, salary_from, salary_to, currency, responsibility)

    @classmethod
    def cast_to_object_list(cls, data: list[dict]) -> list["Vacancy"]:
        """Создает список вакансий из списка словарей HH"""
        list_vacancy = []
        for vacancy_dict in data:
            list_vacancy.append(cls.create_from_dict(vacancy_dict))

        return list_vacancy
