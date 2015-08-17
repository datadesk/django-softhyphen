.PHONY: test

test:
	clear
	pep8 softhyphen
	pyflakes softhyphen
	python setup.py test
