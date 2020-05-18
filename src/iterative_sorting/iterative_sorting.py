# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here
        for j in range(i +1, len(arr)):
            if arr[smallest_index] > arr[j]: 
                smallest_index = j

        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]
    

        # TO-DO: swap
        # Your code here

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code here
    swaps = True
    while swaps == True: 
        swaps = False
        for i in range(1, len(arr)): 
            
            if arr[i]< arr[i-1]: 
                arr[i], arr[i-1] = arr[i - 1], arr[i]
                swaps = True

    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):
    # Your code here


    return arr
