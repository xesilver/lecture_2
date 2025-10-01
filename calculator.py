# Calculator functions
def add(x, y):
    return x + y

def sub(x, y):
    return x - y


# Get user input
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
op = input("Enter operation (+, -, *, /): ")

# Calculate and display result
if op == '+':
    print(add(a, b))
elif op == '-':
    print(sub(a, b))
else:
    print("Invalid operation")
