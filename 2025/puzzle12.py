with open("puzzle12.in", "r") as f:
    data = f.read().splitlines()
    areas = []
    presents = []
    present_matrix = []
    i = 0
    for line in data:
        # print(f"Analyzing line: {line}")
        if "#" in line:
            present_matrix.append(line)
            # print(f"Added line to present matrix: {line}")
            i += 1
        if i == 3:
            # print(f"Present matrix: {present_matrix}")
            presents.append(present_matrix)
            present_matrix = []
            i = 0
        if "x" in line:
            areas.append(line)
    # print(areas[0])
    possible = 0
    for area in areas:
        area = area.split("x")
        width = int(area[0])
        area = area[1]
        area = area.split(":")
        length = int(area[0])
        # print(f"W{width} L{length}")
        total_area = width * length
        # print(f"Total area: {total_area}")
        area = area[1]
        number_of_presents = area.strip(" ")
        for number in number_of_presents.split(" "):
            number = int(number)
            total_area -= number * 9
            # print(number)
        if total_area < 0:
            print("Not enough space")
        else:
            possible += 1
        # print(number_of_presents)
        # height = int(area[1])
    print(possible)
