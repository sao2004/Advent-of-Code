dial = 50
password = 0
moduledvalue = 0
with open("puzzle1input.in") as f, open("puzzle1output.out", "w") as o:
    print(f"The dial starts by pointing at {dial}", file=o)
    for line in f:
        previous_dial = dial
        rotation, value = line[0], int(line[1:])
        if rotation == "L":
            dial = (dial - value) % 100
        elif rotation == "R":
            dial = (dial + value) % 100
        print(f"The dial is rotated {rotation}{value} to point at {dial}", file=o)
        toAdd = 0
        if rotation == "L":
            if value >= previous_dial:
                toAdd = abs(previous_dial - value) // 100
                if previous_dial - value <= 0:
                    toAdd += 1
                if previous_dial == 0:
                    toAdd -= 1
                # print(f"Added {(value - previous_dial) // 100 + 1} to password", file=o)
        elif rotation == "R":
            toAdd = (value + previous_dial) // 100
            # print(f"Added {(value + previous_dial) // 100} to password", file=o)
        password += toAdd
        print(f"Added {toAdd} to password", file=o)

    print(password, file=o)
