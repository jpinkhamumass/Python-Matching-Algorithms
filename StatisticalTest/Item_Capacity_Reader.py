import csv
import os

# Class to store preferences
class Preference:
    def __init__(self, Item, Number):
        self.ItemName = Item
        self.NumberOfTimes = int(Number)  # Ensure Number is an integer

# Reads CSV file and returns a dictionary of Preferences
def csvReader(fname):
    try:
        with open(fname, 'r') as fil:
            reader = csv.reader(fil)
            headers = next(reader)

            dictOfPreferences = {}

            # Create a dictionary of Preference objects
            for row in reader:
                if len(row) < 2:
                    continue  # Skip rows with insufficient columns

                Item = row[0]
                Number = row[1]
                preference = Preference(Item, Number)
                dictOfPreferences[preference.ItemName] = preference.NumberOfTimes

            return dictOfPreferences

    except FileNotFoundError:
        print(f"Error: The file '{fname}' was not found.")
        return None
