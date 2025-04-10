import csv
import os
from typing import List, Optional

# Reads CSV file and returns a list of lists representing rows in the file.
def csvReader(fname):
    try:
        with open(fname, 'r') as fil:
            reader = csv.reader(fil)
            headers = next(reader, None)  # Read headers, if present

            if headers is None:
                print(f"Error: The file '{fname}' is empty.")
                return None

            pplArray = []  # List of lists

            # Create a list of rows
            for row in reader:
                pplArray.append(row)

            return pplArray

    except FileNotFoundError:
        print(f"Error: The file '{fname}' was not found.")
        return None
    except IOError as e:
        print(f"Error: An I/O error occurred while reading '{fname}': {e}")
        return None

# Prints people for test purposes
def printPeopleArray(peopleArray):
    for person in peopleArray:
        print(person)

# Test
readPeople = csvReader('people.csv')  # Ensure the file name includes the .csv extension
printPeopleArray(readPeople)


