n = int(input("Please enter any number: "))        

def reverse_int(n):
    Number = n
    Reverse = 0
    while(Number > 0):    
        Reminder = Number %10    
        Reverse = (Reverse * 10) + Reminder    
        Number = Number // 10
    return Reverse

if n < 0:
  print("This is a negative number")
if type(n) == int:
  print("Reverse of entered number is: " + str(reverse_int(n)))
if type(n) != int:
  print("This number is not an integer")
