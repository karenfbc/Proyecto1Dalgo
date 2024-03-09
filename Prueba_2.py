import sys

def min_movimientos(torres):
    # Base case: si solo hay una torre, el mínimo número de movimientos es 0
    if len(torres) == 1:
        return 0
    
    # Creamos una matriz para memoización
    n = len(torres)
    memo = [[-1] * n for _ in range(n)]
    
    # Función auxiliar recursiva
    def helper(torres, index, prev_index):
        # Verificar si ya hemos calculado este estado
        if memo[index][prev_index] != -1:
            return memo[index][prev_index]
        
        # Base case: si hemos llegado al final de las torres, el mínimo número de movimientos es 0
        if index == len(torres) - 1:
            return 0
        
        min_movs = 10000000000000000
        for i in range(max(0, prev_index-1), min(n, prev_index+2)):
            if torres[i] < torres[index]:
                # Calcular los movimientos restantes recursivamente
                movimientos_restantes = helper(torres, i, index)
                # Actualizar el mínimo número de movimientos
                min_movs = min(min_movs, movimientos_restantes)
        
        # Guardar el resultado en la matriz de memoización
        memo[index][prev_index] = min_movs + 1
        return min_movs + 1
    
    # Llamar a la función auxiliar con las torres y el índice inicial
    return helper(torres, 0, 0)

# Ejemplo de uso
#torres = [3, 2, 1, 4]
#print(min_movimientos(torres))


if __name__ == "__main__":
    number_of_cases = int(sys.stdin.readline().strip())
    for _ in range(number_of_cases):
        arreglo = list(map(int, sys.stdin.readline().split()))
        result = min_movimientos(arreglo)
        print(result)