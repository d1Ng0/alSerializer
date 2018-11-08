import pickle
import json
import random
from random import randint
import os
import sys
import alUsers
from abc import ABC, abstractmethod

class AbstractSerializer(ABC):
    """
    Interface for serializers. Implement these methods for any class that implements the serializer.
    """
     
    @abstractmethod
    def toFile(self):
        pass
        
    @abstractmethod
    def fromFile(self):
        pass

class Serializer(AbstractSerializer):
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

