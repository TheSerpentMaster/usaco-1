def InsertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
            
        arr[j + 1] = key
    
    return arr

# Example usage:

if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6]
    print("Unsorted array:", arr)
    sorted_arr = InsertionSort(arr)
    print("Sorted array:", sorted_arr)
    # Output: Sorted array: [5, 6, 11, 12, 13]