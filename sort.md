# QuickSort
```python
def quick_sort(array):
    if len(array) <= 1:
        return array

    pivot = array[len(array) // 2]
    left = [el for el in array if el < pivot]
    middle = [el for el in array if el == pivot]
    right = [el for el in array if el > pivot]

    return left + middle + right
```
## in-place quick sort
```python
def quicksort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        left = quicksort(arr, low, pivot_index - 1)
        right = quicksort(arr, pivot_index + 1, high)

    return arr

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1
```

## 短い方は再帰して、長い方は末尾再帰最適化
```python
def quicksort(arr, low, high):
    while low < high:
        pivot_index = partition(arr, low, high)
        if pivot_index - low < high - pivot_index:
            quicksort(arr, low, pivot_index - 1)
            low = pivot_index + 1
        else:
            quicksort(arr, pivot_index + 1, high)
            high = pivot_index - 1
    return arr

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1
```


