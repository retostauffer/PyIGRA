


# Install python package
.PHONY: install
install:
	sudo python setup.py install

# Create readme file
.PHONY: readme
readme:
	pandoc README.md -o README.pdf

# Test
.PHONY: test
test:
	PyIGRA --keep --id ASM00094120 -o ASM00094120.txt --limit 3
	PyIGRA --keep --id ASM00094120 -o GMM00010393.txt -p PRESSURE,TEMPERATURE --limit 3

