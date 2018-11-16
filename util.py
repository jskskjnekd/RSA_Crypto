import os
import random
import math

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
:: 11/1/18    1:14 PM
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
        q = int(a // b)
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
:: 11/12/18   12:36 PM
:: inverse modulo
    @input
        phi(n), e
    @output
        t : the inverse of e
            GCD(phi(n), e) = s*phi(n) + t*e
"""


def inverse_mod(phi_n, e):
    s, t = extGCD(phi_n, e)
    if t < 0:
        return phi_n + t
    else:
        return t


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
    # ----------------------
    if (lenValByte == 0):
        if val == 2:
            return True
        else:
            for i in range(2, val):
                if (val % i) == 0:
                    return False
            return True
    # ---------------------
    # print(lenValByte, val.bit_length())
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
    # --- if numBits less than 8
    if (numBits == 1):
        return 2
    elif (numBits == 2):
        return random.choice([2, 3])
    elif (numBits == 3):
        return random.choice([2, 3, 7])
    elif (numBits == 4):
        return random.choice([2, 3, 7, 5, 7, 11, 13])
    elif (numBits == 5):
        return random.choice([2, 3, 7, 5, 7, 11, 13, 17, 19, 23, 29, 31])
    elif (numBits == 6):
        return random.choice([2, 3, 7, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61])
    elif (numBits == 7):
        return random.choice(
            [2, 3, 7, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101,
             103, 107, 109, 113, 127])
    elif (numBits == 8):
        return random.choice(
            [2, 3, 7, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101,
             103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211,
             223, 227, 229, 233, 239, 241, 251])
    # numBits > 8
    while (i < 1000):
        primeVal = byteToint(os.urandom(int(numBits / 8)))
        if primeVal % 2 == 1:
            if isPrime(primeVal):
                # print("find prime number:\n\t", primeVal)
                # print("\tHex:\t", hex(primeVal))
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


"""
:: 11/12/18   2:35 PM
:: Hex to integer
"""


def hexToInt(hexStr):
    return int(hexStr, 16)


"""
:: 11/15/18   11:03 AM
:: Padding
    @input
        n : the final length of padded message in bits
        unpadded_message: uppadded message in bytes
    @output
        padded_message
::
    (0x00 || 0x02 || r || 0x00 || m)
    where r is a random bytes array;
::
    len(padded_message) = n   (in bits)  
"""


def padding(n, unpadded_message):
    print("\n" * 2)
    len_m_inBits_limit = int(n // 2) - 24
    len_r_inBits = n - len(unpadded_message) * 8 - 24
    print("len r in bits:\t", len_r_inBits)
    print("len m in bits:\t", len(unpadded_message) * 8)
    print("total n bits:\t", n, " = ", len_r_inBits, " + 24 + ", 8 * len(unpadded_message))

    if len(unpadded_message) * 8 > len_m_inBits_limit:
        raise ValueError('message size is too big')
    else:
        r = generate_r(len_r_inBits)  
        result = b'\x00\x02' + r + b"\x00" + unpadded_message
        return result


def generate_r(len_r_inBits):
    len_r_inBytes = math.ceil(len_r_inBits // 8)
    r_current_length_inBytes = 0
    r = b""
    while (r_current_length_inBytes != len_r_inBytes):
        randomByte = os.urandom(1)
        if randomByte != b"\x00":
            r += randomByte
            r_current_length_inBytes += 1
    return r
