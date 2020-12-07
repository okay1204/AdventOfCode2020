with open('input.txt') as f:
    inputs = f.read()

# seperating into groups
groups = inputs.split("\n\n")

# seperating into different people
for index, group in enumerate(groups):
    groups[index] = group.split("\n")


yes = 0
for group in groups:

    total_yes = 0

    for answer in group[0]:

        count = 0

        for person in group:
            if answer in person:
                count += 1
        
        if count == len(group): total_yes += 1

    yes += total_yes

print(yes)
