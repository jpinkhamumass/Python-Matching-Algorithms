import csv

students = {}
preference_keys = []

with open('shortpref.csv', 'r') as people:
    csv_reader = csv.DictReader(people)
    headers = csv_reader.fieldnames

    # Dynamically get all preference fields (excluding 'student_id' and 'assigned_group')
    preference_keys = [col for col in headers if col not in ['student_id', 'assigned_group']]

    for row in csv_reader:
      key = row['student_id']
      students[key] = {k: row[k] for k in preference_keys}
      students[key]['assigned_group'] = row['assigned_group']

print(students)


group_to_student = {}
for sid, info in students.items():
  group = info['assigned_group']
  if group:
      group_to_student[group] = sid

final_assignment = {}

while students:
  # build pointers
  pointers = {}

  # Students point to their top available choice
  for sid, info in students.items():
    for key in preference_keys:
        choice = info[key]
        if choice:
          pointers[sid] = choice
          break

  # Groups point to the student currently assigned to them
  for group, sid in group_to_student.items():
    if sid in students:
      pointers[group] = sid

  # Find a cycle
  visited = set()
  path = []
  node = next(iter(pointers))  # start anywhere

  while node not in visited:
    visited.add(node)
    path.append(node)
    if node not in pointers:
      # Dead end — no pointer from this node
      break

    node = pointers[node]
  if not path:
    continue  # Skip this round if no cycle was found



  cycle_start = path.index(node)
  cycle = path[cycle_start:]  # extract cycle only

  while cycle[0] not in students:
    cycle = cycle[1:] + [cycle[0]]

    # Execute cycle
  for i in range(0, len(cycle), 2):  # student → group → ...
    student = cycle[i]
    group = pointers[student]
    final_assignment[student] = group
    students.pop(student)
    group_to_student.pop(group, None)

#Show results
for sid, group in final_assignment.items():
  print(f"Student {sid} gets group {group}")
