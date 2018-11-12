import util

"""
:: 11/12/18   11:50 AM
:: RSA Encryption
"""

class RSA_encryption:
    def __init__(self, numberBits, message):
        """
        :param numberBits:  number of bits for p and q.
                            Basically, number of bits for p (q) should be no less than 512
        :param message: plaintext (as integer)
        """
        self.p = util.generatePrime(numberBits)
        self.q = util.generatePrime(numberBits)
        self.n = self.p * self.q
        self.phi = (self.p - 1)*(self.q - 1)





























