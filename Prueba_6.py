import math
import sys

def min_movimientos(torres):
    n = len(torres)
    memo = {}  

    def min_move(torres, pos):
        key = tuple(torres), pos
        if key in memo:  
            return memo[key]

        if pos == 0:
            memo[key] = 0
        elif pos == n - 1:
            memo[key] = min_move(torres, n - 2)
        else:
            minMov = 10**9  # Inicializamos el mínimo número de movimientos con infinito
            if torres[pos] < torres[pos + 1]:
                if torres[pos - 1] - torres[pos + 1] > 0: #
                    torres[pos - 1] -= 1
                    torres[pos] += 1
                    minMov = min(minMov, 1 + min_move(list(torres), pos))
                else:
                    torres[pos + 1] -= 1
                    torres[pos] += 1
                    minMov = min(minMov, 1 + min_move(list(torres), pos))
            else:
                if torres[pos] > torres[pos -1] and torres[pos-1] < torres[pos + 1]:
                    torres[pos ] -= 1
                    torres[pos-1] += 1
                    minMov = min(minMov, 1 + min_move(list(torres), pos))
                else:
                    minMov = min(minMov, min_move(list(torres), pos - 1))
            memo[key] = minMov  #
        return memo[key]
    
    if n <= 1:
        return 0
    elif n == 2:
        return math.ceil((torres[1]-torres[0])/2) if torres[0] < torres[1] else 0
    else:
        return min_move(torres, n - 1)

print(min_movimientos([0]))  # Expected: 0 CHECK
print(min_movimientos([1]))  # Expected: 0 CHECK 
print(min_movimientos([1, 1]))  # Expected: 0 CHECK
print(min_movimientos([1, 2]))  # Expected: 1 CHECK 
print(min_movimientos([2,1]))  # Expected: 0 CHECK
print(min_movimientos([2,1,0]))  # Expected: 0 CHECK 
print(min_movimientos([3,1,2]))  # Expected: 1 CHECK 
print(min_movimientos([3,1,2,4]))  # Expected: 4 CHECK 
print(min_movimientos([3, 2, 1, 4]))  # Expected: 3 CHECK 
print(min_movimientos([3, 2, 2, 4]))  # Expected: 3 CHECK 
print(min_movimientos([7, 0, 0, 0, 0, 0, 0, 1]))  # Expected: 6 CHECK 
print(min_movimientos([24, 36, 38, 14, 7, 7, 7, 2, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])) # Expected: 2 (FALLA)
print(min_movimientos([4, 3, 2, 2, 4])) # Expected: 3 CHECK
print(min_movimientos([20, 32, 11, 7, 5, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))  # Expected: 1 CHECK
print(min_movimientos([18, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 6, 6, 23, 29]))  # Expected: 536 (FALLA)
print(min_movimientos([24, 36, 38, 14, 7, 7, 7, 2, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])) # Expected: 2 (FALLA)
print(min_movimientos([20, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 2, 9, 3, 5, 14, 19, 23, 32])) # Expected: 857 (FALLA)
print(min_movimientos([4, 3, 2, 2, 4])) # Expected: 3 CHECK 
print(min_movimientos([4, 3, 0, 1, 1])) # Expected: 2 CHECK

if __name__ == "__main__":
    number_of_cases = int(sys.stdin.readline().strip())
    for _ in range(number_of_cases):
        arreglo = list(map(int, sys.stdin.readline().split()))
        n = arreglo[0]
        torres = arreglo[1:]
        result = min_movimientos(arreglo)
        print(result)