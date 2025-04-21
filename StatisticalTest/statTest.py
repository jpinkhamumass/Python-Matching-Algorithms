import Probabilistic_Serial, Serial_Dictatorship_Reader, Item_Capacity_Reader, csv, random, Gale_Shapley, time

import matplotlib.pyplot as plt


def statTestPSR(file_path1, file_path2):

    utilityPointCounter = 0 #This counter is made to make our utilit graph. We are appointing 3 points for getting 1st choice and 2 points for getting 2nd choice. All other allocations are 0 points. 
    
    counter = 0
    agent_counter = 0
    for count in range(1,1001):
        preferences = Probabilistic_Serial.read_agent_preferences(file_path1)
        results = Probabilistic_Serial.probabilistic_serial(file_path1, file_path2)


        for agent in results:
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

            if temp_agent_choice == temp_list[0]:
                utilityPointCounter += 3
            elif temp_agent_choice == temp_list[1]:
                utilityPointCounter += 1
            

            else:
                continue
        

    return ((counter/1000)/(agent_counter/1000)) * 100, utilityPointCounter/1000

def statTestSerialDict(prefFile,itemFile):
    
    utilityPointCounter = 0 #This counter is made to make our utilit graph. We are appointing 3 points for getting 1st choice and 2 points for getting 2nd choice. All other allocations are 0 points. 
    counter = 0
    agent_counter = 0

    for count in range(1,1001):

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
       
        for agent in results:
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

            if temp_agent_choice == temp_list[0]:
                utilityPointCounter += 3
            elif temp_agent_choice == temp_list[1]:
                utilityPointCounter += 1
            else:
                continue

    return ((counter/1000)/(agent_counter/1000)) * 100, utilityPointCounter/1000

def statTestRandomSerialDict(prefFile,itemFile):
    utilityPointCounter = 0 #This counter is made to make our utilit graph. We are appointing 3 points for getting 1st choice and 2 points for getting 2nd choice. All other allocations are 0 points. 
    counter = 0
    agent_counter = 0

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
       
        for agent in results:
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

            if temp_agent_choice == temp_list[0]:
                utilityPointCounter += 3
            
            elif temp_agent_choice == temp_list[1]:
                utilityPointCounter += 1
            
            else:
                continue

    return ((counter/1000)/(agent_counter/1000)) * 100, utilityPointCounter/1000

def statTestGS(prefGroup1,prefGroup2):
    
    utilityPointCounter = 0 #This counter is made to make our utilit graph. We are appointing 3 points for getting 1st choice and 2 points for getting 2nd choice. All other allocations are 0 points. 
    counter = 0
    agent_counter = 0
    
    for count in range(1,1001):
    
        men_prefs = Gale_Shapley.csvReader_gale(prefGroup1)
        women_prefs = Gale_Shapley.csvReader_gale(prefGroup2)

        matches = Gale_Shapley.gale_shapley(men_prefs,women_prefs)
       

        for agent in matches:
            agent_counter += 2
            agentGroup2 = agent[0]
            
            agentGroup1 = agent[1]
          


            temp_list1 = []
        
            tempy = women_prefs[agentGroup2]
            temp_list1.append(tempy[0])
            temp_list1.append(tempy[1])
            temp_list1.append(tempy[2])
        
            
            if agentGroup1 in temp_list1:
                counter += 1
            
            if agentGroup1 == temp_list1[0]:
                utilityPointCounter += 3
            
            elif agentGroup1 == temp_list1[1]:
                utilityPointCounter += 1
        

            temp_list2 = []

            tempy2 = men_prefs[agentGroup1]
            temp_list2.append(tempy2[0])
            temp_list2.append(tempy2[1])
            temp_list2.append(tempy2[2])
            

            if agentGroup2 in temp_list2:
                counter += 1
            
            if agentGroup2 == temp_list2[0]:
                utilityPointCounter += 3
            
            elif agentGroup2 == temp_list2[1]:
                utilityPointCounter += 1
        
            else: 
                continue
        
        return ((counter/1000)/(agent_counter/1000)) * 100, utilityPointCounter/1000

