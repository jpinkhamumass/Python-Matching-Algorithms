import csv
import random
import Gale_Shapley

#We will be importing the same csv reader as the Gale-Shapley algorithm. The goal of the reader is to convert the preferences and number of each item csvs into a usable list.


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
preferences_file = 'men_preferences.csv'  # Replace with your actual preferences CSV file path
items_file = 'prob_items.csv'  # Replace with your actual items CSV file path

preferences = Gale_Shapley.csvReader_gale(preferences_file)
items = Gale_Shapley.csvReader_gale(items_file)
allocation_result = probabilisitc_serial(preferences, items)
print(allocation_result)
