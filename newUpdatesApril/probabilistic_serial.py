import csv
import random
import Gale_Shapley

#We will be importing the same csv reader as the Gale-Shapley algorithm. 
# The goal of the reader is to convert the preferences and number of each item csvs into a usable list.



def probabilisitc_serial(agent_preferences, items_list):
    #This initializes a dictionary to hold the assignments of each agent to each item. 
    # The dictionary is initialized with a 0.0 probability for each item for each agent. The probabilities of each items for each agent will change as the algorithm progresses. 
    assignments_dict = {agent: {item: 0.0 for item in items_list} for agent in agent_preferences}

    #This initializes a counter to keep track of how many agents have been assigned to each item.
    item_counter = {item: 0 for item in items_list}

    #Need to keep track of the number of agents in the system to make sure the fractions for the probability are computed properly.
    total_agents = len(agent_preferences)
  

    #This loop will continue to work until all agents have a fraction of 1.0 for each item. 
    # This fraction represents the probability of each agent being assigned to each item.
    while any(item_counter[item] < total_agents for item in items_list):

        #This loop iterates through each agent and their preferences.
        for agent, preferences in agent_preferences.items():

            #This loop iterates through each item in the agent's preferences.
            #If the item has not been assigned to all agents, the agent is assigned to the item and the counter for that item is incremented.
            #The fraction for that item is also incremented by 1.0/total_agents later on.

            for item in preferences:
                if item_counter[item] < total_agents:
                    assignments_dict[agent][item] += 1
                    item_counter[item] += 1
                    break

    
    #This is dividing the how many agents have been assigned to each item by the total number of agents.
    # This creates a probability for each agent being assigned to each item.
    # This is done to ensure that the probabilities are normalized and sum to 1 for each agent.
    for agent in assignments_dict:
        for item in items_list:
            assignments_dict[agent][item] /= total_agents
    
    
    #Lottery for the actual allocations based on the fractions previously computed.

    output_dict = {} # This will store the final assignments of agents to items.


    #This loop iterates through each agent and their preferences, to check the probability and create final assignments of items.
    for agent in assignments_dict:
        for item in items_list: 

            #random.random() computes a random float between 0.0 and 1.0
            #If the random number is less than the fraction for that item, the agent is assigned to that item.
            #If the agent is assigned to the item, the fraction for that item is set to 1.0 and the item is added to the output dictionary.
            if random.random() < assignments_dict[agent][item]: 
                assignments_dict[agent][item] = 1
                output_dict[agent] = item
            else:
                assignments_dict[agent][item] = 0
    
    # Returning a list of tuples, for the final assingments           
    return list(output_dict.items())



# Example usage using the Gale-Shapley reader and specific test case files
preferences_file = 'men_preferences.csv'  # Replace with your actual preferences CSV file path
items_file = 'prob_items.csv'  # Replace with your actual items CSV file path

preferences = Gale_Shapley.csvReader_gale(preferences_file)
items = Gale_Shapley.csvReader_gale(items_file)
allocation_result = probabilisitc_serial(preferences, items)
print(allocation_result)
