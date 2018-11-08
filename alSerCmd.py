"""
This script is command line tool which shows how to serialize personal data (name, address, phone number).
Usage from cmd line: alSerCmd.py --help
For issues contact me at: diegotrazzi@gmail.com
"""
import argparse
import alSerializer
import alUtils

parser = argparse.ArgumentParser(description='User Serializer.', epilog='For support or feedback email diegotrazzi@gmail.com')
parser.add_argument('--testDataSize', '-t', type=int, default=5, required=False, help='Test the serializer with random users. Specify the batch size, default 50')
parser.add_argument('--filePath', '-f', type=str, default='data/pickle.dat', required=False, help='File path to save the file. Default "data/pickle.dat"')
args = parser.parse_args()

# instance the serializer and utils
app = alSerializer.Serializer()
utils = alUtils.Utilities()
# generate some user test data
testSize = args.testDataSize
users = utils.generateTestData(testSize)
for user in users:
    print("Generating user ->\t{}".format(user))
# serialize data into a pickle file
fName = args.filePath
app.toFile(users, fName)
# read the data back and spit it out
data = app.fromFile(fName)
for user in data:
    print("Reading from file ->\t{}".format(user))