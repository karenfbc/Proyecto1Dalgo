import sys 

# Karen Fuentes
# Alison Aristizabal

def min_movimientos(torres):
    n = len(torres)
    assert 1 <= n <= 10**3, "El número de torres debe estar entre 1 y 10^3"
    assert sum(torres) >= 0 and sum(torres) <= 10**3, "La suma de las alturas de las torres debe estar entre 0 y 10^3"

    memo = {}

    def dp(pos, prev_height):
        if pos == n:
            return 0
        if (pos, prev_height) in memo:
            return memo[(pos, prev_height)]

        min_moves = 100000
        for i in range(int(prev_height), torres[pos] + 1):
            moves = i - torres[pos] + dp(pos + 1, i)
            min_moves = min(min_moves, moves)

        memo[(pos, prev_height)] = min_moves
        return min_moves

    return dp(0, 100000)
# Ejemplo de uso:
#torres = [5, 3, 7, 2, 8]
#print("Mínimo número de movimientos requeridos:", min_movimientos(torres))

"""def minMovimientos(fichas):
    n = len(fichas)
    # Calcula la altura total de las torres para encontrar la altura objetivo
    total_fichas = sum(fichas)
    
    # Inicializa la tabla de programación dinámica
    dp = [[float('inf')] * (total_fichas + 1) for _ in range(n+1)]
    dp[0][0] = 0  # No se requieren movimientos para 0 fichas
    
    # Rellena la tabla de DP
    for i in range(1, n+1):
        for j in range(total_fichas + 1):
            if j >= fichas[i-1]:  # Si podemos formar una torre con la altura actual
                # El mínimo entre no mover fichas o mover la ficha actual para alcanzar la altura j
                dp[i][j] = min(dp[i][j], dp[i-1][j], dp[i-1][j-fichas[i-1]] + abs((total_fichas // n) - j))
            else:
                dp[i][j] = dp[i-1][j]
                
    # Encuentra el mínimo número de movimientos en la última fila considerando la distribución ideal de fichas
    min_mov = float('inf')
    for j in range(total_fichas + 1):
        min_mov = min(min_mov, dp[n][j])
        
    return min_mov"""

# Ejemplo de uso
#fichas = [4, 3, 2, 1]
#print(minMovimientos(fichas))

if __name__ == "__main__":
    number_of_cases = int(sys.stdin.readline().strip())
    for _ in range(number_of_cases):
        arreglo = list(map(int, sys.stdin.readline().split()))
        n = arreglo[0]
        torres = arreglo[1:]
        result = min_movimientos(arreglo)
        print(result)