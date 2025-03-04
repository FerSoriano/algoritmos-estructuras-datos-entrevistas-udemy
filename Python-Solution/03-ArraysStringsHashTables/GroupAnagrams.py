"""
 * Un anagrama es una palabra creada a partir de la reordenación de las letras de otra palabra. Ej: saco - caso
 * Dado un array de strings, devuelve los anagramas agrupados. Cualquier orden es válido.
 *
 * Ejemplo:
 *  Input: words = ["saco", "arresto", "programa", "rastreo", "caso"].
 *  Output: [["saco", "caso"], ["arresto", "rastreo"], ["programa"]].
 --
Crear una funcion para crear el Hash de acuerdo a las veces que se repite cada caracter de la palabra

"""
def GroupAnagrams(words: list) -> list:
    anagrams = []
    lenWords = {}
    for word in words:
        hash_str = getAnagramHash(word)
        if hash_str not in lenWords:
            lenWords[hash_str] = []
        lenWords[hash_str].append(word)

    return lenWords.values()
    # for k,v in lenWords.items():
    #     anagrams.append(v)

    # return anagrams


def getAnagramHash(string: str) -> str:
    letterCount = [0] * 26
    for c in string:
        letterCount[ord(c.lower())-97]+= 1 # ord() da el numero acorde a anscii. 'a' = 97.
    return str(letterCount)


words = ["saco", "arresto", "programa", "rastreo", "caso"]
anagrams = GroupAnagrams(words=words)

print(anagrams)