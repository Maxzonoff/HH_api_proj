from src import vacancy, filters

from src import hh_api


def main():
    api = hh_api.HeadHunterAPI()
    search_query = input("Введите поисковый запрос: ")
    api.get_vacancies(search_query)
    search_words = input('Введите ключевые слова: ').split()
    vacancies = vacancy.Vacancy.cast_to_object_list(api.vacancies)
    vacancies = filters.filter_vacancies(vacancies, search_words)
    vacancies.sort(reverse=True)
    top_n = int(input('Введите количество вакансий по зарплате: '))
    vacancies = filters.top_n(vacancies, top_n)
    vacancies = list(map(str, vacancies))

    print('\n***\n'.join(vacancies))


if __name__ == '__main__':
    main()
