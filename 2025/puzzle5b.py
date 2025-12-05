intervals = []
numbers = set()
answer = 0
loading = 0
with open("puzzle5.in", "r") as f, open("puzzle5.out", "w") as o:
    for line in f:
        if "-" in line:
            left_range, right_range = map(int, line.split("-"))
            intervals.append([left_range, right_range])

    intervals.sort(key=lambda x: x[0])
    # print(intervals)
    answer = intervals[0][1] - intervals[0][0] + 1
    print(f"First interval: {intervals[0]}", file=o)
    x = 0
    for left, right in intervals[1:]:
        x += 1
        print(f"Processing interval {left}-{right}", file=o)
        print(
            f"Comparing {left} with {intervals[x - 1][0]} and {right} with {intervals[x - 1][1]}",
            file=o,
        )
        if left >= intervals[x - 1][0] and right <= intervals[x - 1][1]:
            print(
                f"Skipping interval {left}-{right} because it is contained within the last interval",
                file=o,
            )
            intervals.remove([left, right])
            x -= 1
            continue
        print(f"Comparing {left} with {intervals[x - 1][1]}", file=o)
        if left > intervals[x - 1][1]:
            print(
                f"Adding {right}-{left}+1={right - left + 1} because {left} > {intervals[x - 1][1]}",
                file=o,
            )
            answer += right - left + 1
        else:
            print(f"Comparing {right} with {intervals[x - 1][1]}", file=o)
            if right > intervals[x - 1][1]:
                print(
                    f"Adding {right}-{intervals[x - 1][1]}={right - intervals[x - 1][1]} because {right} > {intervals[x - 1][1]}",
                    file=o,
                )
                answer += right - intervals[x - 1][1]

    print(f"Answer: {answer}", file=o)
    # for left, right in intervals:
    #     print(f"Adding to answer {right - left + 1} on interval {left}-{right}", file=o)
    #     answer += right - left + 1
    # # answer = len(numbers)
    # print(f"Answer: {answer}", file=o)
