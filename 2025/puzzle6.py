answer_col = 0
answer_total = 0
with open("puzzle6.in", "r") as f, open("puzzle6.out", "w") as o:
    data = f.read()
    data = data.split("\n")
    data = [row.split() for row in data]
    data.pop()
    print(data)
    for x in range(len(data[0])):
        # print(f"The operation is {data[len(data) - 1][x]}")
        answer_col_plus = 0
        answer_col_times = 1
        for y in range(len(data) - 1):
            number = int(data[y][x])
            if data[len(data) - 1][x] == "+":
                answer_col_plus += number
                if y == 0:
                    print(f"{number}", end=" ", file=o)
                else:
                    print(f"+ {number}", end=" ", file=o)
            elif data[len(data) - 1][x] == "*":
                answer_col_times *= number
                if y == 0:
                    print(f"{number}", end=" ", file=o)
                else:
                    print(f"* {number}", end=" ", file=o)
        if data[len(data) - 1][x] == "+":
            answer_col = answer_col_plus
        elif data[len(data) - 1][x] == "*":
            answer_col = answer_col_times
        print(f"= {answer_col}", file=o)
        answer_total += answer_col
    print(f"= {answer_total}", file=o)
