password = 0
number_arr = []
with open("puzzle3input.in", "r") as f, open("puzzle3output.out", "w") as out:
    for line in f:
        number_arr = []
        first_max = -999
        index_max = -1
        second_max = -999
        index_second_max = -1
        for digit in range(len(line.strip())):
            for number in reversed(number_arr):
                if (
                    line[digit] > number
                    and 12 - len(number_arr) + 1 <= len(line.strip()) - digit
                ):
                    number_arr.pop()
            if len(number_arr) < 12:
                number_arr.append(line[digit])
        print(f"{number_arr}")
        number = int("".join(number_arr))
        # print(number)
        password += number
    print(password)
