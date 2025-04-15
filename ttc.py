import csv

students = {}
with open('course_students.csv', 'r') as people:
  csv_reader = csv.DictReader(people)
  for row in csv_reader:
        key = row['student_id']
        students[key] = {
            'first_choice': row['first_choice'],
            'second_choice': row['second_choice'],
            'third_choice': row['third_choice'],
            'assigned_group': row['assigned_group']
        }
# print(students['0'])
# print(students.keys())

matches = students.copy()
waiting = len(students.keys())

group_to_student = {}
for sid, info in students.items():
  group = info['assigned_group']
  if group:
    group_to_student[group] = sid


final_assignment = {}

while students:
  # Step 3a: Build pointers
  pointers = {}

  # Students point to their top available choice
  for sid, info in students.items():
    for choice_key in ['first_choice', 'second_choice', 'third_choice']:
      choice = info[choice_key]
      if choice:  # skip if empty string
        pointers[sid] = choice
        break

  # Groups point to the student currently assigned to them
  for group, sid in group_to_student.items():
    if sid in students:
      pointers[group] = sid

  # Step 3b: Find a cycle
  visited = set()
  #path = []
  #node = next(iter(pointers))  # start anywhere
  #edits
  cycle_found = False
  
  for start in pointers:
    if start in visited:
      continue
    path = []
    node = start
    local_visited = {}

    while node not in local_visited and node in pointers:
      path.append(node)  
      local_visited[node] = len(path) - 1
      node = pointers[node]

    if node in local_visited:
      cycle_start = local_visited[node]
      cycle = path[cycle_start:]
    ## edits
    #while node not in visited:
      #visited.add(node)
      #path.append(node)
    
      #node = pointers[node]

    #cycle_start = path.index(node)
    #cycle = path[cycle_start:]  # extract cycle only

    if any(node in students for node in cycle):
      while cycle[0] not in students:
        cycle = cycle[1:] + [cycle[0]]
    else:
      continue
    
      # Step 3c: Execute cycle
    for i in range(0, len(cycle), 2):  # student → group → ...
      if i + 1 >= len(cycle):
        break
      student = cycle[i]
      group = pointers[student]
      final_assignment[student] = group
      students.pop(student, None)
      group_to_student.pop(group, None)
    cycle_found = True
    break
  if not cycle_found:
    break

# Step 4: Show results
for sid, group in final_assignment.items():
  print(f"Student {sid} gets group {group}")
