# Clean build files
clean:
	find . -name 'rsa*' -print0 | xargs -0 chmod +x
	cp rsa-enc.py rsa-enc
	cp rsa-dec.py rsa-dec
	cp rsa-keygen.py rsa-keygen
	pip install -r requirements.txt
	pip3 install -r requirements.txt
