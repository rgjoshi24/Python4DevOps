import os
import sys

def add(num1, num2):
    sum = num1 + num2
    return sum

def sub(num1, num2):
    diff = num1 - num2
    return diff

def mul(num1, num2):
    prod = num1 * num2
    return prod

num1 = float(sys.argv[1])
operator = sys.argv[2]
num2 = float(sys.argv[3])
# num2 = sys.argv[3]
# print(num2)

if operator == "+":
    result = add(num1, num2)
elif operator == "-":
    result = sub(num1, num2)
elif operator == "mul":
    result = mul(num1, num2)
else:
    print("Invalid Operator, operator has to be +, - or mul.")

print("The result is:", result)

print("The value of env variable $TEST_ENV_VAR is", os.getenv("TEST_ENV_VAR"))

