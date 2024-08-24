def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def quickSort(arr):
    if len(arr) <= 1:
        return arr
    else:
        return quickSort([x for x in arr[1:] if x < arr[0]]) + arr[0:1] + quickSort([x for x in arr[1:] if x >= arr[0]])