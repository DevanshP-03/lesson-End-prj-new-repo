import os

def greet_user(name):
    print(f"Hello, {name}! Welcome to GitHub + Python demo.")

def add_numbers(a, b):
    return a + b

if __name__ == "__main__":
    greet_user("Devansh")

    # Get input values from environment variables
    num1 = int(os.environ.get("NUM1", 0))
    num2 = int(os.environ.get("NUM2", 0))

    result = add_numbers(num1, num2)
    print(f"Sum is: {result}")
