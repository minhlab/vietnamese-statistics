#!/usr/bin/python
import fileinput 
import re
import argparse
from collections import OrderedDict
import sys

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--count-file", dest="count_file", 
                        help="path to count file")
    parser.add_argument("remainders", nargs=argparse.REMAINDER)
    args = parser.parse_args()

    # read count file
    with open(args.count_file) as f:
        suffixes = OrderedDict()
        for line in f:
            m = re.search('^\s*(\d+) (.+)$', line)
            if not m:
                print >>sys.stderr, "Line not match: %s" %line
                continue
            count, suffix = m.group(1), m.group(2)
            suffixes[suffix] = (count, set())

    for line in fileinput.input(args.remainders):
	words = line.strip().split(' ')
        for word in words:
            syllables = word.split('_')
            if len(syllables) >= 2:
                suffix = "_".join(syllables[1:])
                if suffix not in suffixes:
                    print >>sys.stderr, "Suffix not found: %s" %suffix
                    continue
                suffixes[suffix][1].add(word)

    for suffix in suffixes:
        print "%s\t%s\t%s" %(suffixes[suffix][0], suffix,
                             "\t".join(suffixes[suffix][1]))
