import click
import util
import RSA
import struct


@click.command()
@click.option('-k',
              help='\"Key file\"\n=>\trequired, specifies a file storing a valid AES key as a hex encoded string\n.')
@click.option('-i', help='\"Input file\"\n=>\trequired, specifies the path of the file that is being operated on\n.')
@click.option('-o',
              help='\"Output file\"\n=>\trequired, specifies the path of the file where the resulting output is stored\n.')
def main(k, i, o):
    print("Key File:\t", k)
    print("Input File:\t", i)
    print("Output File:\t", o)

    # -------------------------Read private key--------------------------------------
    with open(k, 'r') as keyFile:
        keyStringNumBits = keyFile.readline()
        N = int(keyFile.readline())
        d = int(keyFile.readline())
    print("Private Key:\n", N, "\n----\n", d)

    # ------------------------Read message file---------------------------------------
    with open(i, 'rb') as inputFile:
        cipherByte = inputFile.read()
    cipherInt = util.byteToint(cipherByte)
    print("\ncipher text is:\n", cipherInt)

    # ------------------------Read message file---------------------------------------
    plain = RSA.RSACipher.Decryption(N, d, cipherInt)
    print("Plain text bit length is ", plain.bit_length())
    print("\nPlain text is:\n", plain, "\n\n")
    print("\nPlain text bit length:\n", plain.bit_length(), "\n\n")

    plainByte = plain.to_bytes((256 // 8), byteorder='big')
    # if (plain.bit_length() % 8 == 0):
    #     plainByte = plain.to_bytes((plain.bit_length() // 8), byteorder='big')
    # else:
    #     plainByte = plain.to_bytes((plain.bit_length() // 8)+1, byteorder='big')
    print("Plain Bytes : \n",plainByte)
    with open(o, 'wb') as outputFile:
        outputFile.write(plainByte)


if __name__ == '__main__':
    main()
