def quick_sort(arr):
    if len(arr) <= 1:
        return arr  # Base case: already sorted if 1 or 0 elements
    
    pivot = arr[len(arr) // 2]  # Choosing middle element as pivot
    left = [x for x in arr if x < pivot]   # Elements smaller than pivot
    middle = [x for x in arr if x == pivot]  # Elements equal to pivot
    right = [x for x in arr if x > pivot]   # Elements greater than pivot
    
    return quick_sort(left) + middle + quick_sort(right)  # Combine sorted parts

