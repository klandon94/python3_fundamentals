# Bubble sort -- repeatedly steps through the list to be sorted, compares each pair of adjacent items and swaps them if they are in the wrong order

arr = [9,2,17,5,-3,99,22]

def bubble_sort(arr):
    for j in range(len(arr)-1):
        for i in range(len(arr)-1-j):
            if arr[i+1]<arr[i]:
                arr[i],arr[i+1] = arr[i+1],arr[i]
    return arr

print(bubble_sort(arr))


# Selection sort -- repeatedly finding the minimum element (considering ascending order) from unsorted part and putting it at the beginning. Maintains two subarrays in a given array

arr = [3,9,2,4,5,22,17]

def selection_sort(arr):
    for x in range(len(arr)):
        min_dex = x
        for i in range(min_dex,len(arr)):
            if arr[i]<arr[min_dex]:
                min_dex = i
        arr[x],arr[min_dex] = arr[min_dex],arr[x]
    return arr

print(selection_sort(arr))


# Insertion sort - Loop over positions in the array, starting with index 1. Each new position must be inserted into the correct place in the sorted subarray to the left of that position

arr = [5,6,3,1,8,7,2,4]

def insertion_sort(arr):
    for x in range(1, len(arr)):
        temp = arr[x]
        i = x - 1
        while i>=0 and arr[i]>temp:
            arr[i+1] = arr[i]
            i -= 1
        arr[i+1] = temp
    return arr

print (insertion_sort(arr))


