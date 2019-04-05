


# Install python package
.PHONY: install
install:
	sudo python setup.py install

git-install:
	sudo pip install git+https://github.com/retostauffer/PyIGRA.git

# Create readme file
.PHONY: readme
readme:
	pandoc README.md -o README.pdf

# Test
.PHONY: test
test:
	PyIGRA_search --id Innsbruck
	PyIGRA_search --id ASM00094120
	PyIGRA --keep --id ASM00094120 -o ASM00094120.txt --limit 3
	PyIGRA --keep --id ASM00094120 -o sounding_data.txt -p PRESSURE,TEMPERATURE --limit 3
	PyIGRA --keep --id ASM00094120 -o sounding_data.txt -p PRESSURE,TEMPERATURE

