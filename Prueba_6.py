import math

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
                if torres[pos] > torres[pos -1]:
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
print(min_movimientos([7, 0, 0, 0, 0, 0, 0, 1]))  # Expected: 6
print(min_movimientos([24, 36, 38, 14, 7, 7, 7, 2, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])) # Expected: 2*
print(min_movimientos([4, 3, 2, 2, 4])) # Expected: 3
