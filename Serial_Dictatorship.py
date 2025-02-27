import Matching_Algorithms; import csv; import random; import math

peopleDictionary = Matching_Algorithms.csvReader('people.csv')

randomBoolean = "False"

def randomness():
    global randomBoolean  # Declare randomBoolean as global
    inputGetter = input("Random: True or False: ") # True or False

    if inputGetter == 'True':
        randomBoolean = inputGetter
        print("successfully set to True.")
        return

    if inputGetter == 'False':
        print("successfully set to False.")
        return

    else:
        print("Error: Please enter True or False: ")
        randomness()

def count(peopleDictionary):
    count = 0
    for person in peopleDictionary.keys():
            count += 1
    return count

def iDNumberListMaker(peopleDictionary):
    IDNumberList = []
    for person in peopleDictionary.keys():
        IDNumberList.append(person)
    return IDNumberList

iDNumberList = iDNumberListMaker(peopleDictionary)

randomness()



if randomBoolean == "True":
     # This shuffler will give us the random order in which agents will choose their objects of preference
    random.shuffle(iDNumberList)

for i in iDNumberList:
    print(i)

# To Do
# 1. Make a new csv format file with items and number of times in can be allocated
# 2. Make a dictionary of items and number of times it can be allocated
    # kw = Preference, value = number of times it can be allocated
# 3. Make Algorithm
    # Use Ordered List Either Unshuffled or Shuffled
    # For Each Person:
        # Check to see if preference is available
        # Yes: Decrement, Allocate
        # No: Go to next preference

# 4. Return Preferences In Some Way