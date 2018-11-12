import os

"""
:: 11/12/18   12:26 PM
:: GCD
    @input 
        x, y
    @output
        highest common factor
"""


def GCD(x, y):
    while (y):
        x, y = y, x % y
    return x



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
    N = p * q
    One_p = (Y * q) % N
    One_q = (X * p) % N
    return (x_p * One_p + x_q * One_q) % N


"""
:: 11/1/18   4:01 PM
:: quickExpMod
    @input
        base:   message int
        power:  value of power
        N:
    @output
        m^(power) mod N
"""


def quickExpMod(base, power, N):
    result = base
    for i in bin(power)[3:]:
        result = (result * result) % N
        if int(i) == 1:
            result = (result * base) % N
    return result


"""
:: 11/1/18   4:39 PM
:: determine if the number is prime or not
    @input:
        val
    @output:
        bool
"""


def isPrime(val):
    securityNum = 30  # security level, if pass, the error rate is less than 2**(-s)
    lenValByte = int(val.bit_length() / 8)
    i = 0
    while (i < securityNum):
        randomChallenge = byteToint(os.urandom(lenValByte))
        if (randomChallenge > 1) and (randomChallenge < val - 2):
            i += 1
            if quickExpMod(randomChallenge, val - 1, val) != 1:
                return False
    return True


"""
:: 11/1/18   4:39 PM
:: Generate a prime number at bits N
    @input:
        N     :    number of bits (512/1024/2048......)
    @output:
        primeVal  
"""


def generatePrime(numBits):
    i = 0  # i is the tracker of simulation times. To find a prime, the expected simulation time is 177*2
    while (i < 1000):
        primeVal = byteToint(os.urandom(int(numBits / 8)))
        if primeVal % 2 == 1:
            if isPrime(primeVal):
                print("find prime number:\n\t", primeVal)
                print("\tHex:\t", hex(primeVal))
                return primeVal
    print("Failed the search of prime number")


"""
:: 11/1/18   4:16 PM
:: Byte array to integer
"""


def byteToint(byteArray):
    result = 0
    for i in byteArray:
        result = result * 256 + int(i)
    return result


if __name__ == '__main__':
    extGCD(8, 11)
    extGCD(42823, 6409)
    extGCD(11, 13)
    extGCD(5, 7)
    print(mappingX(5, 7, 4, 3))
    print(mappingX(11, 13, 9, 11))
    # print((bin(123)))
    print((bin(2 ** 50 - 976)))
    print("-" * 20)

    base = byteToint(os.urandom(int(256 / 8)))
    print("base ", base)
    power = byteToint(os.urandom(int(512 / 8)))
    print("power ", power)
    N = 2535301200456458802993406410833
    quickExpMod(base, power, N)
    # quickExpMod()
    isPrime(2098893665744058648615126425661022259386391)
    generatePrime(512)
