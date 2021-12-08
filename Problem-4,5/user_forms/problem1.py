def meth1(x,n):

    sum=0.00
    for i in range(n):
        sum += (1/(x**(i+1)))

    return sum

def meth2(x,n):

    if n == 0:
        return 0
    else:
        return (1/(x**n)) + meth2(x,n-1)

# x = int(input("Enter a number: "))
# n = int(input("Enter a number: "))

# print(meth1(x,n))
# print(meth2(x,n))
