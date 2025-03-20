def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]  # Swap the elements
                swapped = True
        if not swapped:
            break  # If no elements were swapped, the array is already sorted
    return arr

arr=[]
print(bubble_sort(arr))
