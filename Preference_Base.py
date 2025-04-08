import csv


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

#debugging, added a bunch of tests to see if the function works
    except FileNotFoundError:
        print(f'Error: {fname} not found.')
        return None
    except PermissionError:
        print(f'Error: Permission denied for {fname}.')
        return None
    except Exception as e:
        print(f'Error occurred: {e}')
        return None

# Prints the preference dictionary for test purposes
def printPreferenceDict(preference_dict):
    if not preference_dict:
        print("The dictionary is empty or None.")
        return

    print("\n--- Preference Dictionary ---")
    for key, value in preference_dict.items():
        print(f'Item: {key}, Number of Times: {value}')
    print("\n")

# Test
readPreference = csvReader('preferences.csv')
printPreferenceDict(readPreference)