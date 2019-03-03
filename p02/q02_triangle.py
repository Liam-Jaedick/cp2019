s1 = int(input("Enter side 1(cm): "))
s2 = int(input("Enter side 2(cm): "))
s3 = int(input("Enter side 3(cm): "))

if s1 >= s2 + s3 or s2 >= s1 + s3 or s3 >= s1 + s2:
    print("Invalid triangle!")
else: 
    print("Perimeter is " + str(s1 + s2 + s3) + "cm")
