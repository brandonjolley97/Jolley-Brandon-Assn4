import math


title = "Cuboid Calculator.  If you would like to calculate your cuboid, please enter a number in feet when prompted."
print(title)
length = eval(input("Length:"))
width = eval(input("Width:"))
height = eval(input("Height:"))
surfaceArea = (2 * length * width) + (2 * length * height) + (2 * height * width)
volume = length * width * height
print("Your cuboid has dimensions of", length, "X", width, "X", height, "with a surface area of", surfaceArea, "feet squared and a volume of", volume, "feet cubed.")
