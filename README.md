# RSA_Crypto



## Instructions

```bash
make
```

### RSA Encryption


```bash
python3 rsa-enc -k testData/priv_Key111 -i testData/testPlain_2 -o testData/testPlain_enc_2


sha256sum testPlain_2
db0e180ef1131476ce6c657f976d217eacd7c3d799f02d269346c1736ca9d894  testPlain_2
```

### RSA Decryption

```bash
python3 rsa-dec -k testData/pub_Key111 -i testData/testPlain_enc_2 -o testPlain_dec_2


sha256sum testPlain_dec_2
db0e180ef1131476ce6c657f976d217eacd7c3d799f02d269346c1736ca9d894  testPlain_dec_2
```





