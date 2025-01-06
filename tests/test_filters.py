from src.filters import filter_vacancies, top_n
from src.vacancy import Vacancy


def test_top_n():
    vac = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    res = top_n(vac, 4)
    assert res == [1, 2, 3, 4]


def test_filter_vacancies():
    vac = [
        Vacancy(None, None, None, None, None, None, ""),
        Vacancy(None, None, None, None, None, None, "a"),
        Vacancy(None, None, None, None, None, None, "b"),
        Vacancy(None, None, None, None, None, None, "a b"),
    ]
    res = filter_vacancies(vac, ["a"])
    assert res == [vac[1], vac[3]]
