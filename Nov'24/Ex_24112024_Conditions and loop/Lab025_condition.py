a = int(input("enter your age"))
if a >= 18:
    print(r"you are allowed to \n vote")
else:
    print("you are not allowed to vote")

x = float(input("enter 1st value"))
y = float(input("enter 2nd value\n"))
z = float(input("enter 3d value\n"))

if x > y and x > z: print("max value is", x)
elif y > x and y > z: print("max value is", y)
else:print("max value is", z)
