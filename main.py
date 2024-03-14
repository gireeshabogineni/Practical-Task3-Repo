def calculation(x, y, operator):

    if operator == '+':

        total = x + y
        return total
    elif operator == '-':

        total = x - y
        return total
    elif operator == 'x':

        total = x * y
        return total
    elif operator == '/':

        total = x / y
        return total
    

num1 = float(input("please enter a number : "))
num2 = float(input("please enter a number : "))
operator = input("Enter the any one math symbol (+,-,x,/) : ")

calc = calculation(num1, num2, operator)
print(calc)