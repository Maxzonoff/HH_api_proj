from src import vacancy


def top_n(vacancies: list, n: int) -> list:
    return vacancies[:n]


def filter_vacancies(
    vacancies: list[vacancy.Vacancy], words: list[str]
) -> list[vacancy.Vacancy]:
    res = []
    for vacancy_ in vacancies:
        if vacancy_.has_words(words):
            res.append(vacancy_)
    return res
