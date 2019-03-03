score = int(input("Enter score: "))
if score < 1 or score > 100:
    print("Invalid! Score must be within 0 - 100")
elif 70 <= score <= 100:
    print("Grade: A")
elif 60 <= score <= 69:
    print("Grade: B")
elif 55 <= score <= 59:
    print("Grade: C")
elif 50 <= score <= 54:
    print("Grade: D")
elif 45 <= score <= 49:
    print("Grade: E")
elif 35 <= score <= 44:
    print("Grade: S")
else:
    print("Grade: U")
