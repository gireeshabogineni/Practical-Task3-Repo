# program to calculate basic arithmetic operations using funtion
def calculation(x, y, operator):

    try:
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
    except ZeroDivisionError:
        print("You cannot divide by Zero.. ")

num1 = float(input("please enter a number : "))
num2 = float(input("please enter a number : "))

ops = ['+', '-', 'x', '/']
# implementing defensive programming using while loop to ensure user entering correct operator
while True:
    operator = input("Enter the any one math symbol (+,-,x,/) : ")

    if operator not in ops:
        print(''' Your selected operator is not vaid.
                Please use of the  math symbol (+,-,x,/) only ''')
        continue
    else:
        print('Calculating...')
        break


calc = calculation(num1, num2, operator)
print(calc)