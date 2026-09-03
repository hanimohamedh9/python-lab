from utils import square, is_even, celsius_to_fahrenheit

def main():
    try:
        user_input = float(input("Enter a number: "))
        
        sq = square(user_input)
        even_status = "Even" if is_even(user_input) else "Odd"
        fah = celsius_to_fahrenheit(user_input)
        
        print(f"Square: {sq}")
        print(f"Status: {even_status}")
        print(f"Fahrenheit equivalent: {fah}°F")
    except ValueError:
        print("Please enter a valid numeric value.")

if __name__ == "__main__":
    main()

    worksheet
    Written Explanation of Python's Import System
​Python’s import system connects main.py to utils.py by locating the external module file within the project's directory structure and loading its definitions into the execution namespace.
​When main.py executes the statement from utils import square, is_even, celsius_to_fahrenheit, the following occurs:
​Module Resolution: Python searches the directory containing the current script (src/) as well as the working directory to find a file named utils.py.
​Execution: Once located, Python executes the code inside utils.py to build the function objects in a separate module namespace.
​Namespace Binding: The from...import syntax extracts only the specified functions (square, is_even, and celsius_to_fahrenheit) and injects them directly into main.py's local symbol table, allowing them to be invoked locally just like functions defined within the same file.

Terminal Output and Testing Confirmation
​The program was tested with three distinct numeric inputs (4, 5, and 10), producing the following terminal output:
PS C:\Users\user\python_lab> python src/main.py
Enter a number: 4
Square: 16.0
Status: Even
Fahrenheit equivalent: 39.2°F

PS C:\Users\user\python_lab> python src/main.py
Enter a number: 5
Square: 25.0
Status: Odd
Fahrenheit equivalent: 41.0°F

PS C:\Users\user\python_lab> python src/main.py
Enter a number: 10
Square: 100.0
Status: Even
Fahrenheit equivalent: 50.0°F