#!/usr/bin/python
from fileinput import FileInput

if __name__ == '__main__':
    for line in FileInput():
	words = line.strip().split(' ')
        for word in words:
            print word

