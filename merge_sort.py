def merge_sort(arr):
    if len(arr) <= 1:
        return arr  # Base case: return if array has 1 or 0 elements

    mid = len(arr) // 2  # Find the middle index
    left_half = merge_sort(arr[:mid])  # Recursively sort the left half
    right_half = merge_sort(arr[mid:])  # Recursively sort the right half

    return merge(left_half, right_half)  # Merge sorted halves

def merge(left, right):
    sorted_arr = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_arr.append(left[i])
            i += 1
        else:
            sorted_arr.append(right[j])
            j += 1

    # Append remaining elements, if any
    sorted_arr.extend(left[i:])
    sorted_arr.extend(right[j:])

    return sorted_arr


arr=[]
print(merge_sort(arr))
