n1 = eval(input("Enter first integer: "))
n2 = eval(input("Enter first integer: "))

GCD = 1 
k = 2

while k<= n1 and k<= n2:
    if n1%k == 0 and n2%k==0:
        GCD = k
    k+=1

print("The greatest common divisor for",n1,"and",n2,"is", GCD)