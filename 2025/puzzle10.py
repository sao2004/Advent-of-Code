def button_press(diagram, buttons):
    # print(diagram)
    for button in buttons:
        # print(button)
        if diagram[button] == '#':
            diagram[button] = '.'
        elif diagram[button] == '.':
            diagram[button] = '#'
    return diagram

def bfs(todo_diagram, start, buttons):
    with open("puzzle10.out", "w") as f:
        # f.write(f"Starting BFS with diagram {diagram}\n")
        queue = []
        queue.append((start.copy(), 0))
        print(queue, file=f)
        # finished_diagram = "#" * len(diagram)
        visited = set()
        level = 0
        while queue:
            actual_diagram, level = queue.pop(0)
            # print(f"I'm at level {level} with diagram {actual_diagram}", file=f)
            state = "".join(actual_diagram)
            if state in visited:
                continue
            visited.add(state)
            if todo_diagram == actual_diagram:
                return level
            for button in buttons:
                # print(f"Pressing button {button} on {actual_diagram}", file=f)
                new_diagram = button_press(actual_diagram.copy(), button)
                queue.append((new_diagram, level + 1))
                # print(f"Added {new_diagram} to queue", file=f)



with open("puzzle10.in", "r") as f:
    result = 0
    for line in f:
        diagram = []
        buttons = []
        voltage = []
        # print(line.strip())
        for group in line.strip().split(" "):
            if group.startswith("["):
                diagram = list(group[1:-1])
                # print(diagram)
                # print()
            elif group.startswith("("):
                buttons.append(tuple(map(int, group[1:-1].split(","))))
                # print(buttons)
            elif group.startswith("{"):
                voltage = group[1:-1].split(", ")
                # print(voltage)
        start_diagram = ["." for _ in range(len(diagram))]
        number_of_presses = bfs(diagram, start_diagram, buttons)
        # print(f"Number of presses required: {number_of_presses}")
        result += number_of_presses
    print(f"Total number of presses required: {result}")
