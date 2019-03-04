def m_series(i):
    num = 0
    for x in range(0, i + 1):
        num += x / (x + 1)
    return format(num, '.4f')
    
print("i   :   m(i)")
for i in range(21):
    print(i ," " * (2 - len(str(i))),
          ":", f"{m_series(i)}", " " * (9 - len(str(m_series(i)))))
