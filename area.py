PI=3.14
r=float(input("input the radius of the circle:"))
area=PI*r*r
print("The area of the circle with radius",r, "is = %.2f" %area)
filename=input("input the filename:")
f_extns=filename.split(".")
print("The extension of the file is:" +repr(f_extns[-1]))
