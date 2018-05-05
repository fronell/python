import csv
import pprint

pp = pprint.PrettyPrinter(indent = 2)

def write_csv_from_object():
    print("[==== write_csv_from_object ====]")
    # For the object, the header values must match the same case used by the
    # object variables.  We can't use title case for example because the 
    # object variables are all lowercase
    header = ("year", "make", "model")
    cars = []
    
    class Vehicle(object): 
        
        def __init__(self, make="NA", model="NA", year="NA"):
            self.make  = make
            self.model = model
            self.year  = year

    with open('in.csv') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=",")
        for row in reader:
            cars.append(Vehicle(row['Make'], row['Model'], row['Year']))

    with open("out_object.csv", "w") as csvfile:
        writer = csv.DictWriter(csvfile, 
                                delimiter=",", 
                                lineterminator="\n", 
                                fieldnames=header)
        
        writer.writeheader()
        for car in cars:
            writer.writerow(car.__dict__)
    
    new_header = ("year", "make")
            
    with open("out_object_new_header.csv", "w") as csvfile:
        writer = csv.DictWriter(csvfile, 
                                delimiter=",", 
                                lineterminator="\n", 
                                fieldnames=new_header)
        
        writer.writeheader()
        for car in cars:
            # An alternative method to create a dictionary from the object
            # attributes.  The difference between this and __dict__ is __dict__
            # will return all attributes of the object while this method only
            # adds the attributes we specify in the header.  If we passed in
            # car.__dict__, the following error would occur:
            # ValueError: dict contains fields not in fieldnames: 'model'
            # csv is picky and requires the dictionary we pass in to have the
            # exact fields we specify in the header
            # Here is another way to do it but is harder to understand:
            # Reference: http://stackoverflow.com/questions/7053551/python-valueerror-too-many-values-to-unpack
            #row = {key: value for key, value in inv[key].__dict__.iteritems()
            #       if key in columns}
            row = {}
            for column in new_header:
                row[column] = getattr(car, column)
            writer.writerow(row)

def write_csv_from_dict():
    print("[==== write_csv_from_dict ====]")
    header = ("year", "make", "model")
    # Creates a new array from Vehicle.header with each field name capitalized.
    # Threw it in here as a reference
    header = [x.title() for x in header]
    cars = []

    with open('in.csv') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=",")
        for row in reader:
            cars.append(row)

    # Sort cars by year in descending order
    sorted_cars = sorted(cars, key=lambda d: d['Year'], reverse=True)

    with open("out_dict.csv", "w") as csvfile:
        writer = csv.DictWriter(csvfile, 
                                delimiter=",", 
                                lineterminator="\n", 
                                fieldnames=header)
        
        writer.writeheader()
        writer.writerows(sorted_cars)
            
write_csv_from_dict()
write_csv_from_object()
