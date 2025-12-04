password = 0
with open("puzzle2input.in", "r") as f, open("output.txt", "w") as output:
    for line in f:
        words = line.split(",")
        for word in words:
            left_range, right_range = word.split("-")
            # print(f"Interval {left_range} and {right_range}")
            # print(
            #     f"Left_range len = {len(left_range)} and first half is {int(left_range) // pow(10, len(left_range) // 2)} and second half is {int(left_range) % pow(10, len(left_range) // 2)}"
            # )
            print(f"Range is {left_range}-{right_range}")
            for i in range(int(left_range), int(right_range)):
                i_arr = str(i)
                len_i = len(i_arr)
                if len_i % 2 == 0:
                    if i // pow(10, len_i // 2) == i % pow(10, len_i // 2):
                        password += i
                        print(
                            f"Adding {i} to password from range {left_range}-{right_range}",
                            file=output,
                        )
        print(f"Password is {password}", file=output)
