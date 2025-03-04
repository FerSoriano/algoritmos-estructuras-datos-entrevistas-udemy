"""
 * Dado un array de números enteros y un target, retorna los índices de dos
 * números para los que la suma de ambos sea igual al target.
 *
 * Puedes asumir que hay solamente una solución.
 *
 * Ejemplo 1:
 *  Input: nums = [9,2,5,6], target = 7
 *  Output: [1,2]
 *  Explicación: nums[1] + nums[2] == 7, devolvemos [1, 2].
 *
 * Ejemplo 2:
 *  Input: nums = [9,2,5,6], target = 100
 *  Output: null
 --
 Solucion O(N) -> Lineal
"""

def twoSum(arr, target) -> list:
    # Creamos mi Hash table
    values = {}
    for i,e in enumerate(arr):
        diff = target - e
        if diff in values.keys():
            return [values.get(diff), i]
        values[e] = i
    return None

print(twoSum([9,2,5,6], 7))