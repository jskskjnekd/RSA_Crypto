from unittest import TestCase
import util
import RSA

class TestRSA_encryption(TestCase):
    def test_Encryption(self):
        N_hex = "d94d889e88853dd89769a18015a0a2e6bf82bf356fe14f251fb4f5e2df0d9f9a94a68a30c428b39e3362fb3779a497eceaea37100f264d7fb9fb1a97fbf621133de55fdcb9b1ad0d7a31b379216d79252f5c527b9bc63d83d4ecf4d1d45cbf843e8474babc655e9bb6799cba77a47eafa838296474afc24beb9c825b73ebf549"
        N = util.hexToInt(N_hex)
        e_hex = "10001"
        # e = util.hexToInt(e_hex)
        print(int(e_hex, 16))
        # m_Hex = "12345"
        # m = util.hexToInt(m_Hex)
        # c1 = RSA.RSACipher.Encryption(N, e, m)
        # print(c1)


    def test_Decryption(self):
        pass
