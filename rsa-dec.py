
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
    # -------------------------Read private key--------------------------------------
    # d_hex = "3f84968d43a70548eb23de7c9a6b4352590db37d6cef3c5cacbfeb8e0130aa8b1d2ab2e40e1e9f69615742e03cad775b3c3a43cf9099d533dd17d4e889d8045c18eaff6eef79095f41f3365be41a74d1e5f15799a94eba0cca82d04fc58343c6c9776f7f590a4961ecd16ef0c27dd4c7a725d940ff167d34ee74fc0df6bee11"
    # print(util.hexToInt(d_hex))
    # with open(i, 'r')













































if __name__ == '__main__':
    main()
