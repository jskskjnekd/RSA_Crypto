from . import *
from util import *

class rsa-keygen:
	def __init__(self, num_bits):
		self.p = util.generatePrime(num_bits)
		self.q = util.generatePrime(num_bits)
		self.n = self.p * self.q
		self.phi = (self.p - 1)*(self.q - 1)
	
	def gen_keypair(self, p , q):
		if not isPrime(p) and isPrime(q) and (p == q):
			raise ValueError('issue with prime number generation')
		
