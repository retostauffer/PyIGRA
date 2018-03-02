

# Create readme file
.PHONY: readme
readme:
	pandoc README.md -o README.pdf
