def beCheerful(name='', repeat=1):
    print(f"good morning {name}!\n"*repeat)

beCheerful(repeat=3, name="kl")
beCheerful()



import random

def randInt(min=0, max=100):
    return int(min+random.random()*(max-min+1))

print(randInt(50))
