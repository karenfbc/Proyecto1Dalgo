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
            if torres[pos] < torres[pos+1]:
                if torres[pos-1]-torres[pos+1]>0:
                    torres[pos-1] -=1
                    torres[pos] +=1
                    minMov=min(minMov,1+min_move(torres,pos))
                else:
                    torres[pos+1] -=1
                    torres[pos] +=1
                    minMov=min(minMov,1+min_move(torres,pos))
            else:
                minMov=min(minMov,min_move(torres,pos-1)) 
        return minMov
    if n == 1:
        return 0
    elif n == 2:
        if torres[0]< torres[1]:
            return (torres[1]-torres[0])//2
        else:
            return 0
    else:
            return min_move(torres, n)
    

# Test cases
print(min_movimientos([0])) # Expected: 0
print(min_movimientos([1])) # Expected: 0
print(min_movimientos([1,1])) # Expected: 0
print(min_movimientos([1,2])) # Expected: 1
print(min_movimientos([3,2,1,4]))  # Expected: 3
print(min_movimientos([3,2,2,4]))  # Expected: 2
print(min_movimientos([7,0,0,0,0,0,0,1]))  # Expected: 6

"""if __name__ == "__main__":
    number_of_cases = int(sys.stdin.readline().strip())
    for _ in range(number_of_cases):
        arreglo = list(map(int, sys.stdin.readline().split()))
        result = min_movimientos(arreglo)
        print(result)"""