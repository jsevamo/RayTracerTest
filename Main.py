# /*******************************************************
# * 2020 Juan Sebastián Vargas Molano j.sevamo@gmail.com
# *******************************************************/

# https://github.com/Keeeweee/Raytracing-In-One-Weekend-in-Python Add randomInUnitSphere method

# TODO: CHECK HOW Hit_Records ARE BEING HANDLED WHEN RENDERING THE WORLD.

from PIL import Image
import cv2
from RayTracerTest.Vec3 import Vec3 as vec3
from RayTracerTest.Ray import Ray as ray
from playsound import playsound
import math
from RayTracerTest.Sphere import *
from RayTracerTest.HittableList import *
from RayTracerTest.Hittable import *
from RayTracerTest.Sphere import *
from RayTracerTest.Camera import *
import sys

# /*******************************************************
# from PIL import Image
# import cv2
# from RayTracerTest.Vec3 import Vec3 as vec3
# from RayTracerTest.Ray import Ray as ray
# from playsound import playsound
# *******************************************************/

# Used to determine t_max for our ray. For now it's at infinity!
MAXRANGE: float = math.inf


# # Not used anymore. Used with GetColorOfPixels. Since we use a world now, this is in Sphere class
# def Hit_Sphere(center: vec3, radius: float, r: ray):
#     """
#
#     :rtype: float
#     """
#
#     # To add a sphere, we can use: (X - Cx)² + (Y - Cy)² + (Z - Cz)² = R²
#     # In vector form we have dot((P-C),(P-C)) = R²
#     # And since our ray is P(t) = A + t*B
#     # Then we have dot((A + t*B - C), (A + t*B - C) = R²
#     # Doing some algebra we then have:
#     # dot(B,B) t² + dot(B, A - C) * 2t + dot(A-C, A-C) - R² = 0
#     # which is an equation in the form of:
#     # aX² + bX + c = 0
#     # Now the discriminant is b² - 4*a*c
#     # if that is greater than zero, we have a valid solution, meaning
#     # the ray hit the sphere.
#     # So then we return the complete solution for t, but the smallest value.
#
#     oc: vec3 = r.GetOrigin - center
#     a: float = vec3.DotProduct(r.GetDirection, r.GetDirection)
#     b: float = 2.0 * vec3.DotProduct(oc, r.GetDirection)
#     c: float = vec3.DotProduct(oc, oc) - radius * radius
#     discriminant: float = b * b - 4 * a * c
#
#     if discriminant < 0:
#         return -1.0
#     else:
#         return (-b - math.sqrt(discriminant)) / (a * 2.0)


# # Not used anymore. Replaced by GetColorOfPixelsWithWorld
# # Returns a Vector3D with the color of the pixel based on where the ray is.
# def GetColorOfPixels(r: ray):
#     """
#
#     :rtype: Vec3
#
#     """
#     # if Hit_Sphere(vec3(0, 0, -1), 0.5, r):
#     #    return vec3(1, 0, 0)
#
#     # To get the color of the pixel, we see first the value of t. It can be -1 or any number
#     # greater than 0 if it hit a sphere.
#     t: float = Hit_Sphere(vec3(0, 0, -1), 0.5, r)
#
#     # If the ray hit the sphere, we get the exact point of where it got it by using PointAtParamenter(), and
#     # subtract the sphere's position from the hit position in order to get the normal vector at hit point.
#     # We then make this normal vector an unit vector.
#     # And finally we make a standard graphics trick to have the normal be from -1 -> 1 to 0 -> 1
#     if t > 0.0:
#         N_notUnit: vec3 = r.PointAtParameter(t) - vec3(0, 0, -1)
#         N_notUnit.MakeUnitVector()
#         N: vec3 = N_notUnit
#         return vec3(N.x + 1, N.y + 1, N.z + 1) * 0.5
#
#     # We get the direction of the ray, make it a unit vector.
#     Direction: vec3 = r.GetDirection
#     Direction.MakeUnitVector()
#     unitDirection: vec3 = Direction
#     # We make a standard graphics trick in which we take the unit direction,
#     # add one and multiply by 0.5. This is to have 0 < t < 1 instead of -1 < t < 1
#     # t starts with high values and decreases as the ray goes down the image with it's "y" value.
#     t = 0.5 * (unitDirection.y + 1)
#     # Color white to use
#     color1: vec3 = vec3(1.0, 1.0, 1.0)
#     # Color blueish to use
#     color2: vec3 = vec3(0.5, 0.7, 1.0)
#
#     # We make a linear interpolation between the two colors based on the value of t using (1-t)A + tB
#     return color1 * (1.0 - t) + color2 * t

def RandomInUnitSphere() -> vec3:
    # p: vec3 = vec3(0, 0, 0)

    while True:
        p: vec3 = (vec3(RandomFloat(), RandomFloat(),
                        RandomFloat()) * 2.0) - vec3(1, 1, 1)
        if p.SquaredLength >= 1.0:
            return p


