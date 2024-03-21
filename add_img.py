# {
#     "name": "Melissa Cristina M\\u00e1rquez",
#     "occupation": "Marine Biologist",
#     "rarity": "common"
# },
# import json under people element in the list theres content like that add img attribute to the list with the data first name.png

import json

# Read the JSON file
with open('./people.json', 'r') as file:
    data = json.load(file)

# Iterate over the list of people
for person in data['people']:
    # Extract the first name from the 'name' field
    first_name = person['name'].split()[0]

    #uncapitalize the first letter
    first_name = first_name.lower()
    
    # Add the 'img' attribute to the person dictionary
    person['img'] = f'{first_name}.png'
    person['import'] = f'import {first_name} from "./{first_name}.jpg";'

#write all import statements to a file
with open('./imports.txt', 'w') as file:
    for person in data['people']:
        file.write(person['import'] + '\n')

# Write the updated data back to the JSON file
with open('./people.json', 'w') as file:
    json.dump(data, file)