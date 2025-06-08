def greet_user(name):
    print(f"Hello, {name}! Welcome to GitHub + Python demo.")

def add_numbers(a, b):
    return a + b

if __name__ == "__main__":
    greet_user("Devansh")

    # Take input from the user
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    result = add_numbers(num1, num2)
    print(f"Sum is: {result}")
