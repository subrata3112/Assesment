x = int(input("Enter a number for x: "))
y = int(input("Enter a number for y: "))
a = int(input("Enter a number for a: "))
b = int(input("Enter a number for b: "))

ans = (((x+(1/y))**a)*((x-(1/y))**b))/(((y+(1/x))**a)*((y-(1/x))**b))
print(ans)
