# 25. Write a program to simulate a simple calculator (add, subtract, multiply, divide).
class result:
	def add(a,b):
		return a+b
	def sub(a,b):
		return a-b
	def multiply(a,b):
		return a*b
	def divide(a,b):
		if b == 0:
			return "0 division error"
		return a/b

a = int(input("a= "))
b = int(input("b= "))
op = input("+,-,*,/  : ")

if op == "+": 
	re = result.add(a,b)
elif op == "-":
	re = result.sun(a,b)
elif op == "*":
	re = result.multiply(a,b)
elif op == "/":
	re = result.divide(a,b)
else:
	print("Invalid operator")
 
print(f"Result: {re}")
# This code implements a basic calculator that can perform addition, subtraction, multiplication, and division.
# It prompts the user for two numbers and an operator, then performs the corresponding operation.   
