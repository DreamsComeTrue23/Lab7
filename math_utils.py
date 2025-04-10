def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        print("Cannot divide by zero")
    else:
        return x / y


def power(x, y):
    return x ** y


def mod(x, y):
    if y == 0:
        print("Cannot be modded by zero")
    else:
        return x % y


if __name__ == "__main__":
    print("Testing")
    print("6 + 8=", add(6 + 8))
    print("6 - 8=", subtract(6 + 8))
    print("6 % 8=", mod(6 + 8))
    print("6 * 8=", multiply(6 + 8))
    print("6 / 0=", divide(6 + 0))
    print("6 ** 8=", power(6 + 8))
