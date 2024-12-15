import math

# Define a base Calculator class
class Calculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y == 0:
            return "Error! Division by zero."
        return x / y


# Define a ScientificCalculator class that inherits from Calculator
class ScientificCalculator(Calculator):
    def square_root(self, x):
        if x < 0:
            return "Error! Negative value cannot have a square root."
        return math.sqrt(x)

    def power(self, x, y):
        return math.pow(x, y)

    def sine(self, x):
        return math.sin(math.radians(x))

    def cosine(self, x):
        return math.cos(math.radians(x))

    def tangent(self, x):
        return math.tan(math.radians(x))

    def logarithm(self, x, base=10):
        if x <= 0:
            return "Error! Logarithm undefined for non-positive values."
        if base == 'e':
            return math.log(x)
        return math.log(x, base)


# Define the interface to interact with the user
def main():
    print("Welcome to the Scientific Calculator!")
    calc = ScientificCalculator()

    while True:
        print("\nSelect an operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Square Root")
        print("6. Power")
        print("7. Sine")
        print("8. Cosine")
        print("9. Tangent")
        print("10. Logarithm")
        print("11. Exit")

        choice = input("Enter your choice (1-11): ")

        if choice == '11':
            print("Exiting... Thank you for using the calculator!")
            break

        if choice in ['1', '2', '3', '4', '6']:
            x = float(input("Enter the first number: "))
            y = float(input("Enter the second number: "))

        if choice == '1':
            print(f"{x} + {y} = {calc.add(x, y)}")
        elif choice == '2':
            print(f"{x} - {y} = {calc.subtract(x, y)}")
        elif choice == '3':
            print(f"{x} * {y} = {calc.multiply(x, y)}")
        elif choice == '4':
            print(f"{x} / {y} = {calc.divide(x, y)}")
        elif choice == '5':
            x = float(input("Enter the number: "))
            print(f"Square root of {x} = {calc.square_root(x)}")
        elif choice == '6':
            print(f"{x} raised to the power of {y} = {calc.power(x, y)}")
        elif choice == '7':
            x = float(input("Enter the angle in degrees: "))
            print(f"Sine of {x}° = {calc.sine(x)}")
        elif choice == '8':
            x = float(input("Enter the angle in degrees: "))
            print(f"Cosine of {x}° = {calc.cosine(x)}")
        elif choice == '9':
            x = float(input("Enter the angle in degrees: "))
            print(f"Tangent of {x}° = {calc.tangent(x)}")
        elif choice == '10':
            x = float(input("Enter the number: "))
            base = input("Enter the base (default 10, or 'e' for natural logarithm): ")
            if base == "":
                base = 10
            print(f"Logarithm of {x} with base {base} = {calc.logarithm(x, base)}")
        else:
            print("Invalid choice. Please try again.")

# Run the calculator
if __name__ == "__main__":
    main()
