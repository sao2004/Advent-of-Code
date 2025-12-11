def dfs_rec(current, end, neighbours, nodes_to_index, index_to_nodes, memo):
    if current == end:
        return 1
    if memo[nodes_to_index[current]] != -1:
        return memo[nodes_to_index[current]]
    ways = 0
    for neighbour in neighbours[nodes_to_index[current]]:
        ways += dfs_rec(index_to_nodes[neighbour], end, neighbours, nodes_to_index, index_to_nodes, memo)
    memo[nodes_to_index[current]] = ways
    return ways

with open("puzzle11.in", "r") as f, open("puzzle11.out", "w") as o:
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
    # print(nodes_to_index, file=o)
    i = 0
    for index, node in enumerate(nodes_to_index):
        index_to_nodes[index] = node
    # print(index_to_nodes, file=o)
    for line in data:
        parts = line.strip().split(": ")
        # print(parts)
        for part in parts[1].split(" "):
            # print(f"Adding {nodes_to_index[part]} to index {nodes_to_index[parts[0]]}")
            neighbours[nodes_to_index[parts[0]]].append(nodes_to_index[part])
    memo = [-1] * len(nodes_to_index)
    answer = 1
    checkpoints = ["svr", "fft", "dac", "out"]
    for i in range(len(checkpoints)-1):
        print(f"Applying DFS from {checkpoints[i]} to {checkpoints[i+1]}")
        nr_ways = dfs_rec(checkpoints[i], checkpoints[i+1], neighbours, nodes_to_index, index_to_nodes, memo)
        print(f"Number of ways from {checkpoints[i]} to {checkpoints[i+1]}: {nr_ways}")
        answer *= nr_ways
        memo = [-1] * len(nodes_to_index)
    print(f"Number of ways: {answer}")
