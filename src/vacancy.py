import re


class Vacancy:
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
        self.pk = pk
        self._name = name
        self._url = url
        self._salary_from = salary_from or 0
        self._salary_to = salary_to or 0
        self._currency = currency
        self._responsibility = responsibility or ''

    def __str__(self):
        lines = [
            f'Название вакансии: {self._name}',
            f'Ссылка на вакансия: {self._url}',
            f'Зарплата от: {self._salary_from}',
            f'Зарплата до: {self._salary_to}',
            f'Валюта: {self._currency}',
            f'Описание вакансий: {self._responsibility}'
        ]
        return '\n'.join(lines)

    def __lt__(self, other):
        return max(self._salary_from, self._salary_to) < max(other._salary_from, other._salary_to)

    def has_words(self, words: list[str]) -> bool:
        for word in words:
            if re.search(word, self._responsibility, flags=re.IGNORECASE):
                return True
        return False

    def to_dict(self):
        return {'pk': self.pk,
                'name': self._name,
                'url': self._url,
                'salary_from': self._salary_from,
                'salary_to': self._salary_to,
                'currency': self._currency,
                'responsibility': self._responsibility,
                }

    @classmethod
    def create_from_dict(cls, data: dict):
        pk = data.get("id")
        name = data.get("name")
        url = data.get("alternate_url")
        salary_dict = data.get("salary") or {}
        salary_from = salary_dict.get("salary_from")
        salary_to = salary_dict.get("salary_to")
        currency = salary_dict.get("currency")
        snippet_dict = data.get("snippet") or {}
        responsibility = snippet_dict.get("responsibility")

        return cls(pk, name, url, salary_from, salary_to, currency, responsibility)

    @classmethod
    def cast_to_object_list(cls, data: list[dict]) -> list['Vacancy']:
        list_vacancy = []
        for vacancy_dict in data:
            list_vacancy.append(cls.create_from_dict(vacancy_dict))

        return list_vacancy


