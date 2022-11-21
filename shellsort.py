def shellSort(arr, n):
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap

            arr[j] = temp
        gap =gap// 2


arr = [23, 7, 5, 0, 99, 24, 35,36]
size = len(arr)
shellSort(arr, size)
print("sorted array is")
print(arr)
    
