# Using readlines()
inputList = open("inputDay4.txt", "r")
lines = inputList.readlines()

#   byr (Birth Year)
#   iyr (Issue Year)
#   eyr (Expiration Year)
#   hgt (Height)
#   hcl (Hair Color)
#   ecl (Eye Color)
#   pid (Passport ID)
#   cid (Country ID)

nrPassports = 0


def validByr(byr):
    byrV = int(byr)
    if (byrV >= 1920) and (byrV <= 2002):
        return True
    return False


def validIyr(iyr):
    iyrV = int(iyr)
    if (iyrV >= 2010) and (iyrV <= 2020):
        return True
    return False


def validEyr(eyr):
    eyrV = int(eyr)
    if (eyrV >= 2020) and (eyrV <= 2030):
        return True
    return False


def validHgt(hgt):
    if "cm" in hgt:
        hgtV = int(hgt.split("cm")[0])
        if (hgtV >= 150) and (hgtV <= 193):
            return True
    else:
        if "in" in hgt:
            hgtV = int(hgt.split("in")[0])
            if (hgtV >= 59) and (hgtV <= 76):
                return True
        return False


def validHcl(hcl):
    if (hcl[0] == "#") and (len(hcl) == 7):
        for elem in hcl[1:6]:
            if (elem not in [str(i) for i in range(0, 10)]) and (
                elem not in ["a", "b", "c", "d", "e", "f"]
            ):
                return False
        return True
    return False


def validEcl(ecl):
    if ecl in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
        return True
    return False


def validPid(pid):
    if len(pid) == 9:
        try:
            int(pid)
            return True
        except:
            return False
    return False


def passportCheck(passport):
    if (
        ("byr" in passport)
        and ("iyr" in passport)
        and ("eyr" in passport)
        and ("hgt" in passport)
        and ("hcl" in passport)
        and ("ecl" in passport)
        and ("pid" in passport)
    ):
        if (
            (validByr(passport["byr"]))
            and (validIyr(passport["iyr"]))
            and (validEyr(passport["eyr"]))
            and (validHgt(passport["hgt"]))
            and (validHcl(passport["hcl"]))
            and (validEcl(passport["ecl"]))
            and (validPid(passport["pid"]))
        ):
            return True
    return False


passport = {}

for i in lines:
    if i == "\n":
        if passportCheck(passport):
            nrPassports += 1
        passport = {}
    else:
        entry = i.split(" ")
        for j in entry:
            entryValue = j.split(":")
            passport[entryValue[0]] = entryValue[1].rstrip()

print(nrPassports)
