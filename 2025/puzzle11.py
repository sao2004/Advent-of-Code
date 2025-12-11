def bfs(start, neighbours, nodes_to_index, index_to_nodes):
    queue = [start]
    nr_ways = 0
    while queue:
        current = queue.pop(0)
        # print(current)
        if current == "out":
            # print("Reached out")
            nr_ways += 1
        else:
            # print(nodes_to_index[current])
            for neighbour in neighbours[nodes_to_index[current]]:
                # print(f"Adding {index_to_nodes[neighbour]}:{neighbour} to queue")
                queue.append(index_to_nodes[neighbour])
    return nr_ways

with open("puzzle11.in", "r") as f:
    data = f.readlines()
    # print(len(data))
    neighbours = [[]for _ in range(len(data)+1)]
    nodes_to_index = {}
    nodes_to_index["out"] = 0
    index_to_nodes = {}
    i = 1
    for line in data:
        parts = line.strip().split(": ")
        # print(parts)
        nodes_to_index[parts[0]] = i
        i += 1
    # print(nodes_to_index)
    i = 0
    for index, node in enumerate(nodes_to_index):
        index_to_nodes[index] = node
    # print(index_to_nodes)
    for line in data:
        parts = line.strip().split(": ")
        # print(parts)
        for part in parts[1].split(" "):
            # print(f"Adding {nodes_to_index[part]} to index {nodes_to_index[parts[0]]}")
            neighbours[nodes_to_index[parts[0]]].append(nodes_to_index[part])
        # print(node)
        # print(bfs(node, "end"))
    # for neighbour in neighbours:
    #     print(neighbour)
    nr_ways = bfs("you", neighbours, nodes_to_index, index_to_nodes)
    print(f"Number of ways: {nr_ways}")
