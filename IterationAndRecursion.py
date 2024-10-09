def factorial_iterative_while(n):
    # Special case for 0! = 1
    if n == 0:
        return 1
    
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)

# Function to print factorial results using both methods
def print_factorial_results():
    numbers = [2, 6, 12, 18, 24, 120]
    
    # Iterative results
    print("Factorial results using an iterative function")
    for num in numbers:
        print(f"{num}! = {factorial_iterative_while(num)}")

    # Recursive results
    print("\nFactorial results using a recursive function")
    for num in numbers[:-1]:
        print(f"{num}! = {factorial_recursive(num)}")
        
# Run the function to display results
print_factorial_results()
