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
parser.add_argument('--filePath', '-p', type=str, default='data/data', required=False, help='Path to save the file (without extension). Default "data/data"')
parser.add_argument('--format', '-f', choices=['pk', 'hd5', 'sql'], default='pk', required=True, help='pk: pickle file format, hd5 or SQL. Note: sql populates an SQLite DB which can be accessed through a web page: http://127.0.0.1:8000/ [ It requires django server to be active]')
args = parser.parse_args()

# Instance the serializer type and utils
suffix = args.format
if suffix == 'pk': #pickle ff
    app = alSerializer.PickleSerializer()
elif suffix == 'hd5': # hdf5
    app = alSerializer.Hdf5Serializer()
elif suffix == 'sql':
    print('SQL starts here ....')
    app =  alSerializer.djSerializer()
    

# generate some user test data
testSize = args.testDataSize
utils = alUtils.Utilities()
users = utils.generateTestData(testSize)
for user in users:
    print("Generating user ->\t{}".format(user))

# add extension to file 
fName = args.filePath
fName = fName + '.' + suffix

# serialize data into a file
app.toFile(users, fName)

"""
# read the data back and spit it out
data = app.fromFile(fName)

# for user in data:
for user in data:
    print("Reading from file ->\t{}".format(user))
"""