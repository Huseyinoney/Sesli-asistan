
import wikipedia


wikipedia.set_lang("tr")
#a=wikipedia.summary("türkiye",sentences=2)
#print(a)


def sözlük(ifade):
    wikipedia.set_lang("tr")
    a=wikipedia.summary(ifade,sentences=3)
    return a

