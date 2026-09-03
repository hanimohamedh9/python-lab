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
