import csv
from Matching_Algorithms import csvReader
people = csvReader("people.csv")

for person in people.values():
    print(person.preferences)

def hi():
    return
def ttc(all):
    num_agents = len(all)
