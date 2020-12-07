with open('input.txt') as f:
    inputs = f.read()

# seperating into groups
groups = inputs.split("\n\n")

# seperating into different people
for index, group in enumerate(groups):
    groups[index] = group.split("\n")


yes = 0
for group in groups:

    answered = set()
    for person in group:
        for answer in person:
            answered.add(answer)

    yes += len(answered)

print(yes)
