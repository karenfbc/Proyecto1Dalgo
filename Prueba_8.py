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
            print(str(torres[pos-1]),str(torres[pos]),str(torres[pos+1]))
            if torres[pos] < torres[pos + 1]:
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
    if n <= 1:
        return 0
    elif n == 2:
        return math.ceil((torres[1]-torres[0])/2) if torres[0] < torres[1] else 0
    else:
        return min_move_0(torres, n - 1, recorrido)

print(min_movimientos([1, 1, 0, 3]))