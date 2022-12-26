def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


input_num = int(input("Enter a number: "))
result = factorial(input_num)
print(f"Factorial of {input_num}: {result}")
