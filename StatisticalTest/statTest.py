import Probabilistic_Serial, Serial_Dictatorship_Reader, Item_Capacity_Reader, csv, random, Gale_Shapley, time

import matplotlib.pyplot as plt


#need a seperate reader for psr stat test to make sure we can extract top 3 choices for each agent.
def reader_psr1(file_path):
    with open(file_path, mode='r') as file:
        reader = csv.reader(file)
    
        pref_dict = {}
        # Iterate through each row in the CSV
        headers = next(reader)  # Read headers
        for row in reader:

            pref_list = []
            
            # Get the student's preferences and assigned group
            first = row[1]
            second = row[2]
            third = row[3]
            name = row[0]

            pref_list.append(first)
            pref_list.append(second)
            pref_list.append(third)
            pref_dict[name] = pref_list
    return pref_dict

def reader_psr2(file_path):
    with open(file_path, mode='r') as file:
        reader = csv.reader(file)
    
        pref_dict = {}
        # Iterate through each row in the CSV
        headers = next(reader)  # Read headers
        for row in reader:

            pref_list = []
            
            # Get the student's preferences and assigned group
            first = row[1]
            second = row[2]
            third = row[3]
            fourth = row[4]
            fifth = row[5]
            sixth = row[6]
            seventh = row[7]
            eighth = row[8]
            ninth = row[9]
            tenth = row[10]
            name = row[0]

            pref_list.append(first)
            pref_list.append(second)
            pref_list.append(third)
            pref_list.append(fourth)
            pref_list.append(fifth)
            pref_list.append(sixth)
            pref_list.append(seventh)
            pref_list.append(eighth)
            pref_list.append(ninth)
            pref_list.append(tenth)
            pref_dict[name] = pref_list
    return pref_dict


# print(reader_psr2('Pref1.csv'))


def statTestPSR(file_path1, file_path2):

    referencePrefs = reader_psr1(file_path1)

    utilityPrefs = reader_psr2(file_path1)

    utilityList = [] #All utility values for all agents in this list. The minimum valie will be the utility of the worst agent, and the maximum will be the utility of the best agent.
    #Whole point of utilityList is to get the minimum utility value to represent egalitarian welfare.

    #Utility will work on a decreasing scale. Getting choice 1 will be 10 points, choice 2 will be 9 points, and so on. Lowest utility will be 1 point for choice 10.
    
    probabilityPointCounter = 0

    agent_counter = 0
    
    preferences = Probabilistic_Serial.read_agent_preferences(file_path1)
    results = Probabilistic_Serial.probabilistic_serial(file_path1, file_path2)


  
    for agent, items in results.items():
        agent_counter += 1

        for item, fraction in items.items():

            if item in referencePrefs[agent]:
                probabilityPointCounter += fraction

    for agentName, dictList in results.items():
        utility = 0
        
        for item, fraction in dictList.items():
            if item in utilityPrefs[agentName]:
                if item == utilityPrefs[agentName][0]:
                    utility += 10 * fraction
                elif item == utilityPrefs[agentName][1]:
                    utility += 9 * fraction
                elif item == utilityPrefs[agentName][2]:
                    utility += 8 * fraction
                elif item == utilityPrefs[agentName][3]:
                    utility += 7 * fraction
                elif item == utilityPrefs[agentName][4]:
                    utility += 6 * fraction
                elif item == utilityPrefs[agentName][5]:
                    utility += 5 * fraction
                elif item == utilityPrefs[agentName][6]:
                    utility += 4 * fraction
                elif item == utilityPrefs[agentName][7]:
                    utility += 3 * fraction
                elif item == utilityPrefs[agentName][8]:
                    utility += 2 * fraction
                elif item == utilityPrefs[agentName][9]:
                    utility += 1 * fraction

        utilityList.append(utility)
   
    return (probabilityPointCounter/agent_counter) * 100, min(utilityList)


def statTestSerialDict(prefFile,itemFile):
    
    counter = 0
    agent_counter = 0

   

        # Creates a dictionary of people and their preferences
    peopleArray = Serial_Dictatorship_Reader.csvReader(prefFile)

    preferenceDictionary = Item_Capacity_Reader.csvReader(itemFile)

    outputList = {}

    for personRow in peopleArray:
        personID = personRow[0]
        preferences = personRow[1:-1]  # Skip first (ID) and last (extra)

        for pref in preferences:
            if pref in preferenceDictionary and preferenceDictionary[pref] > 0:
                preferenceDictionary[pref] -= 1
                outputList[personID] = pref
                break  # Move to next person after assigning



    results = list(outputList.items())
    preferences = Probabilistic_Serial.read_agent_preferences(prefFile)
    

    finalEgalitarian = [] #List to store all utility values for all agents, we will take minimum from this point.

    for agent in results:
        utilityPointCounter = 0
        agent_counter += 1
        temp_agent = agent[0]
        temp_agent_choice = agent[1]


        temp_list = []
    
        tempy = preferences[temp_agent]
        temp_list.append(tempy[0])
        temp_list.append(tempy[1])
        temp_list.append(tempy[2])

        if temp_agent_choice in temp_list:
            counter += 1


        #Utility will work on a decreasing scale. Getting choice 1 will be 10 points, choice 2 will be 9 points, and so on. Lowest utility will be 1 point for choice 10.

        
        temp = preferences[temp_agent]
        utility_List = []
        
        for temp_item in temp:
            utility_List.append(temp_item)

        if temp_agent_choice == utility_List[0]:
            utilityPointCounter += 10
        elif temp_agent_choice == utility_List[1]:
            utilityPointCounter += 9
        elif temp_agent_choice == utility_List[2]:
            utilityPointCounter += 8
        elif temp_agent_choice == utility_List[3]:
            utilityPointCounter += 7
        elif temp_agent_choice == utility_List[4]:
            utilityPointCounter += 6
        elif temp_agent_choice == utility_List[5]:
            utilityPointCounter += 5
        elif temp_agent_choice == utility_List[6]:
            utilityPointCounter += 4
        elif temp_agent_choice == utility_List[7]:
            utilityPointCounter += 3
        elif temp_agent_choice == utility_List[8]:
            utilityPointCounter += 2
        elif temp_agent_choice == utility_List[9]:
            utilityPointCounter += 1
        
        finalEgalitarian.append(utilityPointCounter)

    return ((counter/1000)/(agent_counter/1000)) * 100, min(finalEgalitarian)

