def mtokm(dist):
    km = dist * 1.609
    return "{:.3f}".format(km)

print("Miles","Kilometers","Kilometres","Miles")

for i in range(1,11):
    print(str(i),'   ',mtokm(i),"    ",str(5*i+20),"       ",mtokm(5*i+20))
