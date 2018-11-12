#!/usr/bin/env python
import click
from . import *
from util import *
import random

def readParameters(n):
    p = generatePrime(n)
    q = generatePrime(n)
    n = p * q
    phi = (p - 1)*(q - 1)
    return (p,q,n,phi)

def gen_keypair(self):
    p = self.p
    q  = self.q
    e = 65537
    while not GCD(e,self.phi) == 1:
        e = random.randrange(1,self.phi)
    d = extGCD(e, self.phi)
    return ((e,self.n),(d, self.n))

@click.command()
@click.option('-p',
              help='specifies the file storing a valid RSA public key as string')
@click.option('-s',
              help='specifies the file starting a valid RSA private key as string')
@click.option('-n',
              help='specifies the expected number of bits in your p and q')
def main(p,s,n):
    num_bits = n
