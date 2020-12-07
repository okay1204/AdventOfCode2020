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

    passports[index] = temp_dict


# checking if valid

valid = 0
for passport in passports:

    # if has all keys
    if len(passport) == 8 or (len(passport) == 7 and 'cid' not in passport.keys()):
        
        # birth year
        if not 1920 <= int(passport['byr']) <= 2002:
            continue
        
        # issue year
        if not 2010 <= int(passport['iyr']) <= 2020:
            continue
        
        # expiration year
        if not 2020 <= int(passport['eyr']) <= 2030:
            continue

        # height
        if passport['hgt'].endswith('cm'):
            height = int(passport['hgt'].replace('cm', ''))

            if not 150 <= height <= 193:
                continue

        elif passport['hgt'].endswith('in'):
            height = int(passport['hgt'].replace('in', ''))

            if not 59 <= height <= 76:
                continue
        else:
            continue

        # hair color
        if not passport['hcl'].startswith("#") and not len(passport['hcl']) == 7:
            continue

        # eye color
        if not passport['ecl'] in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'):
            continue
        
        # passport id
        if not len(passport['pid']) == 9:
            continue

        valid += 1

print(valid)