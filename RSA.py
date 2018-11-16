import util
import os

"""
:: 11/12/18   11:50 AM
:: RSA Encryption
"""


class RSACipher:
    def __init__(self):
        pass

    """
    :: 11/15/18   11:03 AM
    :: Padding
        @input
            N : the final length of padded message in bits
            m : unpadded message in bytes
        @output
            padded_message
    ::
        (0x00 || 0x02 || r || 0x00 || m)
        where r is a random bytes array;
    ::
        len(padded_message) = n   (in bits)  
    """

    def pad(m, N):
        pass
        # n = int(N // 2)
        # if len(m) > len(n):
        #     raise ValueError('message size exceed n bits')
        # else:
        #     r_len = int(n // 2) - 24
        #     pad = b"\0x00\x00" + str(os.urandom(r_len)) + b"\x00"
        #     padded_m = pad + m
        #     print("THIS VALUE SHOULD ALWAYS BE THE SIZE OF n :" + str(len(padded_m)))
        #     return padded_m

    def Encryption(N, e, m):
        """
        :param N:
        :param e:  all from public key
        :param m: message in integer (base 10)
        :return:
            m**e mod N
        """
        return util.quickExpMod(m, e, N)

    def Decryption(N, d, c):
        """
        :param N:
        :param d: all from private key
        :param c: ciphertext
        :return:
            c**d mod N
        """
        return util.quickExpMod(c, d, N)
