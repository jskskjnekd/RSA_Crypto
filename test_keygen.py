import os
from unittest import TestCase
from util import *

class TestKeyGen(TestCase):
    def test_publicKey(self):
        
        for i in range(3,10):
            security_param = 2**i
            num_bytes = str(security_param//8)
            n = ' '+str(security_param)


            print("....... ", str(int((security_param//8)/2)) )
            aes_key = 'head -c '+ str(int((security_param//8)/2)) +' </dev/random  >testData/aes_key'
            os.system(aes_key)

            aes_file = ' testData/aes_key'
            o_cipher_file = ' testData/cipher_output'	   
            o_plain_file = ' testData/plain_output'

            privateKey_file = ' testData/privKey'
            publicKey_file = ' testData/pubKey'
            keygen_command = 'python3 rsa-keygen.py -p'+publicKey_file+' -s'+privateKey_file+' -n'+n
            
          
            enc_command = 'python3 rsa-enc.py -k'+publicKey_file+' -i'+aes_file+' -o'+o_cipher_file
            dec_command = 'python3 rsa-dec.py -k'+privateKey_file+' -i'+o_cipher_file+' -o'+o_plain_file

            os.system(keygen_command)
            os.system(enc_command)
            os.system(dec_command)

            
            
