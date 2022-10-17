class Reversa():
    """Iterador para recorrer una secuencia de atras para adelante"""
    def _init_(self, datos):
        self.datos = datos
        self.indice = len(datos)

    def _iter_(self):
        return self

    def _next_(self):
        if self.indice == 0:
            raise StopIteration()
        self.indice = self.indice-1
        return self.datos[self.indice]

for elemento in Reversa([1,2,3,4]):
    print(elemento)
    
