import pycountry
import langcodes

def getcountry(x):
    language_code=''
    language=''
    try:
        alpha2=pycountry.countries.search_fuzzy(x)[0].alpha_2
        language=pycountry.languages.get(alpha_2=alpha2).name
        language_code=langcodes.find(language).language

    except:
        pass
    return language_code,language