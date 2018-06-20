# Create a function that accepts a number as an input and return a new array that counts down by one from the number
def countdown(x):
    arr = []
    for i in range(x, -1, -1):
        arr.append(i)
    return arr
print(countdown(5))

# Given an array with two numbers, print the first value and return the second
def print_return(arr):
    print(arr[0])
    return arr[1]
print(print_return([3,9]))

# Given an array, return the sum of the first value in the array plus the array's length
def first_plus_length(arr):
    return arr[0] + len(arr)
print(first_plus_length([3,9,2,4]))

#Given an array, return a new array with the array values that are greater than its 2nd value. Print how many values this is. If the array is only 1 element long, return False
def val_greater_than_2nd(arr):
    count = 0
    arr2 = []
    if len(arr) == 1:
        return False
    for x in arr:
        if x > arr[1]:
            arr2.append(x)
            count += 1
    print(count)
    return arr2
print(val_greater_than_2nd([3,2,9,10]))

#Given 2 numbers, return array of length num1 with each value num2. Print "Jinx!" if they are the same
def thislen(x,y):
    arr = []
    if x == y:
        print('Jinx!')
    for i in range(x):
        arr.append(y)
        i+=1
    return arr
print(thislen(2,4))
