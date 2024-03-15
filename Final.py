import math
import sys

def min_movimientos(torres):
    n = len(torres)
    copia_torres = torres.copy()
    matriz = [[0 for _ in range(n)] for _ in range(2)]
    recorrido = 0
    memo0 = {}
    memo1 = {}

    def min_move_0(torres, pos, recorrido):
        llave = 0

        if pos != 0 and pos != n-1:
            llave = tuple([torres[pos-1],torres[pos],torres[pos+1]])

        if pos == 0:
            matriz[recorrido][pos] = 0
        elif pos == n - 1:
            matriz[recorrido][pos] = min_move_0(torres, n - 2, recorrido)

        else:
            minMov = 10**9

            if llave in memo0:
                return memo0[llave]
            elif torres[pos] < torres[pos + 1]:
                if torres[pos - 1] - torres[pos + 1] > 0:
                    torres[pos - 1] -= 1
                    torres[pos] += 1
                    matriz[recorrido][pos] +=1
                    memo0[llave] = matriz[recorrido][pos]
                    minMov = min(minMov, 1 + min_move_0(list(torres), pos, recorrido))
                else:
                    torres[pos + 1] -= 1
                    torres[pos] += 1
                    matriz[recorrido][pos] +=1
                    memo0[llave] = matriz[recorrido][pos]
                    minMov = min(minMov, 1 + min_move_0(list(torres), pos, recorrido))
            else:
                if torres[pos] > torres[pos -1] and torres[pos-1] <= torres[pos + 1]:
                    torres[pos ] -= 1
                    torres[pos-1] += 1
                    matriz[recorrido][pos] +=1
                    memo0[llave] = matriz[recorrido][pos]
                    minMov = min(minMov, 1 + min_move_0(list(torres), pos, recorrido))
                elif torres[pos] > torres[pos -1]:
                    torres[pos ] -= 1
                    torres[pos-1] += 1
                    matriz[recorrido][pos] +=1
                    memo0[llave] = matriz[recorrido][pos]
                    minMov = min(minMov, 1 + min_move_0(list(torres), pos-1, recorrido))
                else:
                    minMov = min(minMov, min_move_0(list(torres), pos - 1, recorrido))

            matriz[recorrido][pos] = minMov

        return matriz[recorrido][pos]
    
    def min_move_1(torres, pos, recorrido):
        if pos == 0:
            matriz[recorrido][pos] = 0
        elif pos == n - 1:
            matriz[recorrido][pos] = min_move_1(torres, n - 2, recorrido)

        else:
            minMov = 10**9
            if minMov > matriz[0][n-1]:
                return matriz[0][n-1]
            
            if torres[pos] > torres[pos +1]:
                    if torres[pos-1] >= torres[pos]:
                        torres[pos -1] -= 1
                        torres[pos+1] += 1
                        minMov= min(minMov, 1 + min_move_1(torres, pos, recorrido))
                    else:
                        torres[pos] -= 1
                        torres[pos+1] += 1
                        minMov = min(minMov, 1 + min_move_1(list(torres), pos, recorrido))
            else:
                if torres[pos+1] - torres[pos-1] > 0 and torres[pos-1]>torres[pos]:
                    torres[pos] -= 1
                    torres[pos] += 1
                    minMov = min(minMov, 1+min_move_1(list(torres), pos-1, recorrido))
                
                else:
                    minMov = min(minMov, min_move_1(list(torres), pos-1, recorrido))

            matriz[recorrido][pos] = minMov
        return matriz[recorrido][pos] 
    
    if n <= 1:
        return 0
    if n == 2:
        return math.ceil((torres[1]-torres[0])/2) if torres[0] < torres[1] else 0
    if recorrido == 0:
        min_move_0(torres, n - 1, 0)
        recorrido = 1
        #print(matriz[0][n-1])
    if recorrido == 1:
        min_move_1(copia_torres[::-1], n - 1, 1)
        #print(matriz[1][n-1])
        recorrido = 2
    if recorrido == 2:
        return min(matriz[0][n-1],matriz[1][n-1])
    

"""print(min_movimientos([0]))  # Expected: 0 
print(min_movimientos([1]))  # Expected: 0 
print(min_movimientos([1, 1]))  # Expected: 0 
print(min_movimientos([1, 2]))  # Expected: 1 
print(min_movimientos([2,1]))  # Expected: 0 
print(min_movimientos([2,1,0]))  # Expected: 0
print(min_movimientos([3,1,2]))  # Expected: 1 // 1 --> 1
print(min_movimientos([3,1,2,4]))  # Expected: 4 
print(min_movimientos([3, 2, 1, 4]))  # Expected: 3  
print(min_movimientos([3, 2, 2, 4]))  # Expected: 3 
print(min_movimientos([0, 0, 0, 0, 0, 0, 1]))  # Expected: 6 MAL
print(min_movimientos([4, 3, 2, 2, 4])) # Expected: 3 
print(min_movimientos([32, 11, 7, 5, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))  # Expected: 1 
print(min_movimientos([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 6, 6, 23, 29]))  # Expected: 536 (FALLA)
print(min_movimientos([0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 2, 9, 3, 5, 14, 19, 23, 32])) # Expected: 857 (FALLA)
print(min_movimientos([3, 2, 2, 4])) # Expected: 3 
print(min_movimientos([3, 0, 1, 1])) # Expected: 1 (FALLA)
print(min_movimientos([36, 38, 14, 7, 7, 7, 2, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])) # Expected: 2
print(min_movimientos([3, 0, 1, 1])) # Expected: 1 (FALLA)
print(min_movimientos([3,1,2,4]))  # Expected: 4 """


if __name__ == "__main__":
    number_of_cases = int(sys.stdin.readline().strip())
    for _ in range(number_of_cases):
        arreglo = list(map(int, sys.stdin.readline().split()))
        n = arreglo[0]
        torres = arreglo[1:]
        result = min_movimientos(torres)
        print(result)