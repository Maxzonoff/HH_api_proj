import responses

from src.hh_api import HeadHunterAPI


@responses.activate
def test_get_vacancies():
    data = [
        {
            "id": "123",
            "name": "name",
            "alternate_url": "url",
            "salary": {"salary_from": 10, "salary_to": 20, "currency": "rub"},
            "snippet": {"responsibility": "qwerty"},
        },
        {
            "id": "321",
            "name": "name",
            "alternate_url": "url",
            "salary": {"salary_from": 10, "salary_to": 20, "currency": "rub"},
            "snippet": {"responsibility": "qwerty"},
        },
        {
            "id": "111",
            "name": "name",
            "alternate_url": "url",
            "salary": {"salary_from": 10, "salary_to": 20, "currency": "rub"},
            "snippet": {"responsibility": "qwerty"},
        },
    ]
    responses.get("https://api.hh.ru/vacancies", json={"items": data})
    hh = HeadHunterAPI()
    hh.get_vacancies("Python")
    assert len(hh.vacancies) == 60
