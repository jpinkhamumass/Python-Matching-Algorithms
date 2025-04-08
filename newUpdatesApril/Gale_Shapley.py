import csv

#This code is a csv reader for the Gale-Shapley algorithm, which reads in the male and female preferences within the code.
def csvReader_gale(file):
    #The preferenceDict is a dictionary that will hold the preferences of each individual. The key is the Individual's ID and the value is a list of their preferences.
    preferenceDict = {} 
    try:
        with open(file, 'r') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                IndividualID = row[0]
                individualPreferences = row[1:]
                preferenceDict[IndividualID] = individualPreferences
    except FileNotFoundError:
        print(f"Error: The file {file} was not found or does not have the proper formatting.")
    
    return preferenceDict



#This code implements the Gale-Shapley algorithm, which is a method for finding a stable matching between two equally sized sets of elements given an ordering of preferences for each element.
#The function takes 2 dictionaries as input, one for each group of individuals. The reader will convert the csv file into a dictionary. 

def gale_shapley(prefGroup1, prefGroup2):
    available = list(prefGroup1.keys())
    currentMatches = {}

    # While there are still unmatched individuals, this loop will continue to work so all individuals/agents are matched
    while available: 
       # The first individual in the available list is selected
       # and their preferences are retrieved from the preference dictionary
        individual1 = available.pop(0)
        individual1preferences = prefGroup1[individual1]


        # The preferences of the first individual are iterated through. 
        # Individual 2 represents the preference agents of individual 1.
        for individual2 in individual1preferences:

            #This line retrieves the preferences of individual 2 from their preference dictionary
            # The pair variable is used to check if individual2

            individual2preferences = prefGroup2[individual2]
            pair = currentMatches.get(individual2)

            # If individual2 is not currently matched, they are matched with individual1
            if pair == None:
                currentMatches[individual2] = individual1
                break

            # If individual2 is already matched, check if they prefer individual1/new agent over their current match
            elif pair != None:
                if individual2preferences.index(pair) > individual2preferences.index(individual1):
                    currentMatches[individual2] = individual1
                    available.append(pair)
                    break
    # Returns a tuple of the current matches
    return list(currentMatches.items())


# Generic Stable Test 
# This function is sourced and adapted to see if the matches being made within the function are stable 
def pairs_stable(men, women, men_prefs, women_prefs):
    for i in range(len(men)):
        current_pref = get_pref(men[i], women[i], men_prefs)
        for j in range(len(women)):
            if i != j and get_pref(men[i], women[j], men_prefs) < current_pref:
                if get_pref(women[j], men[i], women_prefs) < get_pref(women[j], men[j], women_prefs):
                    print("Instable :", men[i], women[j])
                    return False
    return True

def get_pref(actor, target, preferences):
    return preferences[actor].index(target)


#Examples using all the function and specific CSVs

men_preferences = csvReader_gale('men_preferences.csv')
women_preferences = csvReader_gale('women_preferences.csv')

matches = gale_shapley(men_preferences, women_preferences)
print("Matches:", matches)

# Derived men and women lists from preference dictionaries
men = list(men_preferences.keys())
women = list(women_preferences.keys())

is_stable = pairs_stable(men, women, men_preferences, women_preferences)
print("Is stable:", is_stable)

