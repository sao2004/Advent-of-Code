def create_edges(data):
    edges = []
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            edges.append((data[i], data[j], get_area(data[i], data[j])))
    return edges

def get_area(x, y):
    return (abs(y[1]-x[1])+1)*(abs(y[0]-x[0])+1)

with open("puzzle9.in", "r") as f, open("puzzle9.out", "w") as o:
    lines = f.readlines()
    data = [list(map(int, line.strip().split(","))) for line in lines]
    print(data)
    edges = sorted(create_edges(data), key=lambda x: x[2])
    edges.reverse()
    # print(edges, file=o)
    area = get_area(edges[0][0], edges[0][1])
    print(f"Largest area is {area} with coordinates {edges[0][0]} and {edges[0][1]}")
