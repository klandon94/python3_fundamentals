# def a():
#     return 5
# print(a())   --> should print 5

# def a():
#     return 5
# print(a()+a())  --> should print 10

# def a():
#     return 5
#     return 10
# print(a())  --> should print 5

# def a():
#     return 5
#     print(10)
# print(a())  --> should print 5

# def a():
#     print(5)
# x=a()
# print(x) --> should print 5 once

# def a(b,c):
#     print(b+c)
# print(a(1,2) + a(2,3)) --> prints 3,5 then an error saying + is unsupported

# def a(b,c):
#     return str(b) + str(c)
# print(a(2,5)) --> should print 25 

# def a():
#     b = 100
#     print(b)
#     if b < 10:
#         return 5
#     else:
#         return 10
#     return 7
# print(a) --> shouldn't print anything because function wasn't called

# def a(b,c):
#     if b<c:
#         return 7
#     else:
#         return 14
#     return 3
# print(a(2,3)) -->should print 7
# print(a(5,3)) -->should print 14
# print(a(2,3)+a(5,3)) -->should print 21

# def a(b,c):
#     return b+c
#     return 10
# print(a(3,5)) --> should print 8

# b = 500
# print(b)
# def a():
#     b = 300
#     print(b)
# print(b)
# a()
# print(b)  --> should print 500, 500, 300, 500

# b = 500
# print(b)
# def a():
#     b = 300
#     print(b)
#     return b
# print(b)
# a()
# print(b)  --> should print 500, 500, 300, 500

# b = 500
# print(b)
# def a():
#     b = 300
#     print(b)
#     return b
# print(b)
# b=a()
# print(b) --> should print 500, 500, 300, 300

# def a():
#     print(1)
#     b()
#     print(2)
# def b():
#     print(3)
# a() --> should print 1, 3, 2

# def a():
#     print(1)
#     x = b()
#     print(x)
#     return 10
# def b():
#     print(3)
#     return 5
# y = a()
# print(y) --> should print 1, 3, 5, 10