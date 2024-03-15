import math


def min_movimientos(torres):
    n = len(torres)
    matriz = [[0 for _ in range(n)] for _ in range(2)]
    recorrido = 0

    def min_move_0(torres, pos, recorrido, memo={}):
        # Convertimos el estado actual de 'torres' a una tupla para poder usarlo como clave en el diccionario 'memo'
        torres_tupla = tuple(torres)
        # Generamos la clave única combinando el estado de 'torres', 'pos' y 'recorrido'
        clave = (torres_tupla, pos, recorrido)
        
        # Verificamos si el resultado ya está calculado en 'memo'
        if clave in memo:
            print("llegue")
            return memo[clave]

        n = len(torres)  # Suponiendo que 'n' es la longitud de 'torres'
        
        if pos == 0:
            resultado = 0
        elif pos == n - 1:
            resultado = min_move_0(torres, n - 2, recorrido, memo)
        else:
            minMov = float('inf')
            if torres[pos] < torres[pos + 1]:
                if torres[pos - 1] - torres[pos + 1] > 0: 
                    torres[pos - 1] -= 1
                    torres[pos] += 1
                    minMov = min(minMov, 1 + min_move_0(list(torres), pos, recorrido, memo))
                else:
                    torres[pos + 1] -= 1
                    torres[pos] += 1
                    minMov = min(minMov, 1 + min_move_0(list(torres), pos, recorrido, memo))
            else:
                if torres[pos] > torres[pos -1] and torres[pos-1] <= torres[pos + 1]:
                    torres[pos] -= 1
                    torres[pos-1] += 1
                    minMov = min(minMov, 1 + min_move_0(list(torres), pos, recorrido, memo))
                elif torres[pos] > torres[pos -1]:
                    torres[pos] -= 1
                    torres[pos-1] += 1
                    minMov = min(minMov, 1 + min_move_0(list(torres), pos-1, recorrido, memo))
                else:
                    minMov = min(minMov, min_move_0(list(torres), pos - 1, recorrido, memo))
            resultado = minMov

        # Almacenamos el resultado en 'memo' antes de retornarlo
        memo[clave] = resultado
        return resultado

    # NOTA: La llamada a la función está comentada para evitar la ejecución automática.
    # min_move_0(torres, pos, recorrido)

    
    if n <= 1:
        return 0
    elif n == 2:
        return math.ceil((torres[1]-torres[0])/2) if torres[0] < torres[1] else 0
    else:
        return min_move_0(torres, n - 1, recorrido)



print(min_movimientos([0]))  # Expected: 0 
print(min_movimientos([1]))  # Expected: 0 
print(min_movimientos([1, 1]))  # Expected: 0 
print(min_movimientos([1, 2]))  # Expected: 1 
print(min_movimientos([2,1]))  # Expected: 0 
print(min_movimientos([2,1,0]))  # Expected: 0 
print(min_movimientos([3,1,2]))  # Expected: 1 
print(min_movimientos([3,1,2,4]))  # Expected: 4 
print(min_movimientos([3, 2, 1, 4]))  # Expected: 3  
print(min_movimientos([3, 2, 2, 4]))  # Expected: 3 
print(min_movimientos([0, 0, 0, 0, 0, 0, 1]))  # Expected: 6
print(min_movimientos([4, 3, 2, 2, 4])) # Expected: 3 
print(min_movimientos([32, 11, 7, 5, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))  # Expected: 1 
print(min_movimientos([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 6, 6, 23, 29]))  # Expected: 536 (FALLA)
print(min_movimientos([0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 2, 9, 3, 5, 14, 19, 23, 32])) # Expected: 857 (FALLA)
print(min_movimientos([3, 2, 2, 4])) # Expected: 3 
print(min_movimientos([3, 0, 1, 1])) # Expected: 1 (FALLA)
print(min_movimientos([36, 38, 14, 7, 7, 7, 2, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])) # Expected: 2
print(min_movimientos([3, 0, 1, 1])) # Expected: 1 (FALLA)
