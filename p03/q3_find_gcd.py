def gcd(m, n):
    while n:
        m, n = n, m % n
    return m

num1 = int(input("Enter First Number: "))
if 
num2 = int(input("Enter First Number: "))

print("The greatest common divisor is " + str(gcd(num1, num2)))
