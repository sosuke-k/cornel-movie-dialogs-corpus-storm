#! /usr/bin/env python
# -*- coding: utf-8 -*-

from storm.locals import *
from mdcorpus.orm import *
from mdcorpus.parser import *

parser = Parser()

f = open("sample_movie_lines.txt")
line = f.readline()
while line:
    print "=== parse this line ==="
    print line
    list = parser.movie_lines(line)
    line = MovieLine(list[0], list[-1])
    print "the utterance of line(" + str(line.id) + "):"
    print "'" + line.text + "'"
    print ""

    line = f.readline()
f.close
