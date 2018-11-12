import click
import util


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
    N_hex = "d27f0b0056d6b1162ad50b30c9d621efcc387fbad3d71c528d362a6ec455122c025a831735e2c39fe7fb7f79c7d73fe7d039fe7864c8271da5d8e159dfb24e8f0a0e8359ebcc88cb9c84245795a9f89b58b34829943c4842bd44d048f8713d8aa89488b3e9d20d17cee887362153d5c87365c550b805d720cb14008f9d00e339"
    e_hex = "10001"
    print(util.hexToInt(N_hex))
    print(util.hexToInt(N_hex).bit_length())
    print(util.hexToInt(e_hex))


if __name__ == '__main__':
    main()
