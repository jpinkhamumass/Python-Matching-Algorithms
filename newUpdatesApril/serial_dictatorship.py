import Matching_Algorithms; import csv; import random; import math; import Preference_Base

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



#Algorithm 
def output(file):

    preferenceDictionary = Preference_Base.csvReader(file)
    outputList = {}

    for i in iDNumberList:
        personOfInterest = peopleDictionary[i].preferences.values()
        for j in personOfInterest:
            if preferenceDictionary[j] > 0:
                preferenceDictionary[j] -= 1
                peopleDictionary[i].actualMatch = j
                outputList[peopleDictionary[i].IDNumber] = j
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
