import sys

def min_movimientos(torres):
    n = len(torres)
    def min_move(torres, pos):
        minMov=10**9
        if pos == 0:
           return 0
        if pos == n:
            return min_move(torres, n-1)
        else:
            movimientos_ant = 0
            if pos > 0 and torres[pos] < torres[pos-1]:
                movimientos_ant = torres[pos-1] - torres[pos] + min_move(torres[:pos], pos-1)
        
        # Mover de la torre siguiente a la torre actual
            movimientos_sig = 0
            if pos < n-1 and torres[pos] < torres[pos+1]:
                movimientos_sig = torres[pos+1] - torres[pos] + min_move(torres[pos+1:], 0)
        
        return min(movimientos_ant, movimientos_sig)
    
    return min_move(torres, 0)



"""if __name__ == "__main__":
    number_of_cases = int(sys.stdin.readline().strip())
    for _ in range(number_of_cases):
        arreglo = list(map(int, sys.stdin.readline().split()))
        result = min_movimientos(arreglo)
        print(result)"""