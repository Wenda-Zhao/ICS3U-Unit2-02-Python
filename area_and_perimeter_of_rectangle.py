#!/usr/bin/env python3

# Created by Wenda Zhao
# Created on Nov 2020
# This program calculates the area and perimeter of a rectangle
#     with user input


def main():
    # This function calculates the area and perimeter

    # input
    length = int(input("Enter length of the rectangle (mm): "))
    width = int(input("Enter width of the rectangle (mm) "))

    # process
    area = length*width
    perimeter = 2*(length+width)

    # output
    print("")
    print("Area is {}mm²".format(area))
    print("Perimeter is {}mm".format(perimeter))


if __name__ == "__main__":
    main()
