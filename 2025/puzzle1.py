dial = 50
password = 0
moduledvalue = 0
with open("puzzle1input.in") as f, open("puzzle1output.out", "w") as o:
    print(f"The dial starts by pointing at {dial}", file=o)
    for line in f:
        rotation, value = line[0], int(line[1:])
        if rotation == "L":
            moduledvalue = value % 100
            dial -= moduledvalue
            if dial < 0:
                dial += 100
        elif rotation == "R":
            dial += value
            dial %= 100
        if dial == 0:
            password += 1
        print(f"The dial is rotated {rotation}{value} to point at {dial}", file=o)
    print(password, file=o)
