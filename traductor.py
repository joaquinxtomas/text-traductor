from googletrans import Translator

translator = Translator()

dec = input("""Desde que idioma a que idioma desea traducir?
            1-Inglés al español
            2-Español al inglés
            ------------------------------------------------
            """)

if(dec =="1"):
    to_translate = input("Ingrese el texto que desea traducir: ")
    trlted = translator.translate(to_translate, src="en", dest="es")
    print(f'Traducción: {trlted.text}')
elif(dec == "2"):
    to_translate = input("Ingrese el texto que desea traducir: ")
    trlted = translator.translate(to_translate,src="es",dest="en")
    print(f'Traducción: {trlted.text}')
else:
    print("Opción inválida.")
    

