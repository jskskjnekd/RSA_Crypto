# RSA_Crypto











## utility


### int to byte
```python
int(208).to_bytes(length=32, byteorder='big')
```

### byte to int

```python
p = byteToint(os.urandom(int(lenBit / 8)))
```



### Extended GCD

```python
extGCD(8, 11)
```


### isPrime

```python
isPrime(2098893665744058648615126425661022259386391)
```


### quickly calculate (base^power mod N)

```python
base = byteToint(os.urandom(int(256/8)))
print("base ", base)
power = byteToint(os.urandom(int(512/8)))
print("power ", power)
N = 2535301200456458802993406410833
quickExpMod(base, power, N)
```




### Generate prime number with N bits

```python
generatePrime(512)
##  find prime number:
##	 4451537901776597039592466884632478054890795620658824134188439357671435704058966198544688835627890767819990381323643606990189458341735880248209460203214661
##	Hex:	 
##   0x54fea9fcea0948f0e8b8fa2315e041024aa1e192ebdce97cd32df749bc06ffa70076f313dcfe12405fa58e75dba828159ba861dc8cf7678d46d17955bb6dd745
```





