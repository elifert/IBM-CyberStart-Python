from math import sqrt


def main():
    needConversion1 = input("Enter first point using (x, y) format: ").split(", ")
    needConversion2 = input("Enter second point using (x, y) format: ").split(", ")
    x_1, y_1, x_2, y_2 = map(lambda x: int(x), needConversion1 + needConversion2)
    points = [(x_1, y_1), (x_2, y_2)]
    print(f"{euclideanDistance(points):.2f}")


def euclideanDistance(points):
    total = 0
    firstPoint, secondPoint = points
    for x, y in firstPoint, secondPoint:
        total += (x - y) ** 2
    return sqrt(total)


if __name__ == "__main__":
    main()
