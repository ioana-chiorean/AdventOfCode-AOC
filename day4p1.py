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


def passportCheck(passport):
    if (
        ("byr" in passport) 
        and ("iyr" in passport)
        and ("eyr" in passport)
        and ("hgt" in passport)
        and ("hcl" in passport)
        and ("ecl" in passport)
        and ("pid" in passport) 
        #or ("cid" in passport)
    ):
        return True
    print(passport)
    return False


passport = {}

for i in lines:
    if i == "\n":
        if passportCheck(passport):
            nrPassports += 1
        print(nrPassports)
        passport = {}
    else:
        entry = i.split(" ")
        for j in entry:
            entryValue = j.split(":")
            passport[entryValue[0]] = entryValue[1].rstrip

print(nrPassports)
