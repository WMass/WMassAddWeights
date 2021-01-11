#!/usr/bin/env python

import sys

assert(len(sys.argv)==2)

print('Processing %s' % sys.argv[1])

lumis = []

with open(sys.argv[1]) as inputfile:
    for line in inputfile:
        lumis.append(eval(line))

def split_list(alist, wanted_parts=1):
    length = len(alist)
    return [ alist[i*length // wanted_parts: (i+1)*length // wanted_parts] for i in range(wanted_parts) ]

splitlumis = split_list(lumis, 3)

for i,sl in enumerate(splitlumis):
    with open(sys.argv[1].replace('.txt', '_batch%i_JSON.txt' % i), 'w') as outputfile:
        outputfile.write('{"1": [')
        first = True
        for filelumi in sl:
            if first:
                first = False
            else:
                outputfile.write(', ')
            outputfile.write(', '.join(['[%i, %i]' % (lumi, lumi) for lumi in filelumi]))        
        outputfile.write(']}')