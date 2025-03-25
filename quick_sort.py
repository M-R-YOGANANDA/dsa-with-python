def partition(arr, low, high):
    pivot = arr[high]  # Choosing last element as pivot
    i = low - 1  # Pointer for smaller elements
    
    for j in range(low, high):
        if arr[j] < pivot:  # If element is smaller than pivot
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # Swap elements
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]  # Swap pivot into correct position
    return i + 1  # Return pivot index

def quick_sort_inplace(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)  # Get pivot index
        quick_sort_inplace(arr, low, pi - 1)  # Sort left subarray
        quick_sort_inplace(arr, pi + 1, high)  # Sort right subarray

