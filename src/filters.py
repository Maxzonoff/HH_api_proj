from src import vacancy



def top_n(vacancies: list[vacancy.Vacancy], n: int) -> list[vacancy.Vacancy]:
    return vacancies[:n]

def filter_vacancies(vacancies: list[vacancy.Vacancy], words: list[str]) -> list[vacancy.Vacancy]:
    res = []
    for vacancy_ in vacancies:
        if vacancy_.has_words(words):
            res.append(vacancy_)
    return res