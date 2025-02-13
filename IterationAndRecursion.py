# Lenora Welborne
# IterationAndRecursion
def factorial_iterative_while(n):
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
def print_factorial_results():
    numbers = [2, 6, 12, 18, 24, 120]
    print("Factorial results using an iterative function")
    for num in numbers:
        print(f"{num}! = {factorial_iterative_while(num)}")
    print("\nFactorial results using a recursive function")
    for num in numbers:
        print(f"{num}! = {factorial_recursive(num)}")
print_factorial_results()
