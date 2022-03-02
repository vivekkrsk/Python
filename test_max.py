def max(i1,i2):
    if i1>i2:
        result = i1
    else:
        result = i2
    
    return result

def main():
    i = eval(input("Enter a number:"))
    j = eval(input("Enter an another number number:"))
    k = max(i,j)
    print("The larger number of",i ,"and",j,"is",k)

main()