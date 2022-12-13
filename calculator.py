# This line of code does the addtion
def add(a, b):
   return a + b
# This one if for subtraction
def subtract(a, b):
   return a - b
# This if for multiplication
def multiply(a, b):
   return a * b
# And this of for divison
def divide(a, b):
    return a / b
A = int(input("Enter first number: "))
print("Select an operation.")
print("+")
print("-")
print("*")
print("/")
# User input
choice = input("Enter operator to use:")
B = int(input("Enter second number: "))
if choice == '+':
   print(A,"+",B,"=", add(A,B))
elif choice == '-':
   print(A,"-",B,"=", subtract(A,B))
elif choice == '*':
   print(A,"*",B,"=", multiply(A,B))
elif choice == '/':
   print(A,"/",B,"=", divide(A,B))
else:
    print("Invalid input")
