# coding=utf-8
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
import filtro_categorias as fc

elementos_a_borrar = ['un', 'con', 'que', 'en', 'al', 'lo',
'la', 'e', 'de', 'es', 'el', 'del', 'para', 'una', 'a', 'y']

categorias = [fc.ciencia_ficcion(), fc.romance(), fc.fantasia(), fc.accion(), fc.infantiles()]

entrada_usuario = 'mundo fantástico con criaturas';
consulta = entrada_usuario
entrada_usuario = entrada_usuario.split()
entrada_usuario.sort()
entrada_usuario = [word for word in entrada_usuario if word.lower() not in elementos_a_borrar]

sum_cat = np.zeros(len(categorias))
sum_cat = sum_cat.tolist()

for i in range(0,len(categorias)-1):
    for j in range(0, len(entrada_usuario)-1):
        if entrada_usuario[j] in categorias[i].palabras:
            sum_cat[i] += 1
cat_pref1 = sum_cat.index(max(sum_cat))
#cat_pref2 = sum_cat.index(max(sum_cat)-1)


vectores = CountVectorizer(stop_words=elementos_a_borrar, binary = True)
matriz = vectores.fit_transform(categorias[cat_pref1].textos)
matriz = matriz.toarray()
[n, m] = matriz.shape
vector_consulta = np.zeros(m)

for i in range(len(entrada_usuario)):
    if entrada_usuario[i] in vectores.vocabulary_.keys():
        vector_consulta[vectores.vocabulary_[entrada_usuario[i]]] += 1

vector_consulta = vector_consulta[:, np.newaxis]
producto = np.dot(matriz, vector_consulta)
producto = producto.tolist()
pos = producto.index(max(producto))
print("Con la consulta: " + consulta + " quizá te refieres a \n")
print(categorias[cat_pref1].titulos[pos])
