def calculate_pi(iterations):
    """Calculate an approximation of PI using the given number of iterations."""
    pi_approximation = 0
    for i in range(iterations):
        # Add or subtract terms based on the series
        term = (-1) ** i / (2 * i + 1)
        pi_approximation += term
    return 4 * pi_approximation

def main():
    print("Welcome to the PI Approximation Program!")
    while True:
        try:
            # Prompt user for number of iterations
            user_input = input("Enter the number of iterations (or type 'exit' to quit): ").strip()
            if user_input.lower() == "exit":
                print("Goodbye!")
                break
            iterations = int(user_input)
            if iterations < 1:
                print("Please enter a positive integer.")
                continue
            
            # Calculate and display the approximation
            pi_value = calculate_pi(iterations)
            print(f"Approximation of PI after {iterations} iterations: {pi_value}")
        
        except ValueError:
            print("Invalid")

if __name__ == "__main__":
    main()
