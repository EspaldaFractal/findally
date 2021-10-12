import numpy as np
#import filtro_categorias as fc
import json
from sklearn.feature_extraction.text import CountVectorizer
import re
import traduccion
import pandas

datos_pelis = pandas.read_csv("base_prueba.csv");
palabras_de_stop = json.load(open('stopword.json'))
palabras_de_stop = palabras_de_stop['english']

def seleccion_categoria(userRequest, language="english"):
    #Read global information
    stopWords = json.load(open('stopword.json'))

    categoryKeyWords = json.load(open('categoryKeyWords.json'))

    #Clean peticion
    regexStopWords = "|".join(stopWords[language])
    regexStopWords = r"\b("+regexStopWords+r")\b"
    userRequestClean = re.sub(regexStopWords, "", userRequest)

    #Count the times of
    categoriesDic= {"science fiction":0,"romance":0,"kids":0,"fantasy":0,"action":0}
    categoriesKeys= categoriesDic.keys()
    for categoryKey in categoriesKeys:
        regexCategoryKeyWords= r"\b("+"|".join(categoryKeyWords[categoryKey])+r")\b"
        categoryCoincidencies = re.findall(regexCategoryKeyWords,userRequestClean)
        #Count times that request match with categoryKeyWords
        categoriesDic[categoryKey]= len(categoryCoincidencies)

    #my_new_dict = {"q": 18, "z": 10, "o": 13}

    fin_max = max(categoriesDic, key=categoriesDic.get)
    return fin_max

def filtro_pelis(entrada_usuario, descipciones, palabras_malas):
	descipciones_dict = descipciones.to_dict()
	descipciones_dict = {value:key for key, value in descipciones_dict.items()}
	for k in descipciones_dict.keys():
	    descipciones_dict[k] = 0

	vectores = CountVectorizer(stop_words=palabras_malas, binary = True)
	matriz = vectores.fit_transform(descipciones_dict.keys())
	matriz = matriz.toarray()
	[n, m] = matriz.shape
	vector_consulta = np.zeros(m)

	entrada_usuario = entrada_usuario.split()
	for i in range(len(entrada_usuario)):
	    if entrada_usuario[i] in vectores.vocabulary_.keys():
	        vector_consulta[vectores.vocabulary_[entrada_usuario[i]]] += 1
	vector_consulta = vector_consulta[:, np.newaxis]
	producto = np.dot(matriz, vector_consulta)
	producto = producto.tolist()
	pos = producto.index(max(producto))
	return(pos)

entrada_original = "una pantera y un oso intentan convencer a un niño de ir a la selva"
entrada_traducida = traduccion.f_traduccion(entrada_original).text
cat_pref1 = seleccion_categoria(entrada_traducida,language="english")
categoria = datos_pelis[datos_pelis['genre'] == cat_pref1]
descripciones_cate = categoria['description']

indice = filtro_pelis(entrada_traducida, descripciones_cate, palabras_de_stop)
print("La posicion de la película más cercana a la búsqueda es la número " + str(indice) + " de la categoría " + str(cat_pref1) + "")
