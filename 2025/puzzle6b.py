def my_split(data):
    splited = []
    aux = []
    nr_rows = len(data)
    nr_cols = len(data[0])
    for y in range(nr_cols):
        for x in range(nr_rows):
            aux.append(data[x][y])

        splited.append(aux)
        aux = []
    return splited


def process(splited, operators):
    answer = 0
    result_plus = 0
    result_x = 1
    operator_iter = 0
    with open("puzzle6.out", "w") as o:
        for x in splited:
            print(x)
            delimitator = False
            if all(y == " " for y in x):
                print("DELIMITATOR")
                if operators[operator_iter] == "+":
                    print("Operation is addition")
                elif operators[operator_iter] == "*":
                    print("Operation is multiplication")
                delimitator = True
            if not delimitator:
                number_string = ""
                for y in range(len(x)):
                    # print(x[y], end="", file=o)
                    # print(f"joining {x[y]}", file=o)
                    if x[y].isdigit():
                        number_string += x[y]
                # print(
                #     f" string {number_string} devine int {int(number_string)}",
                #     file=o,
                # )
                if operators[operator_iter] == "+":
                    # print(f"+ {number_string}", end=" ", file=o)
                    result_plus += int(number_string)
                elif operators[operator_iter] == "*":
                    # print(f"* {number_string}", end=" ", file=o)
                    result_x *= int(number_string)
            if delimitator:
                if operators[operator_iter] == "+":
                    answer += result_plus
                    # print(f"= {result_plus}", file=o)
                    result_plus = 0
                elif operators[operator_iter] == "*":
                    answer += result_x
                    # print(f"= {result_x}", file=o)
                    result_x = 1
                operator_iter += 1
        if operators[operator_iter] == "+":
            answer += result_plus
            # print(f"= {result_plus}", file=o)
            result_plus = 0
        elif operators[operator_iter] == "*":
            answer += result_x
            # print(f"= {result_x}", file=o)
            result_x = 1
    return answer


with open("puzzle6.in", "r") as f:
    data = f.read()
    data = data.split("\n")
    data.pop()
    # print(data)
    operators = data.pop().split()
    # print(data)
    # print(operators)
    splited = my_split(data)
    print(splited)
    # print()
    print(process(splited, operators))
