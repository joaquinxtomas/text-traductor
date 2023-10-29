def show_languages(list):
    print("Idiomas disponibles: \n")
    for i, language in enumerate(list, start = 1):
        print(f'{i}-{language}')
    print("--------------------------------------")
