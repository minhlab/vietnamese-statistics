#!/usr/bin/python
import fileinput  

if __name__ == '__main__':
    for line in fileinput.input():
        print '|-'
        fields = line.split('\t')
        for field in fields[:10]:
            print "| " + field
