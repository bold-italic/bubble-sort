arr = [64, 34, 25, 12, 22, 11, 90, 5]

n = len(arr)
for i in range(n - 1):
    for j in range(n - i - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
print(arr)

"""If the array is almost sorted already, it will be sorted after the first run. However, the Bubble Sort algorithm 
will continue to run without swapping elements, which is unnecessary."""

arr = [7, 3, 9, 12, 11]

n = len(arr)
for i in range(n - 1):
    swapped = False
    for j in range(n - i - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            swapped = True
    if not swapped:
        break

print(arr)
