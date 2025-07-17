def MergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        MergeSort(L)
        MergeSort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1

            else:
                arr[k] = R[j]
                j += 1
                
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

    return arr

# Example usage:
if __name__ == "__main__":
    arr = [38, 27, 43, 3, 9, 82, 10]
    print("Unsorted array:", arr)
    sorted_arr = MergeSort(arr)
    print("Sorted array:", sorted_arr)
    # Output: Sorted array: [3, 9, 10, 27, 38, 43, 82]