n = int(input("Enter number to be checked till"))
for i in range(n+1):
    if i%3==0:
        print("Python")
    elif i%20==0:
        print("Psuedo Code")
    elif i%5==0:
        print("Java")
    elif i%7==0:
        print("R")
    else:
        print(i)