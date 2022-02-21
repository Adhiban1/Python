import math

# point: Place  of the object
# 'point_to_anlge' is a function which convets the point value into angles a1 and a2
# length: Length if the each arm, Total Arm Length = 2 * length


def point_to_anlge(point=(0, 1), length=1) -> tuple:
    dis = math.sqrt(point[0] ** 2 + point[1] ** 2)
    if dis < length * 2:
        a1 = math.acos(point[0] / dis) + math.acos(dis / (2 * length))
        a2 = math.pi - 2 * math.acos(dis / (2 * length))
        return (a1 * (180 / math.pi), a2 * (180 / math.pi))
    else:
        print(f'"Out of Range" for point={point} and length={length}')
        return (150, 60)  # Default Value


def main():
    Angle1, Angle2 = point_to_anlge((1, 1), 1)
    print(f"Angle1 is {int(Angle1)} and Angle2 is {int(Angle2)}")

    Angle3, Angle4 = point_to_anlge((2, 2), 1)
    print(f"Angle3 is {int(Angle3)} and Angle4 is {int(Angle4)}")


if __name__ == "__main__":
    main()
