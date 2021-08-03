a=int(input("Enter First No. Here: "))
b=int(input("Enter Second No. Here: "))
c=int(input("Enter Third No. Here: "))
if a>b and a>c :
    if b>c:
        print("The Second Largest No. is ",b)
    else:
        print("The Second Largest No. is ",c)
elif b>a and b>c:
    if a>c:
        print("The Second Largest No. is ",a)
    else:
        print("The Second Largest No. is ",c)
else:
    if a>b:
        print("The Second Largest No. is ",a)
    else:
        print("The Second Largest No. is ",b)