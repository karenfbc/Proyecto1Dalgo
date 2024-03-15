import math


def min_movimientos(torres):
    n = len(torres)
    matriz = [[0 for _ in range(n)] for _ in range(2)]
    recorrido = 0

    def min_move_0(torres, pos, recorrido):

        if pos == 0:
            matriz[recorrido][pos] = 0
        elif pos == n - 1:
            matriz[recorrido][pos] = min_move_0(torres, n - 2, recorrido)

        else:
            minMov = 10**9
            if torres[pos] < torres[pos + 1]:
                if torres[pos - 1] - torres[pos + 1] > 0: #
                    torres[pos - 1] -= 1
                    torres[pos] += 1
                    minMov = min(minMov, 1 + min_move_0(list(torres), pos, recorrido))
                else:
                    torres[pos + 1] -= 1
                    torres[pos] += 1
                    minMov = min(minMov, 1 + min_move_0(list(torres), pos, recorrido))
            else:
                if torres[pos] > torres[pos -1] and torres[pos-1] <= torres[pos + 1]:
                    torres[pos ] -= 1
                    torres[pos-1] += 1
                    minMov = min(minMov, 1 + min_move_0(list(torres), pos, recorrido))
                elif torres[pos] > torres[pos -1]:
                    torres[pos ] -= 1
                    torres[pos-1] += 1
                    minMov = min(minMov, 1 + min_move_0(list(torres), pos-1, recorrido))
                else:
                    minMov = min(minMov, min_move_0(list(torres), pos - 1, recorrido))

            matriz[recorrido][pos] = minMov
        return matriz[recorrido][pos] 
    
    def min_move_1(torres, pos, recorrido):

        if pos == 0:
            matriz[recorrido][pos] = 0
        elif pos == n - 1:
            matriz[recorrido][pos] = min_move_0(torres, n - 2, recorrido)

        else:
            minMov = 10**9
            if torres[pos] > torres[pos + 1]:
                if torres[pos - 1] - torres[pos + 1] < 0: #
                    torres[pos - 1] += 1
                    torres[pos] -= 1
                    minMov = min(minMov, 1 + min_move_0(list(torres), pos, recorrido))
                else:
                    torres[pos + 1] += 1
                    torres[pos] -= 1
                    minMov = min(minMov, 1 + min_move_0(list(torres), pos, recorrido))
            else:
                if torres[pos] < torres[pos -1] and torres[pos-1] >= torres[pos + 1]:
                    torres[pos ] += 1
                    torres[pos-1] -= 1
                    minMov = min(minMov, 1 + min_move_0(list(torres), pos, recorrido))
                elif torres[pos] < torres[pos -1]:
                    torres[pos] += 1
                    torres[pos-1] -= 1
                    minMov = min(minMov, 1 + min_move_0(list(torres), pos-1, recorrido))
                else:
                    minMov = min(minMov, min_move_0(list(torres), pos - 1, recorrido))

            matriz[recorrido][pos] = minMov
        return matriz[recorrido][pos] 
    
    if n <= 1:
        return 0
    if n == 2:
        return math.ceil((torres[1]-torres[0])/2) if torres[0] < torres[1] else 0
    if recorrido == 0:
        min_move_0(torres, n - 1, 0)
        recorrido = 1
        print(matriz[0][n-1])
    if recorrido == 1:
        min_move_1(torres, n - 1, 1)
        print(matriz[1][n-1])


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
