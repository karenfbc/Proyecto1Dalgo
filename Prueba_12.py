import math

def min_movimientos(torres):
    n = len(torres)
    matriz = [[0 for _ in range(n)] for _ in range(2)]
    recorrido = 0

    def min_move_0(torres, pos, recorrido):
        # Creamos una tabla de memoización para almacenar los resultados calculados previamente
        memo = [[10**9] * n for _ in range(n)]

        def dp(pos, recorrido):
            # Verificar si el resultado ya está en la tabla de memoización
            if memo[pos][recorrido] != 10**9:
                return memo[pos][recorrido]

            if pos == 0:
                resultado = 0
            elif pos == n - 1:
                resultado = dp(n - 2, recorrido)
            else:
                minMov = 10**9
                if torres[pos] < torres[pos + 1]:
                    if torres[pos - 1] - torres[pos + 1] > 0: 
                        torres[pos - 1] -= 1
                        torres[pos] += 1
                        minMov = min(minMov, 1 + dp(pos, recorrido))
                    else:
                        torres[pos + 1] -= 1
                        torres[pos] += 1
                        minMov = min(minMov, 1 + dp(pos, recorrido))
                else:
                    if torres[pos] > torres[pos -1] and torres[pos-1] <= torres[pos + 1]:
                        torres[pos] -= 1
                        torres[pos-1] += 1
                        minMov = min(minMov, 1 + dp(pos, recorrido))
                    elif torres[pos] > torres[pos -1]:
                        torres[pos] -= 1
                        torres[pos-1] += 1
                        minMov = min(minMov, 1 + dp(pos-1, recorrido))
                    else:
                        minMov = min(minMov, dp(pos - 1, recorrido))
                resultado = minMov

            # Almacenar el resultado en la tabla de memoización
            memo[pos][recorrido] = resultado
            return resultado

        return dp(pos, recorrido)

    if n <= 1:
        return 0
    elif n == 2:
        return math.ceil((torres[1] - torres[0]) / 2) if torres[0] < torres[1] else 0
    else:
        return min_move_0(torres, n - 1, recorrido)

# Ejemplo de uso
print(min_movimientos([0]))  # Expected: 0 
print(min_movimientos([1]))  # Expected: 0 
print(min_movimientos([1, 1]))  # Expected: 0 
print(min_movimientos([1, 2]))  # Expected: 1 
print(min_movimientos([2,1]))  # Expected: 0 
print(min_movimientos([2,1,0]))  # Expected: 0 
print(min_movimientos([3,1,2]))  # Expected: 1 
print(min_movimientos([1,2,4]))  # Expected: 4 
print(min_movimientos([2, 1, 4]))  # Expected: 3  
print(min_movimientos([2, 2, 4]))  # Expected: 3 
print(min_movimientos([0, 0, 0, 0, 0, 0, 1]))  # Expected: 6
print(min_movimientos([3, 2, 2, 4])) # Expected: 3 
print(min_movimientos([11, 7, 5, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))  # Expected: 1 
print(min_movimientos([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 6, 6, 23, 29]))  # Expected: 536 (FALLA)
print(min_movimientos([0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 2, 9, 3, 5, 14, 19, 23, 32])) # Expected: 857 (FALLA)
print(min_movimientos([2, 2, 4])) # Expected: 3 
print(min_movimientos([3, 0, 1, 1])) # Expected: 1 (FALLA)
print(min_movimientos([36, 38, 14, 7, 7, 7, 2, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])) # Expected: 2
