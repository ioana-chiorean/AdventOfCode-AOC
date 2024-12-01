# Using readlines()
inputList = open("inputDay5.txt", "r")
tickets = inputList.readlines()

ticketRow = []
ticketColumn = []

# This airline uses binary space partitioning to seat people. A seat might be specified like FBFBBFFRLR, where F means "front", B means "back", L means "left", and R means "right".
# The first 7 characters will either be F or B. these specify exactly one of the 128 rows on the plane (numbered 0 through 127).  EX. F (0 through 63) or B (64 through 127).
# The last three characters will be either L or R; these specify exactly one of the 8 columns of seats on the plane (numbered 0 through 7).

seatID = 0

for i in tickets:
    x = 0
    y = 127
    for j in [0, 1, 2, 3, 4, 5, 6]:
        if i[j] == "F":
            y = x + (y - x) // 2
        else:
            if ((y - x) // 2) == ((y - x) / 2):
                x = x + (y - x) // 2
            else:
                x = x + 1 + (y - x) // 2
    ticketRow.append(x)
    z = 0
    t = 7
    for j in [7, 8, 9]:
        if i[j] == "L":
            t = z + (t - z) // 2
        else:
            if ((t - z) // 2) == ((t - z) / 2):
                z = z + (t - z) // 2
            else:
                z = z + 1 + (t - z) // 2
    ticketColumn.append(t)
    # print(x,t)
    # print(x*8+t)
    if (x * 8 + t) > seatID:
        seatID = x * 8 + t
    #print(seatID)

#print(ticketRow)
#print(ticketColumn)
print(seatID)