def swap_elements(arr, i, j):
    """Utility function to swap elements and count the swap."""
    arr[i], arr[j] = arr[j], arr[i]
    return 1  # Count this swap

def minimumSwapsUniversal(arr, start=0):
    if len(arr) <= 1 or start >= len(arr) - 1:
        # Base cases: array is effectively sorted or single element left to consider
        return 0 
    
    # For arrays of size 2, check if a swap is needed
    if len(arr) - start == 2:
        return 1 if arr[start] < arr[start+1] else 0

    # Find the maximum element and its index
    max_value = max(arr[start:])
    max_index = arr[start:].index(max_value) + start
    
    swaps = 0
    if max_index != start:
        # Place the maximum element at the start (for descending order)
        swaps += swap_elements(arr, start, max_index)
    
    # Recursively sort the rest of the array
    swaps += minimumSwapsUniversal(arr, start + 1)
    
    return swaps

# Test cases
print(minimumSwapsUniversal([0])) # Expected: 0
print(minimumSwapsUniversal([1])) # Expected: 0
print(minimumSwapsUniversal([1,1])) # Expected: 0
print(minimumSwapsUniversal([1,2])) # Expected: 1
print(minimumSwapsUniversal([3,2,1,4]))  # Expected: 3
print(minimumSwapsUniversal([3,2,2,4]))  # Expected: 2
print(minimumSwapsUniversal([7,0,0,0,0,0,0,1]))  # Expected: 6