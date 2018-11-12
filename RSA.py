import util

"""
:: 11/12/18   11:50 AM
:: RSA Encryption
"""

class RSACipher:
    def __init__(self):
        pass

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






























