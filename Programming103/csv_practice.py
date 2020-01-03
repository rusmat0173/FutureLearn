""" Practice on csv files, using the coffee_shop.csv file, created in Excel.
    Most sources say the best way to deal with large csv files is to use pandas,
    which will print out easy to follow tables

"""

import csv

# compare this to the one immediately below. Here the next method is used to separate the header
with open('coffee_shop.csv') as csvfile:
    my_data = csv.reader(csvfile, dialect='excel', delimiter=',')
    header = next(my_data)
    print(header)
    print("= = = ")
    for row in my_data:
        print(row)

print("= = = =")
# compare this to the one immediately above. Here the there is no next method and header is just another row
with open('coffee_shop.csv') as csvfile:
    my_data = csv.reader(csvfile, dialect='excel', delimiter=',')
    for row in my_data:
        print(row)

# use of writerow method. MUST use newline = '', otherwise Python 3 adds an extra line!
row = ['Coffee Zone', '4', 'Cheam']
with open('coffee_shop.csv', 'a', newline='') as csvFile:
    my_data = csv.writer(csvFile)
    my_data.writerow(row)

# there's also the DictReader method, used a lot in the Rice data analysis course
# you'll see it turns it into a very pesky ordered dictionary
with open('coffee_shop.csv') as csvfile:
    my_data = csv.DictReader(csvfile, dialect='excel', delimiter=',')
    for row in my_data:
        print(row)
        print(row.items(), row.keys(), row.values())
