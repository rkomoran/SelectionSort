# Don't change any of the code that is here, there to fill in the question marks.
# Talk to a buddy if you can't figure it out!
def selection_sort(arr):
    for i in range(0, len(arr) - 1):
        current_minimum = ? 
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[current_minimum]:
                current_minimum = ? 
        
        temp = ?
        arr[i] = ?
        arr[current_minimum] = ?

arr = [2, 6, 5, 1, 3, 4]
selection_sort(arr)
print("Array after sorting:")
print(arr)
