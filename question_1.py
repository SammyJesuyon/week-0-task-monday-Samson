def factorial(x):
    result = 1
    for num in range(1, (x+1)):
        result = num * result
    print("The factorial of", x, "is", result)
factorial(4)