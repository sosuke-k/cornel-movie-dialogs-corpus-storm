#! /usr/bin/env python
# -*- coding: utf-8 -*-

from storm.locals import *
from mdcorpus.orm import *
from mdcorpus.parser import *

parser = Parser()

f = open("sample_movie_characters_metadata.txt")
line = f.readline()
while line:
    print "=== parse this line ==="
    print line
    list = parser.movie_characters_metadata(line)
    character = MovieCharactersMetadata(list[0], list[1], list[-2], list[-1])
    print character.name.encode("utf-8") + " (" + character.gender() + ") appears in '" + list[-3] + "'"
    print ""

    line = f.readline()
f.close
