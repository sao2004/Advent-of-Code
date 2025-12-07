import time

def pretty_print(data, aparitions_vector):
    # print("\033[H\033[J")
    for row in data:
        print(''.join(row))
    for i in aparitions_vector:
        print(i, end=' ')
    print()

with open("puzzle7.in", "r") as f:
    data = f.read().splitlines()
    aparitions_vector = [0] * len(data)
    new_data = []
    new_data = [[data[x][y] for y in range(len(data[x]))] for x in range(len(data))]
    result = 0
    # print(len(data))
    for x in range(len(data)):
        for y in range(len(data[x])):
            if new_data[x][y] == 'S':
                aparitions_vector[y] += 1
            if new_data[x][y] == '^':
                # pretty_print(new_data, aparitions_vector)
                # time.sleep(0.1)
                aparitions_vector[y-1] += aparitions_vector[y]
                aparitions_vector[y+1] += aparitions_vector[y]
                aparitions_vector[y] = 0
                # pretty_print(new_data, aparitions_vector)
                # time.sleep(0.1)
    for i in aparitions_vector:
        result += i
    print(result)
