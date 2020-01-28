# /*******************************************************
# * 2020 Juan Sebastián Vargas Molano j.sevamo@gmail.com
# *******************************************************/

# importing the 3D Vector class called Vec3 that is in another file called Vec3.py
from Vec3 import Vec3 as vec3


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
            # Just random numbers for now to create an image.

            col = vec3(i/nx, j/ny, 0.8)

            ir: int = int(255.99 * col.r)
            ig: int = int(255.99 * col.g)
            ib: int = int(255.99 * col.b)
            print(str(ir) + " " + str(ig) + " " + str(ib) + "\n")
            outputImage.write(str(ir) + " " + str(ig) + " " + str(ib) + "\n")

    # Makes sure to close the output image.
    outputImage.close()


main()

