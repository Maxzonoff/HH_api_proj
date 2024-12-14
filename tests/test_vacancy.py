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
    assert res._name == "name"
    assert res._url == "url"
    assert res._salary_from == 10
    assert res._salary_to == 20
    assert res._currency == "rub"
    assert res._responsibility == "qwerty"


# def test_create_from_dict_missing_name_raises_error():
#     data = {}
#     with pytest.raises(vacancy.VacancyCreateException) as e:
#         vacancy.Vacancy.create_from_dict(data)
#     assert str(e.value) == "Отсутствует ключ name"
#
#
# def test_create_from_dict_missing_url_raises_error():
#     data = {"name": "test_name"}
#     with pytest.raises(vacancy.VacancyCreateException) as e:
#         vacancy.Vacancy.create_from_dict(data)
#     assert str(e.value) == "Отсутствует ключ url"
#
#
# def test_create_from_dict_missing_salary_from_raises_error():
#     data = {
#         "name": "test_name",
#         "alternate_url": "test_url",
#     }
#     with pytest.raises(vacancy.VacancyCreateException) as e:
#         vacancy.Vacancy.create_from_dict(data)
#     assert str(e.value) == "Отсутствует ключ salary_from"
#
#
# def test_create_from_dict_missing_salary_to_raises_error():
#     data = {
#         "name": "test_name",
#         "alternate_url": "test_url",
#         "salary_from": "test_salary_from",
#     }
#     with pytest.raises(vacancy.VacancyCreateException) as e:
#         vacancy.Vacancy.create_from_dict(data)
#     assert str(e.value) == "Отсутствует ключ salary_to"
#
#
# def test_create_from_dict_missing_currency_raises_error():
#     data = {
#         "name": "test_name",
#         "alternate_url": "test_url",
#         "salary_from": "test_salary_from",
#         "salary_to": "test_salary_to",
#     }
#     with pytest.raises(vacancy.VacancyCreateException) as e:
#         vacancy.Vacancy.create_from_dict(data)
#     assert str(e.value) == "Отсутствует ключ currency"
#
#
# def test_create_from_dict_missing_responsibility_raises_error():
#     data = {
#         "name": "test_name",
#         "alternate_url": "test_url",
#         "salary_from": "test_salary_from",
#         "salary_to": "test_salary_to",
#         "currency": "test_currency",
#     }
#     with pytest.raises(vacancy.VacancyCreateException) as e:
#         vacancy.Vacancy.create_from_dict(data)
#     assert str(e.value) == "Отсутствует ключ responsibility"
#
#
# def test_has_words():
#     v = vacancy.Vacancy(None, None, None, None, None, "ab bm")
#     assert not v.has_words([])
#     assert not v.has_words(["qwerty", "aba"])
#     assert v.has_words(["ab"])
#     assert v.has_words(["bm"])
#     assert v.has_words(["ab", "bm"])
