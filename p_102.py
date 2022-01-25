def triangle_area(x1, y1, x2, y2, x3, y3):
    """Calculates area of triangle using x, y from 3 points
    """
    return 0.5 * abs((x1 * (y2 - y3) + (x2 * (y3 - y1) + (x3 * (y1 - y2)))))


def point_in_triangle(line):
    """Takes line from triangles text file, calculating original area as well
    as the areas of AB0, AC0 and BC0. Returns true if the areas of these are
    equal to that of the original area - 0, 0 exists within original area.
    """
    coords = line.rstrip().split(",")
    coords = [int(i) for i in coords]
    x0 = 0
    y0 = 0
    x1 = coords[0]
    y1 = coords[1]
    x2 = coords[2]
    y2 = coords[3]
    x3 = coords[4]
    y3 = coords[5]

    area_original = triangle_area(x1, y1, x2, y2, x3, y3)
    area0_1 = triangle_area(x1, y1, x2, y2, x0, y0)
    area0_2 = triangle_area(x1, y1, x3, y3, x0, y0)
    area0_3 = triangle_area(x2, y2, x3, y3, x0, y0)

    if area0_1 + area0_2 + area0_3 == area_original:
        return True
    else:
        return False


if __name__ == "__main__":
    file = "data/p102_triangles.txt"
    contains_origin = 0

    with open(file, 'r') as f:
        for line in f:
            if point_in_triangle(line):
                contains_origin += 1

    print(contains_origin)


#: answer: 228
