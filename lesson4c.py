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
search = input("Enter the county to search: ")
found = False

for county in counties:
    if county == search:
        found = True
        break
        print("County found")
        break
if found:
    print(search,"County is available")
else:
    print(search, "County not found on the list")

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