def statTestRandomSerialDict(prefFile,itemFile):
    counter = 0
    agent_counter = 0
    finalEgalitarian = [] #List to store all utility values for all agents, we will take minimum from this point.

    for count in range(1,1001):

         # Creates a dictionary of people and their preferences
        peopleArray = Serial_Dictatorship_Reader.csvReader(prefFile)

        random.shuffle(peopleArray)

        preferenceDictionary = Item_Capacity_Reader.csvReader(itemFile)

        outputList = {}

        for personRow in peopleArray:
            personID = personRow[0]
            preferences = personRow[1:-1]  # Skip first (ID) and last (extra)

            for pref in preferences:
                if pref in preferenceDictionary and preferenceDictionary[pref] > 0:
                    preferenceDictionary[pref] -= 1
                    outputList[personID] = pref
                    break  # Move to next person after assigning

    

        results = list(outputList.items())
        preferences = Probabilistic_Serial.read_agent_preferences(prefFile)
       
        

        tempEgalList = []
        
        for agent in results:
            utilityPointCounter = 0
            agent_counter += 1
            temp_agent = agent[0]
            temp_agent_choice = agent[1]


            temp_list = []
        
            tempy = preferences[temp_agent]
            temp_list.append(tempy[0])
            temp_list.append(tempy[1])
            temp_list.append(tempy[2])

            if temp_agent_choice in temp_list:
                counter += 1


            #Utility will work on a decreasing scale. Getting choice 1 will be 10 points, choice 2 will be 9 points, and so on. Lowest utility will be 1 point for choice 10.

            
            temp = preferences[temp_agent]
            utility_List = []
    
            
            for temp_item in temp:
                utility_List.append(temp_item)

            if temp_agent_choice == utility_List[0]:
                utilityPointCounter += 10
            elif temp_agent_choice == utility_List[1]:
                utilityPointCounter += 9
            elif temp_agent_choice == utility_List[2]:
                utilityPointCounter += 8
            elif temp_agent_choice == utility_List[3]:
                utilityPointCounter += 7
            elif temp_agent_choice == utility_List[4]:
                utilityPointCounter += 6
            elif temp_agent_choice == utility_List[5]:
                utilityPointCounter += 5
            elif temp_agent_choice == utility_List[6]:
                utilityPointCounter += 4
            elif temp_agent_choice == utility_List[7]:
                utilityPointCounter += 3
            elif temp_agent_choice == utility_List[8]:
                utilityPointCounter += 2
            elif temp_agent_choice == utility_List[9]:
                utilityPointCounter += 1

            tempEgalList.append(utilityPointCounter)
        
        finalEgalitarian.append(min(tempEgalList))
            

    return ((counter/1000)/(agent_counter/1000)) * 100, min(finalEgalitarian)



percentagePSR = statTestPSR('Pref1.csv', 'dataItems.csv')[0]
print(percentagePSR)
utilityPSR = statTestPSR('Pref1.csv', 'dataItems.csv')[1]
print(utilityPSR)


percentageSD = statTestSerialDict('Pref1.csv','dataitems.csv')[0]
utilitySD = statTestSerialDict('Pref1.csv','dataitems.csv')[1]
print(percentageSD)
print(utilitySD)


percentageRSD = statTestRandomSerialDict('Pref1.csv','dataitems.csv')[0]
utilityRSD = statTestRandomSerialDict('Pref1.csv','dataitems.csv')[1]
print(percentageRSD)
print(utilityRSD)



percentageData = [percentagePSR, percentageSD, percentageRSD]
utilityData = [utilityPSR, utilitySD, utilityRSD]
labels = ['PSR', 'SD', 'RSD',]

fig, axs = plt.subplots(2, 1, figsize=(8, 10))

axs[1].barh(labels, percentageData, alpha=0.5, color=['red', 'blue', 'green', 'orange'])
for i, value in enumerate(percentageData):
    axs[1].text(value, i, f'{value:.2f}%', va='center', fontsize=8)
axs[1].set_xlabel('Probability as Percentage')
axs[1].set_ylabel('Algorithms')
axs[1].set_title('Avg. Agent Probability of Getting Top 3 Choice')
axs[1].set_xlim(0, max(percentageData) + 10)


axs[0].barh(labels, utilityData, alpha=0.5, color=['red', 'blue', 'green', 'orange'])
for i, value in enumerate(utilityData):
    axs[0].text(value, i, f'{value:.2f}', va='center', fontsize=8)
axs[0].set_xlabel('Worst-Off Agent Utility')
axs[0].set_ylabel('Algorithms')
axs[0].set_title('Egalitarian Welfare') 
axs[0].set_xlim(0, max(utilityData) + 10)

plt.tight_layout()
plt.show()
