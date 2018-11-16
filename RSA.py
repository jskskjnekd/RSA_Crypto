import util
import os

"""
:: 11/12/18   11:50 AM
:: RSA Encryption
"""

class RSACipher:
    def __init__(self):
        pass
    #expects m to be bytes, N to be integer
    def pad(m,N):
        n = int(N // 2)
        if len(m) > len(n):
            raise ValueError('message size exceed n bits')
        else:
            r_len = int(n//2) - 24
            pad = b"\0x00\x00"+str(os.urandom(r_len))+b"\x00"
            padded_m = pad + m
            print("THIS VALUE SHOULD ALWAYS BE THE SIZE OF n :"+str(len(padded_m)))
            return padded_m






    def Encryption(N, e, m):
        """
        :param N:
        :param e:  all from public key
        :param m: message in integer (base 10)
        :return:
            m**e mod N
        """
        return util.quickExpMod(m,e,N)

    def Decryption(N, d, c):
        """
        :param N:
        :param d: all from private key
        :param c: ciphertext
        :return:
            c**d mod N
        """
        return util.quickExpMod(c, d, N)






























