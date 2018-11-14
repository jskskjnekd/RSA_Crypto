import click
import util
import RSA


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

    # -------------------------Read public key--------------------------------------
    with open(k, 'r') as keyFile:
        keyStringNumBits = keyFile.readline()
        N = int(keyFile.readline())
        e = int(keyFile.readline())
    print("\nPublic Key:\n", N, "\n----\n", e, "\n\n")

    # ------------------------Read message file---------------------------------------
    with open(i, 'rb') as inputFile:
        messageByte = inputFile.read()
    message = util.byteToint(messageByte)
    print("Plain text is:\n", message, "\n")

    # ------------------------Encryption---------------------------------------
    cipherInt = RSA.RSACipher.Encryption(N, e, message)
    # cipherByte = str(cipherInt).encode('latin-1')
    cipherByte = cipherInt.to_bytes((cipherInt.bit_length() // 8) + 1, byteorder='big')
    print("cipherInt ->\n", cipherInt)
    print("cipherByte =>\n", cipherByte)
    with open(o, 'wb') as outputFile:
        outputFile.write(cipherByte)


if __name__ == '__main__':
    main()
