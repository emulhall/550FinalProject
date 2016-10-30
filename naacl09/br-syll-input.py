#! /usr/bin/env python

usage = """%prog Version of 5th October 2008

(c) Mark Johnson

Maps br-syll.txt to the input required by py-cfg.

usage: %prog [options]"""

import optparse, re, sys
import lx

def file_brentformat(inf, outf, mapper):
    for line in inf:
        segs = (mapper.get(c, c) for c in line.strip()+' ')
        outf.write(' '.join(seg for seg in segs if seg))
        outf.write('\n')


if __name__ == "__main__":
    parser = optparse.OptionParser(usage=usage)
    parser.add_option("-s", "--syllable-boundaries", dest="syllable_boundaries",
                      help="map syllable boundaries to this value")
    parser.add_option("-w", "--word-boundaries", dest="word_boundaries",
                      help="map word boundaries to this value")
    (options,args) = parser.parse_args()
    mapper = {}
    mapper[' '] = options.word_boundaries
    mapper['\t'] = options.word_boundaries
    mapper['.'] = options.syllable_boundaries
    with open("/Users/Elias/550FinalProject/output/sylliformat.txt", 'w') as a1:
        inpt = open('/Users/Elias/550FinalProject/naacl09/br-phono.txt', 'r')
        file_brentformat(inpt, a1, mapper)

