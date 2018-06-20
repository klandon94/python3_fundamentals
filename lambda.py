def square(num):
    return num*num
square(3)

#Lambda is used to specify an anonymous (nameless) function, useful where function only needs to be used once and convenient as arguments to functions that require functions as parameters

#Lambda can be an element in a list:
y = ['test_string', 99, lambda x: x ** 2]
print(y[2])
print(y[2](5))

#Lambda can be passed to another function as a callback:
def invoker(callback):
    print(callback(2))
invoker(lambda x: 2*x)
invoker(lambda y: 5+y)

#Lambda can be stored in a variable:
add10 = lambda x: x+10
print(add10(2))

#Returned by another function
def incrementor(num):
    return(lambda x: num + x)
incrementor(3)


def map(list, function):
    for i in range(len(list)):
        list[i]=function(list[i])
    return list

print (map([1,2,3,4], (lambda num:num*num)))