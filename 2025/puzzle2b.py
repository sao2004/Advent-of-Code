def get_parts(x, nr_parts):
    list_x = list(x)
    if len(list_x) % nr_parts != 0:
        return False
    nr_digits = len(list_x) // nr_parts
    # print(f"Nr digits {nr_digits}")
    to_compare = list_x[0:nr_digits]
    # print(f"To_compare = {to_compare}")
    for i in range(1, nr_parts):
        prev = i * (nr_digits)
        next = (i + 1) * (nr_digits)
        # print(f"Prev is {prev}, next is {next}")
        compared = list_x[prev:next]
        # print(f"Compared is {compared}")
        # print(f"Comparing {to_compare} to {compared}")
        if to_compare != compared:
            return False
    return True


if __name__ == "__main__":
    password = 0
    with open("iustin.in", "r") as f, open("output.txt", "w") as output:
        for line in f:
            words = line.split(",")
            for word in words:
                left_range, right_range = word.split("-")
                print(f"Range is {left_range}-{right_range}")
                for i in range(int(left_range), int(right_range) + 1):
                    i_arr = str(i)
                    len_i = len(i_arr)
                    for x in range(2, len_i + 1):
                        if get_parts(i_arr, x):
                            password += i
                            print(
                                f"Adding {i} to password from range {left_range}-{right_range}",
                                file=output,
                            )
                            break
            print(f"Password is {password}", file=output)
