import math
import sys

def min_movimientos(torres):
    n = len(torres)
    
    def min_move(torres, pos):
        if pos == n - 1:
            return 0
        else:
            minMov = 10**9  # Inicializamos el mínimo número de movimientos con infinito
            if pos == 0 and torres[pos]< torres[pos + 1]:
                torres[pos] += math.ceil((torres[1]-torres[0])/2)
            elif torres[pos] < torres[pos + 1] and pos != 0:
                if torres[pos - 1] - torres[pos + 1] > 0:
                    torres[pos + 1] -= 1
                    torres[pos] += 1
                    minMov = min(minMov, 1 + min_move(torres, pos))
                else:
                    torres[pos - 1] -= 1
                    torres[pos] += 1
                    minMov = min(minMov, 1 + min_move(torres, pos))
            else:
                minMov = min(minMov, min_move(torres, pos + 1))
                
        return minMov
    
    if n <= 1:
        return 0
    else:
        return min_move(torres, 0)


    # Uso de ejemplo
print(min_movimientos([0]))  # Expected: 0
print(min_movimientos([1]))  # Expected: 0
print(min_movimientos([1, 1]))  # Expected: 0
print(min_movimientos([1, 2]))  # Expected: 1
print(min_movimientos([3, 2, 1, 4]))  # Expected: 3
print(min_movimientos([3, 2, 2, 4]))  # Expected: 2
print(min_movimientos([7, 0, 0, 0, 0, 0, 0, 1]))  # Expected: 6
print(min_movimientos([20, 32, 11, 7, 5, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))  # Expected: 1
print(min_movimientos([18, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 6, 6, 23, 29]))  # Expected: 536
print(min_movimientos([24, 36, 38, 14, 7, 7, 7, 2, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])) # Expected: 2
print(min_movimientos([20, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 2, 9, 3, 5, 14, 19, 23, 32])) # Expected: 857
print(min_movimientos([4, 3, 2, 2, 4])) # Expected: 3
print(min_movimientos([4, 3, 0, 1, 1])) # Expected: 1