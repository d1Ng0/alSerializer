import pickle
import json
import random
from random import randint
import os
import sys
import alUsers

class Utilities():
    """
    Utility Class. Methods that are used by multiple classes and don't fit in any other place
    """

    def __init__(self):
        return

    def generateTestData(self, test_size=10):
        """
        Helper method to generate some test User Objects 
        @returns: a list of users
        """
        # import test data
        n = self.fileOpen('data/names.json')
        names = json.loads(n)
        a = self.fileOpen('data/addresses.json')
        addresses = json.loads(a)

        # generate some entries
        users = []
        for n in range(test_size):
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
            # print("Name: {:20} Surname: {:20} Phone: {:<20} Address: {}".format(name, surname, phone, address))
            # create user entry
            user = alUsers.User(name, surname, phone, address)
            # add to list
            users.append(user)
        return users

    def fileOpen(self, fName):
        """
        Utility to open files. Checks the file exists for IO errors and if file exists
        @returns: file data
        """
        if os.path.exists(fName):
            with open(fName) as f:
                try:
                    return f.read()
                except IOError: # whatever reader error
                    print("Unable to open file: {}".format(fName))
                    sys.exit(1)
        else:
            print("Filename {} doesn't exist".format(fName))
            sys.exit(1)