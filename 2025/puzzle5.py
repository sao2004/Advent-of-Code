intervals = []
numbers = []
answer = 0
with open("puzzle5.in", "r") as f, open("puzzle5.out", "w") as o:
    for line in f:
        if "-" in line:
            left_range, right_range = map(int, line.split("-"))
            intervals.append((left_range, right_range))
            # print(intervals)
        elif line.strip().isdigit():
            numbers.append(int(line))
    for x in numbers:
        for left, right in intervals:
            if left <= x <= right:
                print(
                    f"Ingredient ID {x} is fresh because it falls into range {left}-{right}.",
                    file=o,
                )
                answer += 1
                break
        else:
            print(f"Ingredient ID {x} is spoiled.", file=o)
    print(f"Answer: {answer}", file=o)
