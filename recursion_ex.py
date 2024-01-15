def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


def main():
    n = 5
    print(f"The factorial of {n} is {factorial(n)}")


main()
