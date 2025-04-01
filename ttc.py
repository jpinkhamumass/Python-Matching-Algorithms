import csv
from Matching_Algorithms import csvReader

people = Matching_Algorithms.csvReader('people.csv')
preferences = Preference_Base.csvReader('preferences.csv')

def top_trading_cycles(people_dict):
  unmatched = set(people_dict.keys())
  matchings = {} #final matching results

  while unmatched: # match everyone to their top choice, if taken move to next available choice
    proposals = {}
    for person_id in unmatched:
      person = people_dict[person_id]
      for pref in person.preferences.values():
        if pref in unmatched: #can only propose to a unmatched person
          proposals[person_id] = pref
          break

    #cycles
    visited = set()
    cycles = []

    for start in proposals:
      if start in visited: #skips if part of a cycle already
        continue
      cycle = []
      current = start

      #finding cycles
      while current not in visited:
        visited.add(current)
        cycle.append(current)
        current = proposals.get(current) #moving down the chain
        if current is None or current not in proposals:
          break #stop when someone didnt propose
        if current in cycle:
          #cycle created
          cycle = cycle[cycle.index(current):]
          cycles.append(cycle)
          break #end of cycle

    #assigning matches
    for cycle in cycles:
      for i in range(leng(cycle)):
        giver = cycle[i]
        receiver = cycle[(i + 1) % len(cycle)] #next person in cycle
        people_dict[giver].actualMatch = receiver #assigning the match
        matchings[giver] = receiever
      unmatched -= set(cycle) # removes people who are matched

  return matchings
