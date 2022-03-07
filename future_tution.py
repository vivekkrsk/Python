year = 0
tution = 10000

while tution < 20000:
    year += 1
    tution = tution*1.07

print("Tution will be doubled in", year, "Years")
print("Tuiton will be $"+format(tution,".2f"),"in",year,"Years")