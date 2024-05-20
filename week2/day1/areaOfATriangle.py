'''
1/2 base * height
'''

def AreaOfATriangle(base , height):
    area = (base * height)/2
    return area

# Output
print("Area of a triangle:")
base = int(input("Enter the base: "))
height = int(input("Enter the height: "))
area = AreaOfATriangle(base , height)

print(f"The area of a triangle is: {area}")

