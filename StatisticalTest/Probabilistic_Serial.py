import csv
import collections
import random

#This is a reader to read the agent preferences from the template csv format. 
# It will make a library with the agent ID as the key and the preferences (list) as the value
def read_agent_preferences(file_path):
    agent_preferences = {}
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        headers = next(reader)  # Skip the header row
        for row in reader:
            agent_id = row[0]
            preferences = row[1:11]  # Keep preferences as strings (can be numbers or letters)
            agent_preferences[agent_id] = preferences
    return agent_preferences

#Similar structure to the reader function above, but this one reads the items and their capacities.
def read_items_list(file_path):
    item_capacities = {}
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        headers = next(reader)  # Skip the header row
        for row in reader:
            item = row[0]
            capacity = int(row[1])
            item_capacities[item] = capacity
    return item_capacities


#Probabilistic Serial Algorithm

def probabilistic_serial(preferences_path,items_path):

    agent_preferences = read_agent_preferences(preferences_path)
    item_capacities = read_items_list(items_path)
    
    #Making a copy of the item capacities from the reader function. This tells us how much of an items is left for "consumption"
    remaining_capacity = item_capacities.copy()

    #Initializing the assignments dictionary with 0.0 for each item. We use 0.0 for each item to indicidate that no agent has been assigned to it yet.
    # The number will represent the fraction of the item assigned to the agent.
    assignments = {agent: {item: 0.0 for item in item_capacities} for agent in agent_preferences}

    #Agent pointer is a way to keep track of which item each agent is currently looking at in their preference list.
    #It is initialized to 0 for each agent, meaning they are all looking at the first item in their preference list.
    agent_tracker = {agent: 0 for agent in agent_preferences}

    
    # This main loop will continue to go through until all items are fully consumed. By checking if any item has capacity greater than 0, we ensure the eating algorithm works properly.
    # CapacityBool is a boolean that checks for the capacities, and is the switch for when the while loop stops. 
    capacityBool = any(itemCapacity > 0 for itemCapacity in remaining_capacity.values())

    while capacityBool:

        #Made a dictionary which is defaulted to 0. This will be used to count how many agents are eating each item.
        item_eating_counter = collections.defaultdict(int)

        #This loop goes through each agent and their preferences. It checks if the current item they are looking at has capacity left. If it does, it increments the counter for that item.
        for agent, prefs in agent_preferences.items():
            #Looping through preference list of each agent
            while agent_tracker[agent] < len(prefs):
                #Checking if current item has capacity left and then incrementing the counter
                #If the item is not available, we move to the next item in the preference list.
                current_item = prefs[agent_tracker[agent]]
                if remaining_capacity[current_item] > 0:
                    item_eating_counter[current_item] += 1
                    break
                else:
                    #If the item is not available, we move to the next item in the preference list by incrementing this tracker.
                    agent_tracker[agent] += 1

        if not item_eating_counter:
            break


        #min_time is a baseline of time which must be done to make sure all agents are "eating" for the same period of time; no advantages, etc.

        min_time = float("inf") #checks how long agents can eat current items before atleast one of the items is fully consumed/runs out

        #This loop goes through each item and checks how many agents are eating it. It calculates the time it would take for that item to be fully consumed by the agents eating it.
        for item, num_of_agents in item_eating_counter.items():
            if num_of_agents > 0:
                time_to_finish = remaining_capacity[item] / num_of_agents

                #tracking minimum time needed to finish eating/consuming an item. This updated the infinity, which was preset just in case of a extreme case. 
                min_time = min(min_time, time_to_finish)



        for agent, prefs in agent_preferences.items():
            if agent_tracker[agent] < len(prefs):
                current_item = prefs[agent_tracker[agent]]
                if remaining_capacity[current_item] > 0:

                    #share represents how much of the current item each agent gets. In a specific time period, each agent gets a share of the item based on how many agents are eating it.
                    share = min_time

                    #updates the assignments dictionary with the share of the item assigned to the agent for fractional assignment. Also decrements capacity of the item. 
                    assignments[agent][current_item] += share
                    remaining_capacity[current_item] -= share

                    #We had issues of some fractions being very close to 0 but not 0, so this will make sure all such numbers are treated as 0 for simplicity. 
                    if remaining_capacity[current_item] <= 1e-6:
                        remaining_capacity[current_item] = 0


    #Dictionary that will be outputted with the final assignments.
    final_assignment = {}

    #Keeps track of what is remaining for each item in terms of quantity that can be allocated.
    remaining_slots = item_capacities.copy()

    # Randomize agent order to make lottery fair with less order bias.
    agents = list(assignments.keys())
    random.shuffle(agents)

    for agent in agents:

        # Sort items by descending probability
        # This will be a dictionary of items and their probabilities for the agent.
        item_probability = assignments[agent]
        items = list(item_probability.items())
        
        items.sort(key=lambda x: -x[1])  # Sort items by descending probability

        # Assign the item with the highest probability that is still available
        for item, prob in items:
            if remaining_slots[item] > 0 and prob > 0:
                final_assignment[agent] = item
                remaining_slots[item] -= 1
                break
    

    # Check for unassigned agents and items
    # Unassigned agents are those who did not get assigned any item based on their fractional assignment.
    unassigned_agents = []
    unassigned_items = []

    #These next 2 for loops will make a list of all unassigned agents, and also will accumulate all unassigned items and how much of the items are present. 
    for agent in agents:
        if agent not in final_assignment:
            unassigned_agents.append(agent)

    for items, remainder_cap in remaining_slots.items():
        if remainder_cap > 0:
            unassigned_items.extend([item] * int(round(remainder_cap)))

    #Assignments are done, and items are randomly chosen for unassigned agents. This ensures that some level of first-come first-serve bias is not present. 
    for agent in unassigned_agents:
        final_assignment[agent] = random.choice(unassigned_items) if unassigned_items else None


    return list(final_assignment.items())


# Example usage
assignments = probabilistic_serial('Pref1.csv', 'dataItems.csv')
print(assignments)
