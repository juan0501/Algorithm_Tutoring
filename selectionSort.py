def selection_sort(arr, n):
    for i in range(n-1):
        least = i
        for j in range(i+1, n):
            if arr[j] < arr[least]:
                least = j
        arr[i], arr[least] = arr[least], arr[i]
