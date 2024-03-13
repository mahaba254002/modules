# Constant attribute
PI = 3.14159

# Formulas
def area_of_circle(radius):
    return PI * radius ** 2

def circumference_of_circle(radius):
    return 2 * PI * radius

def area_of_rectangle(length, width):
    return length * width

def perimeter_of_rectangle(length, width):
    return 2 * (length + width)

def area_of_triangle(base, height):
    return 0.5 * base * height

def perimeter_of_triangle(side1, side2, side3):
    return side1 + side2 + side3

def volume_of_sphere(radius):
    return (4 / 3) * PI * radius ** 3

def surface_area_of_sphere(radius):
    return 4 * PI * radius ** 2

def area_of_cylinder(radius, height):
    return 2 * PI * radius * (radius + height)

def volume_of_cylinder(radius, height):
    return PI * radius ** 2 * height