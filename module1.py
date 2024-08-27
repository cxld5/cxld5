# basic_script.py

def main():
    # Print a greeting message
    print("Hello,Your about to me signed out ")

    # Ask for user input
    name = input("HAHA get hacked  ")

    # Print a personalized message
    print(f"your gonna get loged out")

    # Perform a simple calculation
    try:
        number1 = float(input("Enter the first number: "))
        number2 = float(input("Enter the second number: "))
        sum = number1 + number2

        # Display the result
        print(f"The sum of {number1} and {number2} is {sum}.")
    except ValueError:
        print("Invalid input. Please enter valid numbers.")

# Ensure the script runs only if executed directly
if __name__ == "__main__":
    main()
