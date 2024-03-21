import json

def main():
    people = []
    try:
        with open("people.json", "r") as file:
            data = json.load(file)
            print(data)
            people = data["people"]
            print("Number of people already in the list: ", len(people))
    except FileNotFoundError:
        pass

    while True:
        name = input("Enter name: ")
        if name == "":
            break
        occupation = input("Enter occupation: ")
        rarity = input("Enter rarity: ")  # Prompt for rarity attribute
        
        # Check if the name already exists in the list
        for person in people:
            if person["name"] == name:
                print("Name already exists. Keeping original.")
                break
        else:
            people.append({"name": name, "occupation": occupation, "rarity": rarity})  # Add rarity attribute
        
    with open("people.json", "w") as file:
        json.dump({"people": people}, file)

main()
