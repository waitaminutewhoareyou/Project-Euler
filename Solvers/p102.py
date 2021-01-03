from os.path import dirname, join

project_root = dirname(dirname(__file__))
data_path = join(project_root, 'Data', '')
data_dir = data_path + 'p102_triangles.txt'


def readData(dir):
    f = open(dir, 'r')
    data = []
    for line in f:
        ls = line.strip().split(',')
        ls = list(map(int, ls))
        data.append(ls)
    return data


def triangle_area(x1, y1, x2, y2, x3, y3):
    return abs(0.5 * (((x2-x1)*(y3-y1))-((x3-x1)*(y2-y1))))


def interiorQ(triangle):

    area1 = triangle_area(0, 0, triangle[0], triangle[1], triangle[2], triangle[3])
    area2 = triangle_area(0, 0, triangle[0], triangle[1], triangle[4], triangle[5])
    area3 = triangle_area(0, 0, triangle[2], triangle[3], triangle[4], triangle[5])

    total_area = triangle_area(*triangle)

    if abs(total_area - (area1+area2+area3)) < 1e-3:
        return True
    return False


if __name__ == '__main__':
    data = readData(data_dir)
    count = sum(map(interiorQ, data))
    print(count)