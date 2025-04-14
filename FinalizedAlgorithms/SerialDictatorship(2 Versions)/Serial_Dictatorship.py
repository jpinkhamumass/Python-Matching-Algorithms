import Serial_Dictatorship_Reader as Serial_Dictatorship_Reader; import csv; import random; import math; import preferenceReader

# Creates a dictionary of people and their preferences
peopleArray = Serial_Dictatorship_Reader.csvReader('Pref1.csv')  

#Initialize a boolean random to be input later 
randomBoolean = "False"

def randomness():
    global randomBoolean  # Declare randomBoolean as global
    inputGetter = input("Random: True or False: ") # True or False

    if inputGetter == 'True': # Changes method to use an arbitrary order
        randomBoolean = inputGetter
        print("Successfully set to True.")
        return

    if inputGetter == 'False': # Uses the order from input
        print("Successfully set to False.")
        return

    else: # Invalid input
        print("Error: Please enter True or False: ")
        randomness()

randomness() # User determines if input order random or not

if randomBoolean == "True": 
     # This shuffler will give us the random order in which agents will choose their objects of preference
    random.shuffle(peopleArray)

# Algorithm
def output(file):
    preferenceDictionary = preferenceReader.csvReader(file)
    

    outputList = {}


    for personRow in peopleArray:
        personID = personRow[0]
        preferences = personRow[1:-1]  # Skip first (ID) and last (extra)

        for pref in preferences:
            if pref in preferenceDictionary and preferenceDictionary[pref] > 0:
                preferenceDictionary[pref] -= 1
                outputList[personID] = pref
                break  # Move to next person after assigning

    return list(outputList.items())

def printer(file): 
    print(output(file))

printer('dataItems.csv') # Prints the output of the algorithm
