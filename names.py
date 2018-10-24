
names = ['Arthur Dent', 'Zaphod Beeblebrox', 'Trillian Astra']

first_names = []
last_names = []

for i in range(len(names)):
    split_name = names[i].split(' ')
    first_name, last_name = tuple(split_name)
    first_names.append(first_name)
    last_names.append(last_name)

print(first_names)
print(last_names)

# first_names = ['Arthur', 'Zaphod', 'Trillian']
# last_names = ...

