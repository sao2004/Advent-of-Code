from math import sqrt
from collections import Counter
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False

        self.parent[root_x] = root_y
        return True


    def pretty_print(self):
        for i in range(len(self.parent)):
            print(f"{i}: {self.parent[i]}")
        print()

    def top_three(self):
        roots = [self.find(i) for i in range(len(self.parent))]
        root_counts = Counter(roots)
        top_three = sorted(root_counts.items(), key=lambda x: x[1], reverse=True)[:3]
        return top_three

def get_distance(a, b):
    distance = sqrt(abs(a[0] - b[0])**2 + abs(a[1] - b[1])**2 + abs(a[2] - b[2])**2)
    return distance

def create_edges(data):
    edges = []
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            distance = get_distance(data[i], data[j])
            edges.append((distance, i, j))
    return edges


with open("puzzle8.in", "r") as f:
    lines = f.readlines()
    data = [list(map(int, line.strip().split(","))) for line in lines]

uf = UnionFind(len(lines))

num_of_connected_pairs = 0

for dist, i, j in sorted(create_edges(data)):
    uf.union(i, j)
    # uf.pretty_print()
    num_of_connected_pairs += 1
    if num_of_connected_pairs == 999:
        break

top_three = uf.top_three()
# print(top_three)
answer = 1
for root, count in top_three:
    answer *= count

print(answer)
