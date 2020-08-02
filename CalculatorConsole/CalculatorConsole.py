num1 = 0
num2 = 0
result = 0
def Addition(n1,n2):
    return n1 + n2
def Subtraction(n1,n2):
    return n1 - n2
def Multiplication(n1,n2):
    return n1 * n2
def Division(n1,n2):
    return n1 / n2
print("Press 1 for Addition \nPress 2 for subtraction \nPress 3 for multiplication \nPress 4 for division \nPress 0 for Exit \n")
while True:
    choise = int(input("enter choise"))
    if choise == 0:
        break
    num1 = (int(input("Enter first number")))
    num2 = (int(input("Enter second number")))
    if choise == 1:
        result = Addition(num1,num2)
    if choise == 2:
        result = Subtraction(num1,num2)
    if choise == 3:
        result = Multiplication(num1,num2)
    if choise == 4:
        result = Division(num1,num2)
    resultSting="The result is {}"
    print(resultSting.format(result))