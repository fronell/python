import csv
import pprint

pp = pprint.PrettyPrinter(indent = 2)

#### Using Objects ####
class Vehicle(object): 
    
    header = ("year", "make", "model")
    
    def __init__(self, make="Chevy", model="Tahoe", year="1984"):
        self.make  = make
        self.model = model
        self.year  = year

cars = []
car1 = Vehicle()
cars.append(car1)
car2 = Vehicle("Dodge", "Ram", "1977")
cars.append(car2)

print(",".join(Vehicle.header).title())

def write_csv_from_object():
    # Creates a new array from Vehicle.header with each field name capitalized
    # but won't work with writer.writeheader() because it'll then try to 
    # access the attributes using the capitalized form
    #header = [x.title() for x in Vehicle.header]
    with open("out_object.csv", "w") as csvfile:
        writer = csv.DictWriter(csvfile, 
                                delimiter=",", 
                                lineterminator="\n", 
                                fieldnames=Vehicle.header)
        
        writer.writeheader()
        for car in cars:
            # An alternative method to create a dictionary from the object
            # attributes.  The difference between this and __dict__ is __dict__
            # will return all attributes of the object while this method only
            # adds the attributes we specify in Vehicle.header
            #row = {}
            #for column in Vehicle.header:
            #    row[column] = getattr(car, column)
            #print(row)
            writer.writerow(car.__dict__)
            
write_csv_from_object()

#### Using Dictionaries ####

header = ("Year", "Make", "Model")
cars = []
#cars.append({'Make': "Chevy", 'Model': "Tahoe", 'Year': "1984"})
#cars.append({'Make': "Dodge", 'Model': "Ram", 'Year': "1977"})

with open('in.csv') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=",")
    for row in reader:
        cars.append(row)

pp.pprint(cars)
sorted_cars = sorted(cars, key=lambda d: d['Year'], reverse=False)
pp.pprint(sorted_cars)

def write_csv_from_dict():
    with open("out_dict.csv", "w") as csvfile:
        writer = csv.DictWriter(csvfile, 
                                delimiter=",", 
                                lineterminator="\n", 
                                fieldnames=header)
        
        writer.writeheader()
        writer.writerows(sorted_cars)
            
write_csv_from_dict()
