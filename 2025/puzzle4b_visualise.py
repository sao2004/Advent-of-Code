import time


def process(matrix, row, col):
    removed = 0
    alt_matrix = [row.copy() for row in matrix]
    for i in range(1, row):
        for j in range(1, col):
            if matrix[i][j] == "@":
                count = 0
                for k in range(i - 1, i + 2):
                    for l in range(j - 1, j + 2):
                        # print(
                        #     f"Checking element {matrix[k][l]}({k}, {l}), processing ({i}, {j})",
                        #     file=o,
                        # )
                        if matrix[k][l] == "@" and not (k == i and l == j):
                            count += 1
                            # print(
                            #     f"Adding to {count} when I'm at {matrix[k][l]}({k}, {l}) processing element {matrix[i][j]}({i}, {j})",
                            #     file=o,
                            # )
                if count < 4:
                    alt_matrix[i][j] = "x"
                    removed += 1
    return alt_matrix, removed


matrix = []
row = 0
col = 0
answer = 0
removed = 0
with open("puzzle4input.in", "r") as f, open("puzzle4out.out", "w") as o:
    buffer = f.readline().strip()
    length = len(buffer)
    border = ["."] * (length + 2)
    matrix.append(border)
    matrix.append(["."] + list(buffer) + ["."])
    for line in f:
        matrix.append(["."] + list(line.strip()) + ["."])
    matrix.append(border)
    row = len(matrix)
    col = len(matrix[0])
    print("\033[H\033[J")
    print("Original matrix:")
    for i in range(1, row - 1):
        for j in range(1, col - 1):
            print(matrix[i][j], end="")
        print("")
    time.sleep(0.5)
    alt_matrix, removed = process(matrix, row, col)
    print("\033[H\033[J")
    print(f"Removed {removed} roll of paper:")
    for i in range(1, row - 1):
        for j in range(1, col - 1):
            print(alt_matrix[i][j], end="")
        print("")
    answer += removed
    matrix = alt_matrix
    time.sleep(0.5)
    while removed:
        alt_matrix, removed = process(matrix, row, col)
        print("\033[H\033[J")
        print(f"Removed {removed} roll of paper:")
        for i in range(1, row - 1):
            for j in range(1, col - 1):
                print(alt_matrix[i][j], end="")
            print("")
        answer += removed
        matrix = [row.copy() for row in alt_matrix]
        time.sleep(0.5)
    print(answer)
