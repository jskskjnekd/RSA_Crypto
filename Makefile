# Clean build files
clean:
<<<<<<< HEAD
	find . -name 'rsa*' -print0 | xargs -0 chmod +x
	find . -name 'rsa*' | while read f; do mv "$f" "${f%.py}"; done
	pip install -r requirements.txt
	pip3 install -r requirements.txt
=======
	find . -name '*.py' -print0 | xargs -0 chmod +x
	find . -name '*.py' | while read f; do cp "$f" "${f%.py}"; done
	pip install -r requirements.txt
	pip3 install -r requirements.txt
>>>>>>> 5efab1bef540c43ad79cd5637d0ee5bc69ab4104
