import Probabilistic_Serial, Serial_Dictatorship_Reader, Item_Capacity_Reader, csv, random


def statTestPSR(file_path1, file_path2):

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
            else:
                continue

    return ((counter/1000)/(agent_counter/1000)) * 100


def statTestSerialDict(prefFile,itemFile):
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
            else:
                continue

    return ((counter/1000)/(agent_counter/1000)) * 100


def statTestRandomSerialDict(prefFile,itemFile):
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
            else:
                continue

    return ((counter/1000)/(agent_counter/1000)) * 100




resultsPSR = statTestPSR('Pref1.csv', 'dataItems.csv')
# print(resultsPSR)


resultsSD = statTestSerialDict('Pref1.csv','dataitems.csv')
# print(resultsSD)

resultsRSD = statTestRandomSerialDict('Pref1.csv','dataitems.csv')
# print(resultsRSD)

print(f'The results show that PSR has a % of {resultsPSR}, SD had a % of {resultsSD} and RSD had a % of {resultsRSD}.')
