from src.vacancy import Vacancy


def test_str():
    vac = Vacancy("123", "name", "url", 10, 20, "rub", "qwerty")
    assert (
        str(vac)
        == """Название вакансии: name
Ссылка на вакансия: url
Зарплата от: 10
Зарплата до: 20
Валюта: rub
Описание вакансий: qwerty"""
    )


def test_lt():
    vac_1 = Vacancy("123", "name", "url", 10, 20, "rub", "qwerty")
    vac_2 = Vacancy("123", "name", "url", 20, 30, "rub", "qwerty")
    assert vac_1 < vac_2


def test_to_dict():
    vac = Vacancy("123", "name", "url", 10, 20, "rub", "qwerty")
    assert vac.to_dict() == {
        "pk": "123",
        "name": "name",
        "url": "url",
        "salary_from": 10,
        "salary_to": 20,
        "currency": "rub",
        "responsibility": "qwerty",
    }


def test_create_from_dict():
    data = {
        "id": "123",
        "name": "name",
        "alternate_url": "url",
        "salary": {"salary_from": 10, "salary_to": 20, "currency": "rub"},
        "snippet": {"responsibility": "qwerty"},
    }
    res = Vacancy.create_from_dict(data)
    assert res.pk == "123"
