import json
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import numpy as np

#Esta parte corresponde a la carga y conversión del archivo json
with open("sarcasmo.json", 'r') as f:
    conjunto_datos = json.load(f)

oraciones = []
indicador = []
enlaces = []
for item in conjunto_datos:
    oraciones.append(item['headline'])
    indicador.append(item['is_sarcastic'])
    enlaces.append(item['article_link'])
#fin carga y conversión de archivo json
#Separamos datos de entrenamiento y datos de prueba
tam_entre = 20500
oraciones_entre = oraciones[0:tam_entre]
oraciones_pru = oraciones[tam_entre:]
indicador_entre = indicador[0:tam_entre]
indicador_pru = indicador[tam_entre:]
#fin separación datos entrenamiento y prueba
#generación de tokens para las distintas palabras
tokens = Tokenizer(num_words=10000,oov_token="<OOV>")
tokens.fit_on_texts(oraciones_entre)
indice_palabras = tokens.word_index

secuencias = tokens.texts_to_sequences(oraciones_entre)
secuencias_pad = pad_sequences(secuencias,maxlen=100, padding='post', truncating = 'post')

secuencias_pru = tokens.texts_to_sequences(oraciones_pru)
secuencias_pru_pad = pad_sequences(secuencias_pru, maxlen = 100, padding='post', truncating = 'post')
#fin generación de tokens
#entranamiento red neuronal
modelo = tf.keras.Sequential([tf.keras.layers.Embedding(10000, 16, input_length=100),
tf.keras.layers.GlobalAveragePooling1D(),
tf.keras.layers.Dense(24, activation = 'relu'),
tf.keras.layers.Dense(1, activation='sigmoid')
])
modelo.compile(loss='binary_crossentropy', optimizer = 'adam', metrics = ['accuracy'])

modelo.summary()

#arreglo de los datos con numpy
secuencias_pad = np.array(secuencias_pad)
indicador_entre = np.array(indicador_entre)
secuencias_pru_pad = np.array(secuencias_pru_pad)
indicador_pru = np.array(indicador_pru)
#fin arreglo de los datos con numpy

history = modelo.fit(secuencias_pad, indicador_entre, epochs=30,
validation_data=(secuencias_pru_pad, indicador_pru), verbose = 2)
#Fin entrenamiento red neuronal
#prueba red neuronal
oraciones_usuario = [
"granny starting to fear spiders in the garden might be real",
"game of thrones season finale showing this sunday night"
]
secuencias_usuario = tokens.texts_to_sequences(oraciones_usuario)
secuencias_usuario_pad = pad_sequences(secuencias_usuario, 100, padding='post', truncating = 'post')

prediccion = modelo.predict(secuencias_usuario_pad)
print(prediccion)
#fin prueba red neuronal
