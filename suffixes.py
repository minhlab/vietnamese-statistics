#!/usr/bin/python
import fileinput

if __name__ == '__main__':
    for line in fileinput.input():
	words = line.strip().split(' ')
        for word in words:
            syllables = word.split('_')
            if len(syllables) >= 2:
                suffix = "_".join(syllables[1:])
                print suffix

