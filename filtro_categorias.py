import numpy as np

class ciencia_ficcion:
    def __init__(self):
        self.categoria = "ciencia ficción"
        self.palabras = ['futuro', 'futurismo', 'futurista', 'utopía',
        'distopía', 'tecnología', 'tecnológico', 'robots', 'cyborg',
        'virtual'
        ]
        self.textos = ['un tipo musculoso con gafas que entra en un mundo virtual.']
        self.titulos = ['Matrix']
class romance:
    def __init__(self):
        self.categoria = "romance"
        self.palabras = ['amor', 'melancolía', 'relación', 'pareja',
        'ternura', 'tristeza', 'beso', 'matrimonio', 'romántica',
        'romántico', 'tierna', 'tierno']
class infantiles:
    def __init__(self):
        self.categoria = "infantiles"
        self.palabras = ['magia', 'mágico', 'amigable', 'cuento',
        'cuentos', 'fábula', 'caricaturezcos', 'caricatura', 'tierno']
        self.textos = ['alicia es una niña que ingresa a un mundo fantástico rodeada de personajes caricaturezcos.',
        ]
        self.titulos = ['Alicia en el país de las maravillas']
class fantasia:
    def __init__(self):
        self.categoria = "fantasia"
        self.palabras = ['criaturas', 'fantástica', 'fantástico',
        'mágia', 'mágico', 'hechicería', 'fantasía', 'mágicas']
        self.textos = ['un chinito al que lo bullea la familia e ingresa a una escuela de magia.',
        'mundo fantástico lleno de magia y criaturas.',
        ]
        self.titulos = ['Harry Potter', 'El señor de los anillos']
class accion:
    def __init__(self):
        self.categoria = "accion"
        self.palabras = ['autos', 'armas', 'guerra', 'carros']
        self.textos = ['la familia es lo primero, y estos conductores de autos lo saben.',
        'John travolta va otra vez a otro país del tercer mundo otra vez a librerarlo',
        'Otra película más de acción con armas y rubias']
        self.titulos = ['Rápidos y furiosos', 'John travolta otra vez', 'Rambo otra vez']
