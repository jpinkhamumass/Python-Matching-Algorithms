import Matching_Algorithms; import csv; import random; import math; import Preference_Base

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

    return currentMatches


#Generic Stable Test 

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


men_preferences = {
    'A': ['X', 'Y', 'Z'],
    'B': ['Y', 'X', 'Z'],
    'C': ['X', 'Z', 'Y']
}

women_preferences = {
    'X': ['B', 'A', 'C'],
    'Y': ['A', 'B', 'C'],
    'Z': ['A', 'C', 'B']
}

matches = gale_shapley(men_preferences, women_preferences)
print("Matches:", matches)

men = ['A', 'B', 'C']
women = ['X', 'Y', 'Z']

is_stable = pairs_stable(men, women, men_preferences, women_preferences)
print("Is stable:", is_stable)
