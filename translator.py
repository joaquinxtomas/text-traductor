from googletrans import Translator
import traductor as tc

translator = Translator()

lang = ("Ingles", "Español", "Portugués", "Mandarín", "Francés")
cod_lang = ["en", "es", "pt","zh-tw","fr"]

tc.show_languages(lang)

lang_1= input(f"Ingrese el numero del idioma de origen del texto: ")

if lang_1.isnumeric() and len(lang) > 0:
    selctd_lang = lang[int(lang_1)-1]
    code_language = cod_lang[int(lang_1)-1]


tc.show_languages(lang)

to_translate = input("Ingrese el numero del idioma al que desea traducirlo:")

if to_translate.isnumeric() and len(lang) > 0:
    to_translate_lang = lang[int(to_translate) - 1]
    to_translate_code = cod_lang[int(to_translate) - 1]
    
text = input("Ingrese el texto a traducir: ")

trlted = translator.translate(text,src=code_language,dest=to_translate_code)
print(f'Traduccion de lo escrito: {trlted.text}')