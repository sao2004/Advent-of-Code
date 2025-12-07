import time

def pretty_print(data):
    print("\033[H\033[J")
    for row in data:
        print(''.join(row))

with open("puzzle7.in", "r") as f:
    data = f.read().splitlines()
    times_splitted = 0
    new_data = []
    new_data = [[data[x][y] for y in range(len(data[x]))] for x in range(len(data))]
    print(len(data))
    for x in range(len(data)):
        for y in range(len(data[x])):
            if new_data[x][y] == '^' and new_data[x-1][y] == '|':
                times_splitted += 1
                if new_data[x][y-1] == '.':
                    # print("entered y-1 = . if")
                    # time.sleep(0.5)
                    new_data[x][y-1] = '|'
                if new_data[x][y+1] == '.':
                    # print("entered y+1 = . if")
                    # time.sleep(0.5)
                    new_data[x][y+1] = '|'
            elif new_data[x][y] == '.':
                if new_data[x-1][y] == 'S' or new_data[x-1][y] == '|':
                    new_data[x][y] = '|'
                else:
                    new_data[x][y] = '.'
        pretty_print(new_data)
        time.sleep(0.4)
    print(times_splitted)
