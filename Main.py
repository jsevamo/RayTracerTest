def main():
    nx: int = 200
    ny: int = 100

    print("P3\n" + str(nx) + " " + str(ny) + "\n255\n")

    for j in range(ny - 1, 0, -1):
        for i in range(0, nx, 1):
            r: float = i / nx
            g: float = j / ny
            b: float = 0.2
            ir: int = int(255.99 * r)
            ig: int = int(255.99 * g)
            ib: int = int(255.99 * b)
            print(str(ir) + " " + str(ig) + " " + str(ib) + "\n")


main()
