terminate=False
while not terminate:
    number1=int(input("Please input a number:"))
    number2=int(input("Please enter another number: "))
    while True:
        operation=input("Please enter add/sub or quit to exit:")
        if operation =="quit":
           terminate=True
           break
        if operation not in ["add","sub"]:
            print("Unknown operation!")
            continue
        if operation=="add":
            print("Result is",number1+number2)
            break
        if operation=="sub":
            print("Result is", number1-number2)
            break
    break