def runTimePSR(file_path1, file_path2):
    run_time_counter = 0

    for count in range(1,1001):
        startingTime = time.time()
        
        Probabilistic_Serial.probabilistic_serial(file_path1, file_path2)
        endingTime = time.time()
        
        runTime = endingTime - startingTime
        run_time_counter += runTime
    
    return run_time_counter/ 1000

def runTimeSD(prefFile,itemFile):
    run_time_counter = 0

    for count in range(1,1001):
        startTime = time.time()
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
        endTime = time.time()
        runTime = endTime - startTime
        run_time_counter += runTime
    
    return run_time_counter/ 1000

def runTimeRSD(prefFile, itemFile):
    run_time_counter = 0

    for count in range(1,1001):
        startTime = time.time()
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
        endTime = time.time()
        runTime = endTime - startTime
        run_time_counter += runTime
    
    return run_time_counter/ 1000

def runTimeGS(prefGroup1, prefGroup2):
    time_counter = 0
    for count in range(1,1001):

        startTime = time.time()
    
        men_prefs = Gale_Shapley.csvReader_gale(prefGroup1)
        women_prefs = Gale_Shapley.csvReader_gale(prefGroup2)

        matches = Gale_Shapley.gale_shapley(men_prefs,women_prefs)

        endTime = time.time()
        runTime = endTime - startTime
        time_counter += runTime
    return time_counter/ 1000


percentagePSR = statTestPSR('Pref1.csv', 'dataItems.csv')[0]
utilityPSR = statTestPSR('Pref1.csv', 'dataItems.csv')[1]


percentageSD = statTestSerialDict('Pref1.csv','dataitems.csv')[0]
utilitySD = statTestSerialDict('Pref1.csv','dataitems.csv')[1]


percentageRSD = statTestRandomSerialDict('Pref1.csv','dataitems.csv')[0]
utilityRSD = statTestRandomSerialDict('Pref1.csv','dataitems.csv')[1]


percentageGS = statTestGS('Male1.csv','Female1.csv')[0]
utilityGS = statTestGS('Male1.csv','Female1.csv')[1]

#print(f'The results show that PSR has a % of {percentagePSR}, SD has a % of {percentageSD}, RSD has a % of {percentageRSD}, and GS has a % of {percentageGS}.')

timePSR = runTimePSR('Pref1.csv', 'dataItems.csv')

timeSD = runTimeSD('Pref1.csv','dataitems.csv')

timeRSD = runTimeRSD('Pref1.csv','dataitems.csv')

timeGS =runTimeGS('Male1.csv','Female1.csv')

# print(timeSD)
# print(timeRSD)
# print(timePSR)
# print(timeGS)


percentageData = [percentagePSR, percentageSD, percentageRSD, percentageGS]
utilityData = [utilityPSR, utilitySD, utilityRSD, utilityGS]
timeData = [timePSR, timeSD, timeRSD, timeGS]
labels = ['PSR', 'SD', 'RSD', 'GS']

fig, axs = plt.subplots(2, 1, figsize=(8, 10))

axs[1].barh(labels, percentageData, alpha=0.5, color='maroon')
for i, value in enumerate(percentageData):
    axs[1].text(value, i, f'{value:.2f}%', va='center', fontsize=8)
axs[1].set_xlabel('Percentage')
axs[1].set_ylabel('Algorithms')
axs[1].set_title('Percentage of Each Agent Getting Their Top 3 Choices')
axs[1].set_xlim(0, max(percentageData) + 10)


axs[0].barh(labels, utilityData, alpha=0.5, color='maroon')
for i, value in enumerate(utilityData):
    axs[0].text(value, i, f'{value:.2f}', va='center', fontsize=8)
axs[0].set_xlabel('Avg. Total Utility of Each Algorithm: 3 Points for 1st Choice, 1 Point for 2nd Choice')
axs[0].set_ylabel('Algorithms')
axs[0].set_title('Utility of Each Algorithm')
axs[0].set_xlim(0, max(utilityData) + 10)

plt.tight_layout()
plt.show()
