# /*******************************************************
# * 2020 Juan Sebastián Vargas Molano j.sevamo@gmail.com
# *******************************************************/


# Main function for the raytracer
def main():
    # This is how we can create a ppm image to write.
    outputImage = open("renderedImage.ppm", "w+")

    # width (nx) and height (ny) of the output image.
    nx: int = 200
    ny: int = 100

    # create a ppm image header based on this: https://en.wikipedia.org/wiki/Netpbm#File_formats
    print("P3\n" + str(nx) + " " + str(ny) + "\n255\n")
    outputImage.write("P3\n" + str(nx) + " " + str(ny) + "\n255\n")

    # The for loop that writes the pixels of the image. It writes from left to right
    # and then from top to bottom.
    for j in range(ny, 0, -1):
        for i in range(0, nx, 1):
            #Just random numbers for now to create an image.
            r: float = i / nx
            g: float = j / ny
            b: float = 0.2
            ir: int = int(255.99 * r)
            ig: int = int(255.99 * g)
            ib: int = int(255.99 * b)
            print(str(ir) + " " + str(ig) + " " + str(ib) + "\n")
            outputImage.write(str(ir) + " " + str(ig) + " " + str(ib) + "\n")

    # Makes sure to close the output image.
    outputImage.close()


main()
