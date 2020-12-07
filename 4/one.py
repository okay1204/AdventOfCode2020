with open('input.txt') as f:
    passports = f.read()

passports = passports.split("\n\n")
passports = list(map(lambda passport: passport.replace("\n", " "), passports))

# converting them all into a dict
for index, passport in enumerate(passports):
    temp_dict = {}

    for pair in passport.split():
        key, value = pair.split(":")
        temp_dict[key] = value

    print(temp_dict)
    passports[index] = temp_dict


# checking if valid

valid = 0
for passport in passports:

    # if has all requirements
    if len(passport) == 8 or (len(passport) == 7 and 'cid' not in passport.keys()):
        valid += 1

print(valid)