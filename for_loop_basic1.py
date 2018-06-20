#Basic - print all numbers from 0 to 150
for i in range(151):
    print(i)

#Multiples of five - print all multiples of 5 from 5 to 1,000,000
for i in range(5,1000001,5):
    print(i)

#Counting, the Dojo Way - print integers 1 to 100. If divisible by 5, print "Coding" instead. If by 10, also print "Dojo"
for i in range(1, 21):
    if i%5 == 0:
        print('Coding', end=' ')
        if i%10 == 0:
            print('Dojo')
        print()
    else:
        print(i)

#Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum
sum = 0
for i in range(500000):
    if i%2 == 1:
        sum+=i
print(sum)

#Countdown by Fours - Print positive numbers starting at 2018,  counting down by fours (exclude 0)
for i in range(2018,1,-4):
    print(i)

#Flexible Countdown - given lowNum, highNum, mult, print multiples of mult from lowNum to highNum, using for loop. i.e for (2,9,3) print 3 6 9
def flex(low,high,mult):
    for i in range(low,high+1):
        if i % mult == 0:
            print(i)
flex(2,9,3)

