import csv

# people class maker
class Person:
    def __init__(self, IDNumber, lastName, firstName, actualMatch, **kwargs):
        self.IDNumber = IDNumber 
        self.lastName = lastName
        self.firstName = firstName
        self.actualMatch = actualMatch
        self.preferences = kwargs # dictionary of preferences
        
        

    def actualMatchSetter(actualMatch):
        self.actualMatch = actualMatch

# reads CSV file and returns a dictionary of Person objects, 
# Each IDNumber is stored as the key and the person object is stored as the value.
def csvReader(fname):
    try:
       with open(f'{fname}', 'r') as fil:
            reader = csv.reader(fil)
            headers = next(reader)

            dictOfPeople = {}
           
            # otherwise, create a list of People objects
            for row in reader:
                IDNumber = row[0]
                lastName = row[1]
                firstName = row[2]
                actualMatch = row[3]
                preferences = {f"Preference {i+1}": row[i+4] for i in range(len(row[4:]))}
                person= Person(IDNumber, lastName, firstName, actualMatch, **preferences)
                dictOfPeople[IDNumber] = person
            
            return dictOfPeople

    except:
        print(f'Error occurred when opening {fname} to read')
        return None

# prints people for test purposes
def printPeopleDict(people_dict):
    if not people_dict:
        print("The dictionary is empty or None.")
        return

    print("\n--- People Dictionary ---")
    for ID, person in people_dict.items():
        print(f"ID: {ID}")
        print(f"  Name: {person.firstName} {person.lastName}")
        print(f"  Actual Match: {person.actualMatch}")
        print(f"  Preferences:")
        for key, value in person.preferences.items():
            print(f"    {key}: {value}")
        print("-" * 30)  # Separator for readability

# test
readPeople = csvReader('people.csv')
printPeopleDict(readPeople)
    

