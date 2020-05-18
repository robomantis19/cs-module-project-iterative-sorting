def linear_search(arr, target):
    # Your code here
    for i in arr: 
        if i is target: 
            return arr.index(i)
        


    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    print((len(arr) -1)//2)
    if (len(arr))//2:
        mid = len(arr)//2
        left = (len(arr)-1)//2
        right = (len(arr)+1)//2
        if target == arr[mid]:
            return mid
        if arr[left] < arr[mid]: 
            arr[mid], arr[left] = arr[left], arr[mid]
        elif arr[right]> arr[mid]: 
            arr[mid], arr[right] = arr[right], arr[mid]
        return binary_search(arr[:mid], target)

      # not found
