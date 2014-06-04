vietnamese-statistics
=====================

Tools to do some statistics on a Vietnamese corpus. The corpus must be segmented, can spread on multiple files.
* words.py: print all words in a corpus
* prefixes.py: print all prefixes in a corpus
* suffixes.py: print all suffixes in a corpus
* bind-prefixes.py: read prefixes from a file (format: <count> <prefix>) and print them together with all words in a corpus
* bind-suffixes.py: read suffixes from a file (format: <count> <suffix>) and print them together with all words in a corpus
* count-all: generate count and bind files for a corpus, also serves as an usage example

There are ready-made statistics of RIDF-2013 corpus in files *.cnt, *.bind.
