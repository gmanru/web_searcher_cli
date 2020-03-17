from search_google import search_phrase
from search_yandex import yandex_query
from  export import mass_dict_to_csv
from  export import mass_dict_to_json

def intro():
    key_word = input("Введите текст запроса в поисковик ")
    search_system = input("Пожалуйста, выберите поисковую систему: 1) Google , 2) Yandex\n")
    output_file = input("Пожалуйста, выберите формат вывода запроса: 1)В консоль, 2)Csv файл, 3)Json файл\n")


    if search_system == "1":
         mass = search_phrase(str(key_word))
         if output_file == "2":
            mass_dict_to_csv(mass)

         if output_file == "3":
              mass_dict_to_json(mass)
    elif search_system == "2":
         yandex_query(str(key_word))
         if output_file == "2":
                mass_dict_to_csv(mass)

         if output_file == "3":
              mass_dict_to_json(mass)
