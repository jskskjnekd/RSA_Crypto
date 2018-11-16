#!/usr/bin/env python
import click
from . import *
from util import *
import random



def compute_phi_p_q(n):
    e = 3
    num_bits = int(n)
    p_prime = generatePrime(num_bits)
    q_prime = generatePrime(num_bits)
    phi = (p_prime - 1)*(q_prime - 1)
    return phi, p_prime, q_prime

def keygen(n):
    e = 3
    phi, p_prime, q_prime = compute_phi_p_q(n)
    N = p_prime * q_prime

    while not GCD(e, phi) == 1:
        e = random.randrange(1,phi)
    d = inverse_mod(phi, e)

    return (e, N), d


@click.command()
@click.option('-p',
              help='specifies the file storing a valid RSA public key as string')
@click.option('-s',
              help='specifies the file starting a valid RSA private key as string')
@click.option('-n',
              help='specifies the expected number of bits in your p and q')
def main(p, s, n):
    # ------------ Return RSA keypair -------------_#
    num_bits = int(n)
    pub_tuple, priv = keygen(num_bits)

    # ------------ Store string representation ----_#
    numbits_string = str(pub_tuple[1].bit_length())
    N_string = str(pub_tuple[1])
    e_string = str(pub_tuple[0])
    d_string = str(priv)

    # ------------ Output Results -------------_#
    with open(p, 'w') as publicFile:
        publicFile.writelines(numbits_string + '\n')
        publicFile.writelines(N_string + '\n')
        publicFile.writelines(e_string)

    with open(s, 'w') as privateFile:
        privateFile.writelines(numbits_string + '\n')
        privateFile.writelines(N_string + '\n')
        privateFile.writelines(d_string)


if __name__ == '__main__':
    main()
