from unittest import TestCase
import os
import hashlib

# test
class TestMain(TestCase):

    def generateRandomPlainFile(self, numBits, count):
        randomVal = os.urandom(int(numBits / 8))
        fileName = "testData/testPlain_" + str(count)
        with open(fileName, 'wb') as plainFile:
            plainFile.write(randomVal)
        return fileName

    def test_main(self):
        count = 0
        for round in range(3,10):
        #-------------------------------- BEGIN GENERATING KEY FILES
            security_param = 256*2
            n = ' '+str(security_param)

            print("....... ", str(int((security_param//8)/2)) )

            o_cipher_file = 'testData/cipher_output'
            o_plain_file = 'testData/plain_output'

            privateKey_file = 'testData/privKey'
            publicKey_file = 'testData/pubKey'
            keygen_command = 'python3 rsa-keygen.py -p '+publicKey_file+' -s '+privateKey_file+' -n '+n

            os.system(keygen_command)            

	    #-------------------------------- FINISH GENERATING KEYFILES
            
            #privateKeyFile = 'testData/privKey1.txt'
            #publicKeyFile = 'testData/pubKey1.txt'
            #encryptedFile = originalPlainFile + "_enc"
            #decryptedFile = originalPlainFile + "_dec"

            os.system("rm testData/testPlain*")
            print ("\n"*5)
            count = 1
            numBits = 256
            originalPlainFile = self.generateRandomPlainFile(numBits, count)

            print('\x1b[1;31;47m' + "\nEncryption.... " + str(round) + '\n' + '\x1b[0m')
            print(originalPlainFile, privateKey_file, publicKey_file, o_cipher_file, o_plain_file)
            encryption_command = "python3 rsa-enc.py " + " -k " + publicKey_file + "  -i  " + originalPlainFile + "  -o  " + o_cipher_file
            os.system(encryption_command)
            print('\x1b[1;31;47m' + "\nDecryptrion.... " + str(round) + '\n' + '\x1b[0m')
            decryption_command = "python3 rsa-dec.py " + " -k " + publicKey_file + "  -i  " + o_cipher_file + "  -o  " + o_plain_file
            os.system(decryption_command)
            # -----------------------
            with open(originalPlainFile, 'rb') as originalPlainFileContent:
                originalPlainFileData = originalPlainFileContent.read()            #-----------------------
            with open(o_plain_file, 'rb') as decryptedFileContent:
                decryptedFileData = decryptedFileContent.read()
            # -----------------------
            try:
                self.assertEqual(hashlib.sha3_256(originalPlainFileData).hexdigest(), hashlib.sha3_256(o_plain_file).hexdigest())
                print('\x1b[6;30;42m' + "\nround " +  str(round) + ' Success!\n' + '\x1b[0m')
            except:
                print('\x1b[3;30;41m' + "\nround " + str(round) + ' Failed!\n' + '\x1b[0m')


    def test_intToByte(self):
        t = 361228602529821044081166545515048259738259280980846596864414691243720388090
        print(t.bit_length())
        tBytes = t.to_bytes((256// 8), byteorder='big')
        print(tBytes)
        orig_bytes = b'\x00\xccr\xb9\x8b\x07.\x9f@\xee\x002\x0f\x0fS>\xe1\xb5\x83\x03\xef\xd2{\xe0\xaf\xe4\x9b\xe2\x9dk-\xfa'
        print(orig_bytes)

