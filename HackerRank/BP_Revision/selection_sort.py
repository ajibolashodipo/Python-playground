def selection_sort(arr):
    for i in range(0, len(arr)):
        min_idx = i

        # check for smallest digit in unsorted section of array
        for j in range(i, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
                
        # after smallest digit is found,check for whether min changed; then make the swap
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
        print(arr)

    return arr


print(selection_sort([7,6,9,3,5,6,2,8,5,1]))