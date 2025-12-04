password = 0
with open("puzzle3input.in", "r") as f, open("puzzle3output.out", "w") as out:
    for line in f:
        first_max = -999
        index_max = -1
        second_max = -999
        index_second_max = -1
        for digit in range(len(line.strip())):
            if int(line[digit]) > int(first_max) and digit < len(line.strip()) - 1:
                first_max = line[digit]
                index_max = digit
                second_max = -999
            elif int(line[digit]) > int(second_max):
                second_max = line[digit]
                index_second_max = digit
            print(f"{line[digit]}", end="", file=out)
        print(
            f" {first_max} found at {index_max}, {second_max} found at {index_second_max}",
            file=out,
        )
        password += int(first_max) * 10 + int(second_max)
    print(f"Password: {password}", file=out)
