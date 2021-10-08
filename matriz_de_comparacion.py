# coding=utf-8
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np

texto = ['un tipo musculoso con gafas que entra en un mundo virtual.',
'un chinito al que lo bullea la familia e ingresa a una escuela de magia.',
'la tierra media es un mundo fantástico en el que la comunidad del anillo luchará contra el mal para librar la tierra media.',
'alicia es una niña que ingresa a un mundo fantástico rodeada de personajes caricaturezcos.',
'la familia es lo primero, y estos conductores de autos lo saben.']

elementos_a_borrar = ['un', 'con', 'que', 'en', 'al', 'lo',
'la', 'e', 'de', 'es', 'el', 'del', 'para', 'una', 'a', 'y']

vectores = CountVectorizer(stop_words=elementos_a_borrar, binary = True)
matriz = vectores.fit_transform(texto)
matriz = matriz.toarray()
#print(matriz)
#print(matriz.shape)
claves = list(vectores.vocabulary_.keys())
indices = list(vectores.vocabulary_.values())
#print(len(claves))

entrada_usuario = 'Mundo fantástico con personajes caricaturezcos y magia';
entrada_usuario_lista = entrada_usuario.split()

entrada_usuario = [word for word in entrada_usuario_lista if word.lower() not in elementos_a_borrar]
#print(entrada_usuario)
vector_res = np.zeros(len(texto))
tam = matriz.shape
