# Clean build files
clean:
	find . -name 'rsa*' -print0 | xargs -0 chmod +x
	find . -name 'rsa*' | while read f; do mv "$f" "${f%.py}"; done
	pip install -r requirements.txt
	pip3 install -r requirements.txt
