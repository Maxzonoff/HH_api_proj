import pytest
from src import vacancy


def test_create_from_dict_missing_name_raises_error():
    data = {}
    with pytest.raises(vacancy.VacancyCreateException) as e:
        vacancy.Vacancy.create_from_dict(data)
    assert str(e.value) == 'Отсутствует ключ name'


def test_create_from_dict_missing_url_raises_error():
    data = {'name': 'test_name'}
    with pytest.raises(vacancy.VacancyCreateException) as e:
        vacancy.Vacancy.create_from_dict(data)
    assert str(e.value) == 'Отсутствует ключ url'


def test_create_from_dict_missing_salary_from_raises_error():
    data = {'name': 'test_name',
            'alternate_url': 'test_url',
            }
    with pytest.raises(vacancy.VacancyCreateException) as e:
        vacancy.Vacancy.create_from_dict(data)
    assert str(e.value) == 'Отсутствует ключ salary_from'


def test_create_from_dict_missing_salary_to_raises_error():
    data = {'name': 'test_name',
            'alternate_url': 'test_url',
            'salary_from': 'test_salary_from'
            }
    with pytest.raises(vacancy.VacancyCreateException) as e:
        vacancy.Vacancy.create_from_dict(data)
    assert str(e.value) == 'Отсутствует ключ salary_to'

def test_create_from_dict_missing_currency_raises_error():
    data = {'name': 'test_name',
            'alternate_url': 'test_url',
            'salary_from': 'test_salary_from',
            'salary_to': 'test_salary_to'
            }
    with pytest.raises(vacancy.VacancyCreateException) as e:
        vacancy.Vacancy.create_from_dict(data)
    assert str(e.value) == 'Отсутствует ключ currency'

def test_create_from_dict_missing_responsibility_raises_error():
    data = {'name': 'test_name',
            'alternate_url': 'test_url',
            'salary_from': 'test_salary_from',
            'salary_to': 'test_salary_to',
            'currency': 'test_currency'
            }
    with pytest.raises(vacancy.VacancyCreateException) as e:
        vacancy.Vacancy.create_from_dict(data)
    assert str(e.value) == 'Отсутствует ключ responsibility'


