# print(1+2*2//4-5)
width = 19
height = 5*9
# print(height % width)

# print(2**100)

# print((3+3)*2/4**3)

com1 = 1+2j
com2 = 1-2j
print(com1 + com2)
print(com1 - com2)
print(com1 * com2)
print(12**2-12*4)

num1 = float(input("Enter first number: "))
op = input("Enter operator: ")
num2 = float(input("Enter second number: "))

if op ==  "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "/":
    print(num1 / num2)
elif op == "*":
    print(num1 * num2)
else:
    print("Invalid operator")

