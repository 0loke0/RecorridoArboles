from ArbolBinarioBusqueda import ArbolBinarioBusqueda

arbol = ArbolBinarioBusqueda()

#Insertar los valores al arbol
arbol.insertar(18)
arbol.insertar(5)
arbol.insertar(3)
arbol.insertar(4)
arbol.insertar(1)
arbol.insertar(8)
arbol.insertar(20)
arbol.insertar(19)
arbol.insertar(21)
arbol.insertar(22)

print("\nRecorrido inorder")
arbol.ObtenerInorder(arbol.raiz)
print("\n")

print("\nNodos que tiene 2 hijos")
arbol.ObtenerHijosCompletos(arbol.raiz)
print("\n")

print("\nNodos que tiene hijos con par")
arbol.ObtenerHijosConPar(arbol.raiz)
print("\n")

print("\nSuma de hijos")
arbol.ObtenerSumaHijos(arbol.raiz)
print("\n")

print("\nRuta nodo buscado")
arbol.ObtenerRutaNodo(arbol.raiz,4)
print("\n")
