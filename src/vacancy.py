class VacancyBaseException(Exception):
    pass


class VacancyCreateException(VacancyBaseException):
    pass


class Vacancy:
    def __init__(
            self,
            name: str,
            url: str,
            salary_from: int | None,
            salary_to: int | None,
            currency: str | None,
            responsibility: str | None,
    ) -> None:
        self._name = name
        self._url = url
        self._salary_from = salary_from
        self._salary_to = salary_to
        self._currency = currency
        self._responsibility = responsibility

    @classmethod
    def create_from_dict(cls, data: dict):
        try:
            name = data['name']
        except KeyError:
            raise VacancyCreateException('Отсутствует ключ name')

        try:
            url = data['alternate_url']
        except KeyError:
            raise VacancyCreateException('Отсутствует ключ url')

        try:
            salary_from = data['salary_from']
        except KeyError:
            raise VacancyCreateException('Отсутствует ключ salary_from')

        try:
            salary_to = data['salary_to']
        except KeyError:
            raise VacancyCreateException('Отсутствует ключ salary_to')

        try:
            currency = data['currency']
        except KeyError:
            raise VacancyCreateException('Отсутствует ключ currency')

        try:
            responsibility = data['responsibility']
        except KeyError:
            raise VacancyCreateException('Отсутствует ключ responsibility')

        return cls(name)
