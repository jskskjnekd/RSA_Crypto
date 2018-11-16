# Clean build files
clean:
	find . -name '*.py' -print0 | xargs -0 chmod +x
	find . -name '*.py' | while read f; do cp "$f" "${f%.py}"; done
	pip install -r requirements.txt
	pip3 install -r requirements.txt