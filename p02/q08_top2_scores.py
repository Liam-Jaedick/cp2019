scores = {}
def grades(name, score):
    scores[name] = score
    
num_student = int(input("Number of Students: "))

x = 0

while x < num_student:
    n = input("Name: ")
    s = input("Score:")
    grades(n,s)
    x = x+1

print(max(scores))
scores.pop(max(scores))
print(max(scores))
