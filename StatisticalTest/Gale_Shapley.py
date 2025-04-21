import csv

#This code is a csv reader for the Gale-Shapley algorithm, which reads in the preferences of the 2 groups (i.e. male and female for example) within the code.
def csvReader_gale(file):
    
    #The preferenceDict is a dictionary that will hold the preferences of each individual. The key is the Individual's ID and the value is a list of their preferences.
    preferenceDict = {} 
    try:
        with open(file, 'r') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)  # Skip the header row if present
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
                print(individual2preferences.index(pair), individual2preferences.index(individual1))
                if individual2preferences.index(pair) > individual2preferences.index(individual1):
                    currentMatches[individual2] = individual1
                    available.append(pair)
                    break
                    
    # Returns a tuple of the current matches
    return list(currentMatches.items())


# Generic Stable Test 
# This function is sourced and adapted to see if the matches being made within the function are stable 
def pairs_stable(individual1, individual2, group1Pref, group2Pref):
    
    #Will be looping over the length of the first group so that all individual matches are checked
    for i in range(len(individual1)):
    
       #Using another function to get the ranking of individual 2 within individual 1's preferences
        current_pref = get_pref(individual1[i], individual2[i], group1Pref)

        #Now we will loop over the length of the 2nd group to see if there is any other individual who is preferred over the current match for individual 1.
        for j in range(len(individual2)):
            #Skipping any comparison with their current allocated match
            if i != j and get_pref(individual1[i], individual2[j], group1Pref) < current_pref:
                #Checking if both individuals prefer each other over their current matches - would mean instability present
                if get_pref(individual2[j], individual1[i], group2Pref) < get_pref(individual2[j], individual1[j], group2Pref):
                    print("Instable :", individual1[i], individual2[j])
                    return False
    return True

#Helper function that is used to get the preference ranking of the target within the actor's preference list. 
def get_pref(actor, target, preferences):
    return preferences[actor].index(target)



#Example usage
men_prefs = csvReader_gale('Male.csv')
women_prefs = csvReader_gale('Female.csv')

matches = gale_shapley(men_prefs,women_prefs)
print("Matches:", matches)

men = list(men_prefs.keys())
women = list(women_prefs.keys())

print("Stable:", pairs_stable(men, women, men_prefs, women_prefs))
