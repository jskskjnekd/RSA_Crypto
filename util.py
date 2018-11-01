"""
:: 11/1/18   1:14 PM
:: extended GCD
    A general method for solving
        Xa + Yb = GCD(a,b)
    @input:
        a, b
    @output
        X, Y
"""


def extGCD(a, b):
    prev_x = 1
    x = 0
    prev_y = 0
    y = 1
    while (b != 0):
        q = int(a / b)
        tempX1 = prev_x - q * x
        tempX2 = x
        x = tempX1
        prev_x = tempX2
        tempY1 = prev_y - q * y
        tempY2 = y
        prev_y = tempY2
        y = tempY1
        temp_b = a % b
        temp_a = b
        a = temp_a
        b = temp_b
    print(a, prev_x, prev_y)
    return prev_x, prev_y


if __name__ == '__main__':
    extGCD(8, 11)
    extGCD(42823, 6409)
