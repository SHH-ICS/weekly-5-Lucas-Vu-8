def calculate_pi(n):
    """Approximate PI using the given number of iterations."""
    return 4 * sum((-1) ** i / (2 * i + 1) for i in range(n))
# Leibniz formula all in one line
def main():
    print("PI Approximation Program")
    while True:
        user_input = input("Enter iterations (or 'exit' to quit): ").strip()
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        if user_input.isdigit():
            n = int(user_input)
            print(f"Approximation of PI after {n} iterations: {calculate_pi(n)}")
        else:
            print("Invalid")

if __name__ == "__main__":
    main()
