import pickle
import json
import random
from random import randint

# import test data
n = open('data/names.json').read()
names = json.loads(n)
a = open('data/addresses.json').read()
addresses = json.loads(a)


# generate some entries
for n in range(10):
    # full name
    name = random.choice(names).capitalize()
    surname = random.choice(names).capitalize()
    # address
    address = random.choice(addresses)
     # phone number
    n = 10
    range_start = 10**(n-1)
    range_end = (10**n)-1
    phone = randint(range_start, range_end)
    print("Name: {:20} Surname: {:20} Phone: {:<20} Address: {}".format(name, surname, phone, address))




# PIK = "pickle.dat"

# data = ["A", "b", "C", "d"]

# with open(PIK, "wb") as f:
#     pickle.dump(data, f)

# with open(PIK, "rb") as f:
#     print(pickle.load(f))

# def addUsers():
#     for i range(10):
#         print()