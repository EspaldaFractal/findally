import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

oraciones = [ #diccionario
'Los perros son chéveres',
'El proyecto de integración multimedia trata de procesamiento del lenguaje',
'La cámara no está funcionando muy bien',
'Mañana no hay clase'
]
tokens = Tokenizer(num_words = 50, oov_token = "<OOV>")#El parámetro OOV se hace para
#generar nuevos códigos para palabras que no estaban en el diccionario original
tokens.fit_on_texts(oraciones)
codigos = tokens.word_index #Asignación de códigos a cada palabra
#print(codigos)
secuencias = tokens.texts_to_sequences(oraciones) #Convertir oraciones en códigos completos

entrada = [
'El proyecto de integración es sobre perros',
'La cámara se quedó sin pila'
]
secuencias_para_entrada = tokens.texts_to_sequences(entrada)
secuencias_para_entrada_padd = pad_sequences(secuencias_para_entrada) #El parámetro padding='pre'
#indica en qué orden se da el padding, mientras que maxlenght la longitud máxima de oraciones
#y truncate el sentido en que se truncan las oraciones que exceden el límite
print(secuencias_para_entrada_padd)
print(codigos)
