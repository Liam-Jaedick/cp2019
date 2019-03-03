def kgtop(mass):
    p = mass*2.2
    return p

print("Kilograms ",'\t',"Pounds")

for i in range(11):
    print(str(i),'              ',"{:.2f}".format(kgtop(i)))
