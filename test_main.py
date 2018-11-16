from unittest import TestCase
import os
import hashlib



class TestMain(TestCase):

    def generateRandomPlainFile(self, numBits, count):
        randomVal = os.urandom(int(numBits // 8))
        fileName = "testData/testPlain_" + str(count)
        with open(fileName, 'wb') as plainFile:
            plainFile.write(randomVal)
        return fileName

    def test_RSA_encryption_and_decryption(self, id=111, numBits = 256):
        # generate original message
        originalTextFile = self.generateRandomPlainFile(numBits, id)

        # generate key file
        security_param = numBits * 4
        privateKey_file = 'testData/priv_Key' + str(id)
        publicKey_file = 'testData/pub_Key' + str(id)
        keygen_command = 'python3 rsa-keygen.py ' + \
                         ' -p ' + publicKey_file + \
                         ' -s ' + privateKey_file + \
                         ' -n ' + str(security_param)
        os.system(keygen_command)

        # RSA encrlsyption
        cipherTextFile = "testData/testPlain_enc_" + str(id)
        encryption_command = "python3 rsa-enc.py " + \
                             " -k " + privateKey_file + \
                             " -i " + originalTextFile + \
                             " -o " + cipherTextFile
        os.system(encryption_command)

        # RSA decryption
        newPlainTextFile = "testData/testPlain_dec_" + str(id)
        decryption_command = "python3 rsa-dec.py " + \
                                " -k " + publicKey_file + \
                                " -i " + cipherTextFile + \
                                " -o " + newPlainTextFile
        os.system(decryption_command)

        # compare original file and decrypted file
        with open(originalTextFile, 'rb') as originalPlainFileContent:
            originalPlainFileData = originalPlainFileContent.read()
        with open(newPlainTextFile, 'rb') as decryptedFileContent:
            decryptedFileData = decryptedFileContent.read()
        self.assertEqual(originalPlainFileData, decryptedFileData)
        print('\x1b[6;30;42m' + "\nid " + str(id) + ' Success!\n' + '\x1b[0m')


    def test_benchmark_RSA(self):
        for i in range(10):
            self.test_RSA_encryption_and_decryption(i)

    def test_intToByte(self):
        t = 361228602529821044081166545515048259738259280980846596864414691243720388090
        print(t.bit_length())
        tBytes = t.to_bytes((256 // 8), byteorder='big')
        print(tBytes)
        orig_bytes = b'\x00\xccr\xb9\x8b\x07.\x9f@\xee\x002\x0f\x0fS>\xe1\xb5\x83\x03\xef\xd2{\xe0\xaf\xe4\x9b\xe2\x9dk-\xfa'
        print(orig_bytes)
