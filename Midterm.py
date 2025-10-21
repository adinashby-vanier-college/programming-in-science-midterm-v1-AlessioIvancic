import math

# Q1: Calculate the area of a circle
def area_of_circle(radius):
    return 0.0
    


    

# Q2: Hollow Right Triangle
def hollow_right_triangle(n):
    result = ""

    if n < 4:
        return("The triangle height should be at least 4.")

    for i in range(n):
        for j in range(n):
            if j == i or i == n - 1 or j == 0:
                return ("*" + "\n")
            else:
                return(" " + "\n")
            
    return result.rstrip

# Q3: Inverted Pyramid
def inverted_pyramid(n):
    return ""

# ----------------------------------------------------------------
print(area_of_circle(5))
print()

print(hollow_right_triangle(3))
print()

print(hollow_right_triangle(4))
print()

print(hollow_right_triangle(5))
print()

print(inverted_pyramid(3))
print()

print(inverted_pyramid(4))
print()

print(inverted_pyramid(5))
print()