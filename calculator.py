import math_utils


def main():
    num1 = int(input('Please enter the first number:'))
    num2 = int(input('Please enter second number:'))

    operator = input('Please enter the operator(+, -, *, /, %, **')

    ops = {
        '+': math_utils.add,
        '-': math_utils.subtract,
        '*': math_utils.multiply,
        '/': math_utils.divide,
        '%': math_utils.mod,
        '**': math_utils.power
    }

    if operator in ops:
        result = ops[operator](num1, num2)
        print(result)
    else:
        print('Invalid operation')


if __name__ == "__main__":
    main()
