from utils import square, is_even, celsius_to_fahrenheit, greet
def main():
    user_name = input("Enter your name: ")
    print(greet(user_name))

    try:
        user_input = float(input("Enter a number: "))

        sq_result = square(user_input)
        even_result = is_even(user_input)
        fahr_result = celsius_to_fahrenheit(user_input)

        parity = "even" if even_result else "odd"

        print(f"\nResults for input: {user_input}")
        print(f"- Square: {sq_result}")
        print(f"- Parity: The number is {parity}.")
        print(f"- Fahrenheit equivalent: {fahr_result}°F\n")

    except ValueError:
        print("Please enter a valid numeric value.")

if __name__ == "__main__":
    main()