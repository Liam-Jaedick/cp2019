def display_pattern(n):
    x = 1
    while x <= n:
        for i in range(x + 1, n + 1):
            print(" ", end = "")
        print(x, end="")
        if x > 1:
            for z in range(1, x):
                print(x - z, end = "")
        print()
        x += 1

number = int(input("Enter Number: "))
display_pattern(n)
