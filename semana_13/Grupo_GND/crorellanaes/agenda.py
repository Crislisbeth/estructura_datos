import time
import random

class NodoBST:
    def __init__(self, clave, valor):
        self.clave = clave
        self.valor = valor
        self.izquierda = None
        self.derecha = None

class BST:
    def __init__(self):
        self.raiz = None

    def insertar(self, clave, valor):
        self.raiz = self._insertar(self.raiz, clave, valor)

    def _insertar(self, nodo, clave, valor):
        if nodo is None:
            return NodoBST(clave, valor)
        if clave < nodo.clave:
            nodo.izquierda = self._insertar(nodo.izquierda, clave, valor)
        elif clave > nodo.clave:
            nodo.derecha = self._insertar(nodo.derecha, clave, valor)
        else:
            nodo.valor = valor  
        return nodo

    def buscar(self, clave):
        return self._buscar(self.raiz, clave)

    def _buscar(self, nodo, clave):
        if nodo is None or nodo.clave == clave:
            return nodo
        if clave < nodo.clave:
            return self._buscar(nodo.izquierda, clave)
        return self._buscar(nodo.derecha, clave)

class Lista:
    def __init__(self):
        self.elementos = []

    def insertar(self, clave, valor):
        self.elementos.append((clave, valor))

    def buscar(self, clave):
        for elemento in self.elementos:
            if elemento[0] == clave:
                return elemento
        return None

def medir_tiempos():
    bst = BST()
    lista = Lista()
    claves = [random.randint(1, 10000) for _ in range(1000)]

    inicio = time.time()
    for clave in claves:
        bst.insertar(clave, f"Valor {clave}")
    tiempo_bst_insert = time.time() - inicio

    inicio = time.time()
    for clave in claves:
        lista.insertar(clave, f"Valor {clave}")
    tiempo_lista_insert = time.time() - inicio

    inicio = time.time()
    for _ in range(100):
        bst.buscar(random.choice(claves))
    tiempo_bst_buscar = time.time() - inicio

    inicio = time.time()
    for _ in range(100):
        lista.buscar(random.choice(claves))
    tiempo_lista_buscar = time.time() - inicio

    print(f"Tiempo de insercion en BST: {tiempo_bst_insert:.6f} segundos")
    print(f"Tiempo de insercion en lista: {tiempo_lista_insert:.6f} segundos")
    print(f"Tiempo de busqueda en BST: {tiempo_bst_buscar:.6f} segundos")
    print(f"Tiempo de busqueda en lista: {tiempo_lista_buscar:.6f} segundos")

if __name__ == "__main__":
    medir_tiempos()
