import math
  
radius =float(input("Enter radius of a circle "))
#cicle circumference formula is => 2*pi*radius
circumference = 2 * math.pi * radius
print(f"cicumference of the circle is: {round(circumference,2)} cm")

#circle Area formula is => pi * r²
Area = math.pi * pow(radius,2)
print(f"Area of the circle is: {round(circumference,2)} cm²")


print("Now we will be finding hypotenuse of a right angle triangle")

height = float(input("Enter a height of a right angle triangle: "))
base = float(input("Enter a base of a right angle triangle: "))
hypotenuse = math.sqrt ( pow(height,2) + pow(base,2))
print(f"The hypotenuse of a right angle trianle is: {round(hypotenuse,2)}")


