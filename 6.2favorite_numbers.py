favorite_numbers = {
    'Nanek': [5, 6, 8],
    'Jarek': [6, 4],
    'Jozek': [7, 5],
    'Arek': [8, 3],
    'Zuza': [9, 4],
}

for friend, value in favorite_numbers.items():
    print(friend)
    for val in value:
        print(val)

list_od_dicts = [
    {'name': 'Jarek', 'gender': 'male', 'age': 21},
    {'name': 'Jurek', 'gender': 'male', 'age': 22},
    {'name': 'Janek', 'gender': 'male', 'age': 23}]

print(list_od_dicts)
total_male_age = 0
for dict in list_od_dicts:
    if dict.get('gender') == 'male':
        total_male_age = total_male_age + dict.get('age')
print(total_male_age)
print(sum(d['age'] for d in list_od_dicts if d['gender']=='male'))