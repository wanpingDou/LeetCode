
def heapify(arr, n, i): 
    largest = i        # 根  
    left = 2 * i + 1   # 左
    right = 2 * i + 2  # 右
    # print([i, left, right, n])
    # print([arr[i], arr[left], arr[right]])

    if left < n and arr[i] < arr[left]: 
        largest = left 
  
    if right < n and arr[largest] < arr[right]: 
        largest = right 
  
    if largest != i: 
        arr[i], arr[largest] = arr[largest], arr[i]  # 交换
        heapify(arr, n, largest) 
  
def HeapSort(arr):
    n = len(arr) 
    # Build a maxheap. 
    for i in range(n, -1, -1): 
        heapify(arr, n, i)
    print(arr)
  
    # 一个个交换元素
    for i in range(n-1, 0, -1): 
        arr[i], arr[0] = arr[0], arr[i]  # 交换
        heapify(arr, i, 0) 

if __name__ == '__main__':
    arr = [ 1,2,3,4] 
    HeapSort(arr) 
    n = len(arr) 
    print ("小根堆: ", arr) 
