# Simple Code to open the file so we can start working with it wtih simple error messages
try:
    f = open('lgas16.csv')
    print('file loaded')
except(IOError):
    print('file not found')

# Capturing and splitting the data that we need
line = f.readline()
titles = line.split(',')

# This while loop will parse the entire document until it reaches the end
print('INSERT INTO LGA (lga_number, lga_code, lga_name, lga_type, area_sqKM, latitude, longitude) ')
print('VALUES')
num_index = 1
while f.readline() is not None:

    line = f.readline()
    data = line.split(',')

    lga_code = data[0]
    lga_name = data[1]
    lga_type = data[2]
    area_sqKM = data[3]
    latitude = data[4]
    longitude = data[5]

    # This print stataement generates the SQL magic that we need

    print('({}, {}, "{}", "{}", {}, {}, {}), '
    .format(num_index, lga_code, lga_name, lga_type, area_sqKM, latitude, longitude))

    num_index += 1


