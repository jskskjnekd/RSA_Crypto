


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


"""
:: 11/1/18   1:33 PM
:: Mapping from (x_p, x_q) to x in Zn*
    @input
        p, q, two co-prime integers
        x_p, x_q
    @output
        x = [(x_p * One_p + x_q * One_q ) % N ]
"""
def mappingX(p, q, x_p, x_q):
    X, Y = extGCD(p, q)
    N = p*q
    One_p = (Y*q) % N
    One_q = (X*p) % N
    return (x_p * One_p + x_q * One_q ) % N








if __name__ == '__main__':
    extGCD(8, 11)
    extGCD(42823, 6409)
    extGCD(11, 13)
    extGCD(5, 7)
    print(mappingX(5,7,4,3))
    print(mappingX(11,13,9,11))
    # print((bin(123)))
    print((bin(2**50-976)))

























