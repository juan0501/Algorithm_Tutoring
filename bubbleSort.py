def bubble_sort(arr, n):
    for i in range(n-1, 0):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
