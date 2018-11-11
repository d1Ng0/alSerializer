import pickle
import json
import random
from random import randint
import os
import sys
import alUsers
from abc import ABC, abstractmethod
import pandas as pd
from djUsers import models # defines the django model to generate users on the sql server

class AbstractSerializer(ABC):
    """
    Interface for serializers. Implement these methods for any class that implements the serializer.
    """
     
    @abstractmethod
    def toFile(self): # python doesn't have overloading -> no need to specify all variables here
        pass
        
    @abstractmethod
    def fromFile(self):
        pass

class PickleSerializer(AbstractSerializer):
    """
    Class to serialize and deserialize users with pickle
    """

    def __init__(self):
        return

    def toFile(self, data, fName, encoding='wb'):
        """
        Serialize data onto a file using pickle. 
        Creates folders, if necessary
        @returns: True if successfull
        """
        try: 
            # check if file path exists, if not attempt to create
            path = os.path.split(fName)[0]
            if not os.path.exists(path):
                os.makedirs(path)
           # dump data into pickle
            with open(fName, encoding) as f:
                pickle.dump(data, f)
                return True
        except:
            raise     

    def fromFile(self, fName, encoding='rb'):
        """
        Read serialized file using pickle
        @returns: data if successfull
        """
        # reads data. no need to close the file when using 'with open'
        try:
            with open(fName, encoding) as f:
                return pickle.load(f)
        except:
            raise

class Hdf5Serializer(AbstractSerializer):
    """
    Class to serialize and deserialize users with hdf5
    In this implementation I use one table for all users. Each group contains a dataset [name, surname, number] 
    and a nested group for the address class.
    """

    def __init__(self):
        return

    def toFile(self, data, fName):
        try: 
            # check if file path exists, if not attempt to create
            path = os.path.split(fName)[0]
            if not os.path.exists(path):
                os.makedirs(path)
           # dump data into pickle
            df = pd.DataFrame()
            columns = ['name', 'surname', 'phone','address']
            for index, user in enumerate(data):
                name = user.get_name()
                surname = user.get_surname()
                phone = user.get_phone()
                address = user.get_address()
                df_entry = pd.DataFrame([[name,surname,phone,address]], index=[index], columns=columns)
                df = df.append(df_entry)
            # write to file
            hdf = pd.HDFStore(fName, mode='w')
            hdf.put('USERS', df, data_columns=True)
            hdf.close()
            return True
        except:
            raise  

    def fromFile(self, fName):
        try:
            users = []
            hdf = pd.HDFStore(fName, mode='r')
            users_df = hdf.get('/USERS')
            # data needs to be converted back into objects
            for index, row in users_df.iterrows():
                address = alUsers.Address()
                address = address.address_from_string(str(row[3]))
                user = alUsers.User(str(row[0]), str(row[1]), str(row[2]), str(address))
                # add to list
                users.append(user)
            hdf.close()
            return users
        except:
            raise

class djSerializer(AbstractSerializer):
    """
    Class to serialize and deserialize users onto an SQLite DB. 
    This database is dynamically populated and can be access form the a local web host: http://127.0.0.1:8000/
    This solution requires an SQLite database, an active server (running either on local host or online).
    The data can be manipulated dynamically and refreshed in real time onto a front-end html-page
    """

    def __init__(self):
        return

    def toFile(self, data, fName):
        print('TO FILE STARTS HERE')
        """
        try: 
            # check if file path exists, if not attempt to create
            path = os.path.split(fName)[0]
            if not os.path.exists(path):
                os.makedirs(path)
           # dump data into pickle
            df = pd.DataFrame()
            columns = ['name', 'surname', 'phone','address']
            for index, user in enumerate(data):
                name = user.get_name()
                surname = user.get_surname()
                phone = user.get_phone()
                address = user.get_address()
                df_entry = pd.DataFrame([[name,surname,phone,address]], index=[index], columns=columns)
                df = df.append(df_entry)
            # write to file
            hdf = pd.HDFStore(fName, mode='w')
            hdf.put('USERS', df, data_columns=True)
            hdf.close()
            return True
        except:
            raise  
        """

    def fromFile(self, fName):
        print('from file')
        """
        try:
            users = []
            hdf = pd.HDFStore(fName, mode='r')
            users_df = hdf.get('/USERS')
            # data needs to be converted back into objects
            for index, row in users_df.iterrows():
                address = alUsers.Address()
                address = address.address_from_string(str(row[3]))
                user = alUsers.User(str(row[0]), str(row[1]), str(row[2]), str(address))
                # add to list
                users.append(user)
            hdf.close()
            return users
        except:
            raise
        """

