from math import sqrt


# declaring points globally to increase its readability and make adjustments easily
points = [(1, 2), (3, 4), (5, 6), (7, 8)]


def main():
    distances = addDistances()
    print(min(distances))


def euclideanDistance(firstPoint, secondPoint):
    # calculating euclidean distance for a pair of points
    total = 0
    for x, y in zip(firstPoint, secondPoint):
        total += (x - y) ** 2
    return sqrt(total)


def addDistances():
    # returning a list of distances using list comprehension
    return [
        euclideanDistance(points[i], points[j])
        for i in range(len(points))
        for j in range(i + 1, len(points))
    ]


if __name__ == "__main__":
    main()
