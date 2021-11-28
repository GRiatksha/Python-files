def MultiplyAnyNumberOfInputs(*args):
    result = 1
    for i in args:
        result *= i
        print(i, ": number", type(i), f"result = {i} * {result} =", result)

    return result


product = MultiplyAnyNumberOfInputs(1, 2, 3, 4)
print(product)
x = "1"
y = "2"
print(x + y)