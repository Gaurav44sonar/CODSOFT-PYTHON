print("         CALCULATOR          ")
print()
n1=int(input("Enter first number: "))
n2=int(input("Enter second number: "))

while True:
    print()
    print("Enter 1: Addition\nEnter 2: Subtraction\nEnter 3: Multiplication\nEnter 4: Division\nEnter 5: Exit")
    choice=int(input())
    if choice==1:
        print()
        print("Addition=",(n1+n2))
    elif choice==2:
        print()
        print("Subtraction=",(n1-n2))
    elif choice==3:
        print()
        print("Multiplication=",(n1*n2))
    elif choice==4:
        print()
        print("Division=",(n1/n2))
    elif choice==5:
        break
    else:
        print("Invalid option")