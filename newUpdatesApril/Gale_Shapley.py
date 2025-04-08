import csv

def csvReader_gale(file):
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

def gale_shapley(prefGroup1, prefGroup2):
    available = list(prefGroup1.keys())
    currentMatches = {}

    while available: # While there are still unmatched individuals
       
        individual1 = available.pop(0)
        individual1preferences = prefGroup1[individual1]

        for individual2 in individual1preferences:
            individual2preferences = prefGroup2[individual2]
            pair = currentMatches.get(individual2)

            if pair == None:
                currentMatches[individual2] = individual1
                break

            elif pair != None:
                if individual2preferences.index(pair) > individual2preferences.index(individual1):
                    currentMatches[individual2] = individual1
                    available.append(pair)
                    break

    return list(currentMatches.items())


# Generic Stable Test 
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

men_preferences = csvReader_gale('men_preferences.csv')
women_preferences = csvReader_gale('women_preferences.csv')

matches = gale_shapley(men_preferences, women_preferences)
print("Matches:", matches)

# Derived men and women lists from preference dictionaries
men = list(men_preferences.keys())
women = list(women_preferences.keys())

is_stable = pairs_stable(men, women, men_preferences, women_preferences)
print("Is stable:", is_stable)

