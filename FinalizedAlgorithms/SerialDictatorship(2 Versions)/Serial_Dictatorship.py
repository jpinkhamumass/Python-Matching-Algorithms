import Serial_Dictatorship_Reader as Serial_Dictatorship_Reader; import csv; import random; import math; import Item_Capacity_Reader


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



# Algorithm
def output(prefFile, itemFile):
   
    # Creates a dictionary of people and their preferences
    peopleArray = peopleArray = Serial_Dictatorship_Reader.csvReader(prefFile)

    #Initialize a boolean random to be input later 
    randomBoolean = "False"

    randomness() # User determines if input order random or not

    if randomBoolean == "True": 
    # This shuffler will give us the random order in which agents will choose their objects of preference
        random.shuffle(peopleArray)

    preferenceDictionary = Item_Capacity_Reader.csvReader(itemFile)

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

def printer(file1, file2): 
    print(output(file1, file2))

printer('Pref1.csv','dataItems.csv') # Prints the output of the algorithm
