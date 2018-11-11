import unittest
import alSerializer
import alUtils

class TestStringMethods(unittest.TestCase):

    def test_one(self):
        """
        Pickle serializer test
        """
        # instance the serializer and the utils
        app = alSerializer.PickleSerializer()
        utils = alUtils.Utilities()
        # generate some user test data
        testSize = 1000
        users = utils.generateTestData(testSize)
        # serialize data into a pickle file
        fName = 'data/test_pickle.dat'
        app.toFile(users, fName)
        # read the data back and spit it out
        data = app.fromFile(fName)
        # compare cached to serialized data
        for cUser, sUser in zip(users,data):
            print("Cached user ->\t\t{}".format(cUser))
            print("Serialized user ->\t{}".format(sUser))
            self.assertEqual(str(cUser), str(sUser))
            print("-----------------------")

if __name__ == '__main__':
    unittest.main()