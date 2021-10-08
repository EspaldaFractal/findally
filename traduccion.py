# coding=utf-8
#¡IMPORTANTE! instalar la versión 3.1.0a0 ->->-> pip install googletrans==3.1.0a0
from googletrans import Translator

def traduccion(entrada):
    traductor = Translator()
    salida = traductor.translate(entrada, dest='en', src='es')
    return salida

consulta = "Un tipo musculoso con gafas que ingresa a un mundo virtual con súper poderes"
traduct = traduccion(consulta)
print(traduct)
