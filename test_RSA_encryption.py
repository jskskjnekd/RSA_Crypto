from unittest import TestCase
import util
import RSA

class TestRSA_encryption(TestCase):
    def test_Encryption(self):
        N_hex = "a674f0f2a01fa0a987d0ef355f36cbd7eda5a931d5eca30b18fc237a481fcea435fe514166db877ca1e645204b0e1e2a8e5f7fcf28a98306c70424f0f4025c7d8c6d89063ac7847bf52eb1f2852bdd5cc03c1cbf63875b5062f4d22b290526a5fecfe343d39c3b46626b63e91670802b4d7a066973474a757d3e5957ddc020afddbeef963643b237651f7bd58d9af4ea67da7de5620539fb904c5a0243388498013470de777c8f11924add97fa1fb11b51cab46ea38adf995ad5efd0958a98cbf022dfb0d4b128917e4b513f120629051307b4d9d1014a28c55c93aaff59f47a7c0472a8b7a1ad5dbf07252c4b2602278fe18a77ec8acb8798f9f8b720dafe03"
        N = util.hexToInt(N_hex)
        e_hex = "00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000f3e7af"
        e = util.hexToInt(e_hex)
        m_Hex = "d20fca706b61bc2ad3ac90c7e8e6bcfd5c871f39b8862c34a0854bc758497c00876c3e753b56afd82e69f4cc487cdbf7648bbf5957acaddc2e45c42cb87de2c845f07d5aaca7ce449347357bea88d998b9e98f2c1ca3fd548bdbff8e5f1b49cb92034ec6c73c61938aae1a7bd8f3fc07e20b545b0e5164c53fadc196560cfa31"
        m = util.hexToInt(m_Hex)
        c1 = RSA.RSACipher.Encryption(N, e, m)
        print(c1)


    def test_Decryption(self):
        pass
