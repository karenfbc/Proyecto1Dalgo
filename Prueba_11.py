import math


def min_movimientos(torres):
    n = len(torres)
    div=n//3
    izq= torres[:div]
    medio= torres[div:div+div]
    der= torres[div+div:0]
    def min_move_0(torres, pos, recorrido):
        pass
    if n <= 1:
        return 0
    elif n == 2:
        return math.ceil((torres[1] - torres[0]) / 2) if torres[0] < torres[1] else 0
    else:
        return min_move_0(list(reversed(torres)), n - 1, recorrido)

# Ejemplo de uso
torres = [3, 2, 5, 4, 6]
print(min_movimientos(torres))


# Ejemplo de uso
#print(min_movimientos([1, 1, 0, 0]))
#print(min_movimientos([0]))  # Expected: 0
#print(min_movimientos([1]))  # Expected: 0
#print(min_movimientos([1, 1]))  # Expected: 0
#print(min_movimientos([1, 2]))  # Expected: 1
#print(min_movimientos([2, 1, 4]))  # Expected: 3
print(min_movimientos([2, 2, 4]))  # Expected: 2
#print(min_movimientos([0, 0, 0, 0, 0, 0, 1]))  # Expected: 6
#print(min_movimientos([32, 11, 7, 5, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))  # Expected: 1
#print(min_movimientos([18, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 6, 6, 23, 29]))  # Expected: 536
#print(min_movimientos([24, 36, 38, 14, 7, 7, 7, 2, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])) # Expected: 2
#print(min_movimientos([20, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 2, 9, 3, 5, 14, 19, 23, 32])) # Expected: 857
#print(min_movimientos([4, 3, 2, 2, 4])) # Expected: 3
#print(min_movimientos([4, 3, 0, 1, 1])) # Expected: 1
