from unittest import TestCase
from util import *

class TestUtil(TestCase):
    def test_extGCD(self):
        input = [
            [42823,6409, -22, 147],
            [1,23, 1, 0],
            [5,177, 71, -2],
            [8,1009, -126, 1],
            [11,432, -157,4],
            [111,432, -35, 9],
            [3456,42, -3, 247],
            [919191,41, -17, 381128],
            [1313131,3000, -1229, 537946]
        ]
        for i in input:
            expected_X = i[2]
            expected_Y = i[3]
            calculated_X , calculated_Y = extGCD(i[0], i[1])
            self.assertEqual(expected_X, calculated_X)
            self.assertEqual(expected_Y, calculated_Y)

    def test_isprime(self):
        input = [
            5,
            2,
            3,
            4,
            59,
            2017,
            2027,
            393050634124102232869567034555427371542904833,
            18446744082299486207,
            1152921506754330623,
            43143988327398957279342419750374600193,
            85053461164796801949539541639542805770666392330682673302530819774105141531698707146930307290253537320447270457,
            982300303982300313982300321982300331982300369982300433982300481982300489,
            982300303982300313982300321982300331982300369982300433982300481982300489982300303982300313982300321982300331982300369982300433982300481982300489982300303982300313982300321982300331982300369982300433982300481982300489982300303982300313982300321982300331982300369982300433982300481982300489,
            1323980736381925928520875923578996707604075732952629060954862004280025284376668355992035808371414287326692258319170317558820550693553915744682056218228163
        ]
        expected = [
            True,
            True,
            True,
            False,
            True,
            True,
            True,
            True,
            True,
            False,
            True,
            True,
            False,
            False,
            True
        ]
        for i in range(len(input)):
            self.assertEqual(expected[i], isPrime(input[i]))
        # isPrime(2**6)

    def test_GCD(self):
        input = [
            [4, 87, 1],
            [42, 88, 2],
            [344, 88888,8],
            [27,29629356, 3]
        ]
        for i in input:
            self.assertEqual(i[2], GCD(i[0], i[1]))


    def test_inverse_mod(self):
        phi_n = 1122864880
        e = 3
        res =inverse_mod(phi_n, e)
        self.assertEqual(748576587, res)

    def test_generatePrime(self):
        print("Prime :\t",generatePrime(1))
        print("Prime :\t",generatePrime(2))
        print("Prime :\t",generatePrime(3))
        print("Prime :\t",generatePrime(4))
        print("Prime :\t",generatePrime(5))
        print("Prime :\t",generatePrime(6))
        print("Prime :\t",generatePrime(7))
        print("Prime :\t",generatePrime(8))
        print("Prime :\t",generatePrime(9))
        print("Prime :\t",generatePrime(10))
        print("Prime :\t",generatePrime(11))
        print("Prime :\t",generatePrime(111))
        print("Prime :\t",generatePrime(1111))
        print("Prime :\t",generatePrime(22))
        print("Prime :\t",generatePrime(222))
        print("Prime :\t",generatePrime(3))
        print("Prime :\t",generatePrime(33))
        print("Prime :\t",generatePrime(4))
        print("Prime :\t",generatePrime(44))
        print("Prime :\t",generatePrime(444))



    def test_padding(self):
        print(bytes(1))
        print(bytes(2))
        print(b'\x00')
        print(b'\x01')
        print(b'\x01' + b'\x02')
        myBits = int("101110", base=2)
        print("myBits", myBits)
        print("myBits len", myBits.bit_length())
        print("myBits len (byte)", (myBits.bit_length()//8)+1)
        print("myBits to byte", myBits.to_bytes((myBits.bit_length()//8)+1, 'big'))
        print("-"*10)
        unpaddedText = os.urandom(256//8)
        padding(580, unpaddedText)





















