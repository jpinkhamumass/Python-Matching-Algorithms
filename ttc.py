import csv
from Matching_Algorithms import csvReader

people = Matching_Algorithms.csvReader('people.csv')
preferences = Preference_Base.csvReader('preferences.csv')

def top_trading_cycles(peopleDict, preferencesDict):
    unassigned = set(peopleDict.keys())
    matchResult = []

    while unassigned:
        visited = set()
        current_path = []
        curr = next(iter(unassigned))

        while curr in unassigned and currrent not in visited:
            visited.add(current)
            current_path.append(current)

            top_preference = None
            for pref in peopleDict[current].preferences:
                if pref in unassigned:
                    top_preference = pref
                    break
            if top_preference is None:
                #print(f"{peopleDict.firstName} {peopleDict.lastName} has no top preference")
                break

            curr = top_preference
        
        #cycle
        if curr in visited:
            cycle_index = current_path.index(curr)
            cycle = current_path[cycle_index:]

            for i in range(len(cycle)):
                agent = cycle[i]
                #assign the next resource in the cycle
                resource = cycle[(i + 1) % len(cycle)]
                #update outcome
                peopleDict[agent].actualMatch = resource
                unassigned.remove(agent)
                
                personName = f"{peopleDict.firstName} {peopleDict.lastName}
                match_result.append([personName, resource])

                
                #change output format
                #returns list of person, number, preference, number
                #giverName = f"{peopleDict[giver].firstName} {peopleDict[giver].lastName}"
                #receiverName = f"{peopleDict[receiver].firstName} {peopleDict[receiver].lastName}"
                #match_result.append((giver, giverName, receiver, receiverName))
    
    return match_result
    
    
    #outputMatches = {}
    #while peopleDict:
        



#def ttc(all):
    #num_agents = len(all)
