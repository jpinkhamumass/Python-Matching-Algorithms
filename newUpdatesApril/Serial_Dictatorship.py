import Matching_Algorithms; import csv; import random; import math; import Preference_Base

# Creates a dictionary of people and their preferences
peopleDictionary = Matching_Algorithms.csvReader('people.csv')

#Initialize a boolean random to be input later 
randomBoolean = "False"

def randomness():
    global randomBoolean  # Declare randomBoolean as global
    inputGetter = input("Random: True or False: ") # True or False

    if inputGetter == 'True': # Changes method to use an arbitrary order
        randomBoolean = inputGetter
        print("successfully set to True.")
        return

    if inputGetter == 'False': # Uses the order from input
        print("successfully set to False.")
        return

    else: # Invalid input
        print("Error: Please enter True or False: ")
        randomness()

count = len(peopleDictionary) # Number of people in input

def iDNumberListMaker(peopleDictionary): # Makes a list of people ID's
    IDNumberList = []
    for person in peopleDictionary.keys():
        IDNumberList.append(person)
    return IDNumberList

iDNumberList = iDNumberListMaker(peopleDictionary) # Makes a list of people ID's from input

randomness() # User determines if input order random or not



if randomBoolean == "True": 
     # This shuffler will give us the random order in which agents will choose their objects of preference
    random.shuffle(iDNumberList)



#Algorithm 
def output(file):

    preferenceDictionary = Preference_Base.csvReader(file) 
    outputList = {}

    for i in iDNumberList: # per person
        personOfInterest = peopleDictionary[i].preferences.values() # gets persons preferences
        for j in personOfInterest: # per preference
            if preferenceDictionary[j] > 0: # preference still has avaiability
                preferenceDictionary[j] -= 1 # decrements number of items that can be allocated
                peopleDictionary[i].actualMatch = j # updates match
                outputList[peopleDictionary[i].IDNumber] = j # updates output list
                break
            else:
                continue

    return list(outputList.items())

def printer(file): 
    print(output(file))

printer('preferences.csv')

# for key, value in outputList.items():
#     print(f'{key} : {value}')

# for i in iDNumberList:
#     print(i)
#     print(peopleDictionary[i].preferences.values())
#     print(peopleDictionary[i].actualMatch)



# To Do
# 1. Make a new csv format file with items and number of times in can be allocated - added it to CS396 Format of CSV
# 2. Make a dictionary of items and number of times it can be allocated
    # kw = Preference, value = number of times it can be allocated - made Preference_Base.py which takes the csv and makes this dictionary
# 3. Make Algorithm
    # Use Ordered List Either Unshuffled or Shuffled
    # For Each Person:
        # Check to see if preference is available
        # Yes: Decrement, Allocate
        # No: Go to next preference

# 4. Return Preferences In Some Way
