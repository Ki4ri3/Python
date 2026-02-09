# A for loop can be used to iterate through a list, tuple, stirng or a dictionary.

name = "Kiarie"

for letter in name:
    if letter == "a":
        print("This is letter a")
    else:
        print(letter)

print("=======================================")
# below is a list of counties.
counties = ["Nairobi", "Mombasa", "Kisumu", "Nakuru",
            "Eldoret", "Machakos", "Kajiado", "Embu"]

print(counties)

for county in counties:
    print(county)

print("=======================================")

for county in counties:
    if county == "Nakuru":
        print("County found")
        break
else:
    print("County not found")

print("=======================================")
# The for loop can also be used to iterate through a dictionary
player = {
    "name": "Mbappe",
    "age": 27,
    "teams": ["PSG", "Real Madrid"],
    "nationality": "French"
}

for value  in player:
    print(player[value])

print("=======================================")

# Loop through the teamsthe player has played for

for teams in player["teams"]:
    print(teams)