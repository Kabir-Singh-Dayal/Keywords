x=int(input("Enter the numbers you want printed"))
s=int(input("Enter number to be skipped"))
x+=1
while x>0:
    x -= 1
    if x==s:
        continue
    print("The number is", x)
    