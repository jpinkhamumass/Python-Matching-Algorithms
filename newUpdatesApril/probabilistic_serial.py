import csv
import random

def probabilisitc_serial(agent_preferences, items_list):
    assignments_dict = {agent: {item: 0.0 for item in items_list} for agent in agent_preferences}
    item_counter = {item: 0 for item in items_list}
    total_agents = len(agent_preferences)
  

    while any(item_counter[item] < total_agents for item in items_list):
        for agent, preferences in agent_preferences.items():
            for item in preferences:
                if item_counter[item] < total_agents:
                    assignments_dict[agent][item] += 1
                    item_counter[item] += 1
                    break

    for agent in assignments_dict:
        for item in items_list:
            assignments_dict[agent][item] /= total_agents
    
    
    #lottery for the actual allocations based on the fractions 
    # print (assignments_dict)

    output_dict = {}
    for agent in assignments_dict:
        for item in items_list:
            if random.random() < assignments_dict[agent][item]:
                assignments_dict[agent][item] = 1
                output_dict[agent] = item
            else:
                assignments_dict[agent][item] = 0
                
            
    return list(output_dict.items())

# Example usage
agent_preferences = {
    "A": ["X", "Y", "Z"],
    "B": ["Y", "X", "Z"],
    "C": ["Z", "X", "Y"]
}

items_list = ["X", "Y", "Z"]

allocation = probabilisitc_serial(agent_preferences, items_list)
print(allocation)
