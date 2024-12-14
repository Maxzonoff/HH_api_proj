from src import filters, hh_api, vacancy
from src.storage import JsonStorage


def main():
    saver = JsonStorage("data/data.json")
    api = hh_api.HeadHunterAPI()
    search_query = input("Введите поисковый запрос: ")
    api.get_vacancies(search_query)
    search_words = input("Введите ключевые слова: ").split()
    vacancies = vacancy.Vacancy.cast_to_object_list(api.vacancies)
    for vac in vacancies:
        saver.add_vacancy(vac)
    vacancies = saver.load()
    vacancies = filters.filter_vacancies(vacancies, search_words)
    vacancies.sort(reverse=True)
    top_n = int(input("Введите количество вакансий по зарплате: "))
    vacancies = filters.top_n(vacancies, top_n)
    vacancies = list(map(str, vacancies))

    print("\n***\n".join(vacancies))


if __name__ == "__main__":
    main()
