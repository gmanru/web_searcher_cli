from search_google import search_phrase

search_system = input("Please, enter the serach system: 1)Google,2)Yandex\n")
key_word = input("Please, enter the keyword to serach\n")

if search_system == "1":

    search_phrase(str(key_word))
