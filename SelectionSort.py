def selection_sort(arr):
    for i in range(0, len(arr) - 1):
        current_minimum = i #replace the i with a '?'
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[current_minimum]:
                current_minimum = j #replace the j with a '?'
         # they implement this, maybe keep the first variables before = sign
        temp = arr[i]
        arr[i] = arr[current_minimum]
        arr[current_minimum] = temp

arr = [2, 6, 5, 1, 3, 4]
selection_sort(arr)
print("Array after sorting:")
print(arr)