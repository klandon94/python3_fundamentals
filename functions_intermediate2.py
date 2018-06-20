# capitals = {'svk':'Bratislava', 'deu':'Berlin', 'dnk':'Copenhagen'}

# capitals['abc'] = 'New country'

# for data in capitals.keys():
#     print(data)


x = [[5,2,3],[10,8,9]]
x[1][0] = 15
print(x)

students = [{'first_name':'Michael', 'last_name':'Jordan'},{'first_name':'John', 'last_name':'Rosales'}]
students[0]['last_name'] = 'Bryant' 
print(students)

sports_directory = {'basketball': ['Kobe', 'Jordan', 'James', 'Curry'], 'soccer': ['Messi', 'Ronaldo', 'Rooney']}
sports_directory['soccer'][0] = 'Andres'
print(sports_directory)

z = [ {'x':10, 'y':20} ]
z[0]['y'] = 30
print(z)

# Create a function that given a list of dictionaries, it loops through each dict in the list and prints each key and the associated value
students = [
     {'first_name' : 'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
# x=list(students[0].keys())
# print(x[0])
# print(students[0].get(x[0]))

def iterateDictionary(List):
    for x in List:
        for key,val in x.items():
            print(key, '-', val, end=' , ')
        print()
iterateDictionary(students)

# def iterateDictionary(List):
#     key = list(List[0].keys())
#     for x in List:
#         print (key[0],'-',x.get(key[0]),',', key[1],'-',x.get(key[1]))
# iterateDictionary(students)

# Create a function that given a list of dictionaries and a key name, it outputs the value stored in that key for each dictionary
def iterateDictionary2(name,List):
    for x in List:
        print(x[name])
iterateDictionary2('first_name', students)
        

# Create a function that prints the name of each location and also how many locations the Dojo currently has. Have the function also print the name of each instructor and how many instructors the Dojo currently has.
dojo = {
    'location':['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors':['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def printDojoInfo(d):
    print(len(d['location']), 'LOCATIONS')
    for x in d['location']:
        print(x)
    print()
    print(len(d['instructors']), 'INSTRUCTORS')
    for x in d['instructors']:
        print(x)
printDojoInfo(dojo)