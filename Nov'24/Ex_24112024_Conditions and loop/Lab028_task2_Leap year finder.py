a=int(input("Enter the Year\n"))
if a%4 ==0 or a%100==0 and a%400>0:print("it is leap year")
else: print("it is not leap year")