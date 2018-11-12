from unittest import TestCase
import util
import RSA

class TestRSA_encryption(TestCase):
    def test_Encryption(self):
        N_hex = "d94d889e88853dd89769a18015a0a2e6bf82bf356fe14f251fb4f5e2df0d9f9a94a68a30c428b39e3362fb3779a497eceaea37100f264d7fb9fb1a97fbf621133de55fdcb9b1ad0d7a31b379216d79252f5c527b9bc63d83d4ecf4d1d45cbf843e8474babc655e9bb6799cba77a47eafa838296474afc24beb9c825b73ebf549"
        N = util.hexToInt(N_hex)
        e_hex = "10001"
        e = util.hexToInt(e_hex)
        m_Hex = "12345"
        m = util.hexToInt(m_Hex)
        c1 = RSA.RSACipher.Encryption(N, e, m)
        expected = util.hexToInt("0xceaee479a52d9d60ea743119d4e79356f411c0bdddefb3f4312f03a289462e7c9f46d5405b6e10e01be5faea6c2e35add343ef536cf47566c91008d85767b72eb00e659ba610f18737ae7b679a9157d10c81b5798be8fd8eed869d1c514c3076cde82912a63e95ee89090dadeeeef4a7f31fe0c6abf9ab3d3c0331ece3cfdbb1")
        self.assertEqual(expected, c1)


    def test_Decryption(self):
        N_hex = "e02bdfa5480894e575f693c941765ad2b2c555d70868e3cbce8835f58b2cc962b24312075fe7202b89e9400a8afafbbc5de8388849f7eb6e1f7f099f5dff0e20083630118952efc46113334873177595eecc03bc78bc18130d5a35f4036657fed996173fd34bcd42edecb23c93891983b0aafd1e6d3aadf920786eb89f4d9b99"
        e_hex = "10001"                         # we will not utilize e in decryption process
        d_hex = "ce7d9b74d3f593b20a0727faaaa22ae70a655bbcc7b256a2d58c02a83b9af5a6442e23dd4729cf284bd0df7cd6a87a59f8e67fac8af623973ccbf84124845caccb69fc189318e35f508bf3023f844dcf4704093251b4caf825f49531aed39ee5a2b90526aad0ec7e7f8be49d134ba2282c1e2e900e78e627dff3d9e0e180be41"
        expected_hex = "24244267854a"          # plain text in hex
        cipher_hex = "6983fc799be19b74d32458ab6c0b7d0d756424b66934d77262d4441b9adf2f6e2ebc7989b5fcc30af2bd51c46bdf7a7a4734da6ad82ac3426d6cafcfc46af18a6c0bc164397e484583fefc10e5bff2c792e73730bef8acf2c05b98d3cd7c54a97a4b7d63d83f97cc7ece536f37bdc0de16125d0b77586a8a8eb4670ac8037799"
        N = util.hexToInt(N_hex)
        e = util.hexToInt(e_hex)
        d = util.hexToInt(d_hex)
        c = util.hexToInt(cipher_hex)
        plain = RSA.RSACipher.Decryption(N, d, c)
        self.assertEqual(util.hexToInt(expected_hex), plain)
