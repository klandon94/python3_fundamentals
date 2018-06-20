# 1) Given an array, write a function that changes all positive numbers in the array to 'big' and returns the same array
def makeItBig(arr):
    for x in range(len(arr)):
        if arr[x] > 0:
            arr[x] = 'big'
    return arr
print(makeItBig([-1,3,5,-5]))

# 2) Given an array of numbers, create a function to replace last value with number of positive values. Return the array
def countPositives(arr):
    count = 0
    for x in arr:
        if x > 0:
            count+=1
    arr[len(arr)-1] = count
    return arr
print(countPositives([-1,1,1,1]))

# 3) Given an array, return the sum of all values in the array
def sumTotal(arr):
    sum = 0
    for x in arr:
        sum+=x
    return sum
print(sumTotal([1,2,3,4]))

# 4) Given an array, return the average of all values in the array
def average(arr):
    sum = 0
    for x in arr:
        sum+=x
    return sum/len(arr)
print(average([1,2,3,4]))

# 5) Given an array, return the length of the array
def length(arr):
    return len(arr)
print(length([1,2,3,4]))

# 6) Given an array, return the minimum value in the array
def minimum(arr):
    min = arr[0]
    for x in arr:
        if x < min:
            min = x
    return min
print(minimum([1,2,3,4]))

# 7) Given an array, return the maximum value in the array
def maximum(arr):
    max = arr[0]
    for x in arr:
        if x > max:
            max = x
    return max
print(maximum([1,2,3,4]))

# 8) Given an array, return a dictionary that has the sumTotal, average, minimum, maximum and length of the array
def ultimate_analyze(arr):
    return {'total':sumTotal(arr), 'avg':average(arr), 'min':minimum(arr), 'max':maximum(arr), 'len':length(arr)}
print(ultimate_analyze([5,10,9,3]))

#9) Given an array, return an array in a reversed order 
def reverse(arr):
    length = len(arr)
    for x in range(len(arr)//2):
        arr[x],arr[length-1]=arr[length-1],arr[x]
        length -= 1
    return arr
print(reverse([1,2,3,4]))
