def SelectionSort(arr):
    n = len(arr)
    
    for i in range(n):
        min_index = i
        
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        
        arr[i], arr[min_index] = arr[min_index], arr[i]
    
    return arr

# Example usage:

if __name__ == "__main__":
    arr = [64, 25, 12, 22, 11]
    print("Unsorted array:", arr)
    sorted_arr = SelectionSort(arr)
    print("Sorted array:", sorted_arr)
    # Output: Sorted array: [11, 12, 22, 25, 64]