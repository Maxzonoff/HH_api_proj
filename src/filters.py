from src import vacancy


def top_n(vacancies: list, n: int) -> list:
    """Возвращая первые n вакансий"""
    return vacancies[:n]


def filter_vacancies(
    vacancies: list[vacancy.Vacancy], words: list[str]
) -> list[vacancy.Vacancy]:
    """Фильтрует вакансии по заданному списку слов"""
    res = []
    for vacancy_ in vacancies:
        if vacancy_.has_words(words):
            res.append(vacancy_)
    return res
