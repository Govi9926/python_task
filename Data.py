"""Create a list of dictionaries where each dictionary represents a person with attributes "name," "age,"
and "city." Include at least three persons in the list."""

#data
persons = [
    {"name": "Govind ", "age": 28, "city": "Indore"},
    {"name": "Gaurav", "age": 22, "city": "Bhopal"},
    {"name": "Harsh", "age": 26, "city": "ujjain"}
]

#Filter out persons who are under the age of 25.
filtered_persons = []
for person in persons:
    if person["age"] >= 25:
        filtered_persons.append(person)

print(filtered_persons)

sorted_persons = sorted(filtered_persons, key=lambda x: x["city"])
print(sorted_persons)


for person in filtered_persons:
    print(f"Name: {person['name']}, Age: {person['age']}, City: {person['city']}")
