from math import sqrt


points = [(1, 2), (3, 4), (5, 6), (7, 8)]


def main():
    distances = addDistances()
    print(min(distances))


def euclideanDistance(firstPoint, secondPoint):
    total = 0
    for x, y in firstPoint, secondPoint:
        total += (x - y) ** 2
    return sqrt(total)


def addDistances():
    return [
        euclideanDistance(points[i], points[j])
        for i in range(len(points))
        for j in range(i + 1, len(points))
    ]


if __name__ == "__main__":
    main()