def GetColorOfPixelsWithWorld(r: ray, world: Hittable):
    # If we hit something in the world, return the normal vector of that pixel and do the graphics trick.
    rec = [Hit_Record()]
    if world.Hit(r, 0, MAXRANGE, rec):
        # return (rec[0].normal + vec3(1, 1, 1)) * 0.5
        target: vec3 = rec[0].p + rec[0].normal + RandomInUnitSphere()
        return GetColorOfPixelsWithWorld(ray(rec[0].p, target - rec[0].p), world) * 0.5
    else:
        Direction: vec3 = r.GetDirection
        Direction.MakeUnitVector()
        unitDirection: vec3 = Direction
        # We make a standard graphics trick in which we take the unit direction,
        # add one and multiply by 0.5. This is to have 0 < t < 1 instead of -1 < t < 1
        # t starts with high values and decreases as the ray goes down the image with it's "y" value.
        t = 0.5 * (unitDirection.y + 1)
        # Color white to use
        color1: vec3 = vec3(1.0, 1.0, 1.0)
        # Color blueish to use
        color2: vec3 = vec3(0.5, 0.7, 1.0)

        # We make a linear interpolation between the two colors based on the value of t using (1-t)A + tB
        return color1 * (1.0 - t) + color2 * t


# Main function for the raytracer
def Main():
    sys.setrecursionlimit(5000)

    # This is how we can create a ppm image to write.
    outputImage = open("renderedImage.ppm", "w+")

    # width (nx) and height (ny) of the output image.
    nx: int = 400
    ny: int = 200
    # Number of samples per pixel for antialiasing. The more samples the better the effect
    # but takes longer to render.
    samples: int = 1

    # create a ppm image header based on this: https://en.wikipedia.org/wiki/Netpbm#File_formats
    # print("P3\n" + str(nx) + " " + str(ny) + "\n255\n")
    outputImage.write("P3\n" + str(nx) + " " + str(ny) + "\n255\n")

    # Create a world of type HittableList to add HittableO Objects (Spheres)
    world = HittableList()
    # Adds two spheres. The first one is so big we just see the top and looks like a floor. Cool!
    world.append(Sphere(vec3(0, -100.5, -1), 100))
    world.append(Sphere(vec3(0, 0, -1), 0.5))

    # Created a camera to better handle rendering.
    cam = Camera()

    # The for loop that writes the pixels of the image. It writes from left to right
    # and then from top to bottom.
    for j in range(ny, 0, -1):
        for i in range(0, nx, 1):

            # # THIS WAS REPLACED BY THE CAMERA CLASS. iT'S DONE THERE NOW.
            #
            # # U and V are vectors inside de image plane. They go from 0 to 1.
            #
            # # If U is 0 and V is 1, it means we are pointing are the top left corner of the image plane.
            #
            # # They are necessary to move the ray through each pixel, as with each iteration in the for loop,
            # # they change values.
            #
            # u: float = i / nx
            # v: float = j / ny
            #
            # # Next is the magic formula that moves the Ray through all the pixels of the image.
            #
            # # We give the ray it's origin, but then here's the good part:
            # # for the Direction, we start with the lower left corner that was set before,
            # # but then we add to this position the horizontal size of the plane time u.
            # # This is crucial because since U goes from 0 to 1, it effectively makes it so
            # # we do indeed go through the whole plane.
            # # Same goes for vertical size time V.
            # r: ray = ray(originOfCamera, lowerLeftCorner + horizontalSize * u + verticalSize * v)
            # # col: vec3 = GetColorOfPixels(r)
            # col: vec3 = GetColorOfPixelsWithWorld(r, world)

            # Rendering now using the camera object and testing if we want to render with
            # antialiasing or not.

            # So the color of each pixel now starts as black.
            col: vec3 = vec3(0, 0, 0)

            # If we use antialiasing, now for each given pixel we also have a loop that sends rays
            # with values +1 or -1 of the original u and v coordinates using the RandomFloat function in Camera.
            # This ensures each pixel now gets a color sample of slightly shifted rays.
            # Everytime we get a color back we add it to the original color variable of the pixel,
            # and then divide by the amount of rays we shot per pixel (samples) in order to average the colors and
            # get proper antialiasing. Cool!
            for s in range(0, samples, 1):
                u: float = (i + RandomFloat()) / nx
                v: float = (j + RandomFloat()) / ny
                r: ray = cam.GetRay(u, v)
                col = col + GetColorOfPixelsWithWorld(r, world)

            col = col / samples

            col = vec3(math.sqrt(col.r), math.sqrt(col.g), math.sqrt(col.b))

            ir: int = int(255.99 * col.r)
            ig: int = int(255.99 * col.g)
            ib: int = int(255.99 * col.b)

            # It's necessary to check later what is going on. For now, here's a quick fix:
            # if ir < 0:
            #     ir = 0
            # if ir > 255:
            #     ir = 255
            # if ig < 0:
            #     ig = 0
            # if ig > 255:
            #     ig = 255
            # if ib < 0:
            #     ib = 0
            # if ib > 255:
            #     ib = 255

            print(str(ir) + " " + str(ig) + " " + str(ib) + "\n")
            outputImage.write(str(ir) + " " + str(ig) + " " + str(ib) + "\n")

    # Makes sure to close the output image.
    outputImage.close()
    print("Image Rendered Correctly! Success!")
    print("The Rendering engine works!")
    print("You suck a little bit less today!")
    print("Rejoice!")
    ShowImage()
    playsound('victory.mp3')


# Uses OpenCV to change the format of the rendered image from PPM to JPG, and then uses Pillow (PIL) to show it.
def ShowImage():
    i = cv2.imread('renderedImage.ppm')
    cv2.imwrite('renderedImage.jpg', i)
    img = Image.open('renderedImage.jpg')
    img.show()


Main()
