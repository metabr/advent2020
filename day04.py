import re

INPUT = "day04.txt"

passports = []
new_passport = True

with open(INPUT) as input:
    for line in input.readlines():
        if line == "\n":
            new_passport = True
        elif new_passport == True:
            passports.append(line.strip("\n"))
            new_passport = False
        else:
            passports[-1] += " " + line.strip("\n")

fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]
optional_fields = ["cid"]


def is_passport_valid(passport):
    missing_fields = []
    for field in fields:
        if not passport.get(field):
            if not field in optional_fields:
                missing_fields.append(field)
    return len(missing_fields) == 0


def is_passport_valid2(passport):
    byr = passport.get("byr")
    if not (byr and re.match("^\d{4}$", byr) and 1920 <= int(byr) <= 2002):
        return False

    iyr = passport.get("iyr")
    if not (iyr and re.match("^\d{4}$", iyr) and 2010 <= int(iyr) <= 2020):
        return False

    eyr = passport.get("eyr")
    if not (eyr and re.match("^\d{4}$", eyr) and 2020 <= int(eyr) <= 2030):
        return False

    hgt = passport.get("hgt", "")
    if hgt.endswith("cm"):
        if not (re.match("^\d{3}cm$", hgt) and 150 <= int(hgt[:-2]) <= 193):
            return False
    elif hgt.endswith("in"):
        if not (re.match("^\d{2}in$", hgt) and 59 <= int(hgt[:-2]) <= 76):
            return False
    else:
        return False

    hcl = passport.get("hcl")
    if not (hcl and re.match("#[0-9a-f]{6}$", hcl)):
        return False

    ecl = passport.get("ecl", "")
    if not ecl in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
        return False

    pid = passport.get("pid", "")
    if not re.match("^\d{9}$", pid):
        return False

    return True


def parse_passport(passport_string):
    pairs = passport_string.split(" ")
    result = {}
    for pair in pairs:
        key, val = pair.split(":")
        result[key] = val
    return result


valid = 0
valid2 = 0

for passport in passports:
    p = parse_passport(passport)
    if is_passport_valid(p):
        valid += 1
        if is_passport_valid2(p):
            valid2 += 1

print(f"Valid passports: {valid}")
print(f"Valid passports (part 2): {valid2}")
