from shapely import Polygon

def get_area(x, y):
    return (abs(y[1]-x[1])+1)*(abs(y[0]-x[0])+1)

with open("puzzle9.in", "r") as f:
    lines = f.readlines()
    data = [list(map(int, line.strip().split(","))) for line in lines]
    # print(data)
    big_polygon = Polygon(data)
    max_area = -1
    for point1 in data:
        for point2 in data:
            min_x = min(point1[0], point2[0])
            max_x = max(point1[0], point2[0])
            min_y = min(point1[1], point2[1])
            max_y = max(point1[1], point2[1])
            polygon = Polygon([(min_x, min_y), (max_x, min_y), (max_x, max_y), (min_x, max_y)])
            if big_polygon.contains(polygon):
                if get_area(point1, point2) > max_area:
                    max_area = get_area(point1, point2)
    print(f"Max area: {max_area}")
