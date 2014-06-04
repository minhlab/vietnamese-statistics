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
        prefixes = OrderedDict()
        for line in f:
            m = re.search('^\s*(\d+) (.+)$', line)
            if not m:
                print >>sys.stderr, "Line not match: %s" %line
                continue
            count, prefix = m.group(1), m.group(2)
            prefixes[prefix] = (count, set())

    for line in fileinput.input(args.remainders):
	words = line.strip().split(' ')
        for word in words:
            syllables = word.split('_')
            if len(syllables) >= 2:
                prefix = "_".join(syllables[:-1])
                if prefix not in prefixes:
                    print >>sys.stderr, "Prefix not found: %s" %prefix
                    continue
                prefixes[prefix][1].add(word)

    for prefix in prefixes:
        print "%s\t%s\t%s" %(prefixes[prefix][0], prefix,
                             "\t".join(prefixes[prefix][1]))
