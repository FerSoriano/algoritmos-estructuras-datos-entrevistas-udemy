"""
 * Dado un método que recibe una String, comprobar si todos los caracteres son únicos o no.
 *
 * isUnique("abcde") => true;
 * isUnique("abcded") => false;

 Solucion a utilizar: HashTable
 Complejidad -> O(N) - Lineal
 --
 Se puede mejorar a O(1) - Constante, si tomamos como referencia los simbolos del ASCII, 
 Si el largo del string es mayor al numero de ASCII, entonces si tenemos valores repetidos.
 Sino, siempre recorreremos los mismos numeros sin incrementar la complejidad.
 --
"""

def IsUnique_HashTable(string) -> bool:
    # creamos la tabla hash
    hashtable = {}
    for i,e in enumerate(string):
        if e in hashtable.keys():
            return False
        hashtable[e] = i
    return True

def IsUnique_MejorComplejidad(string) -> bool:
    NUMBER_OF_CHARS = 128 # ASCII

    if len(string) > NUMBER_OF_CHARS:
        return False

    hashtable = {}
    for i,e in enumerate(string):
        if e in hashtable.keys():
            return False
        hashtable[e] = i

    return True

print(IsUnique_MejorComplejidad("abcde"))
print(IsUnique_MejorComplejidad("abcdefghijklmnopqrstuvwxyzo"))


