#! /usr/bin/env python
# -*- coding: utf-8 -*-

from storm.locals import *
from mdcorpus.orm import *
from mdcorpus.parser import *

parser = Parser()

f = open("sample.txt")
line = f.readline()
while line:
    print "=== parse this line ==="
    print line
    list = parser.movie_titles_metadata(line)
    genres = list.pop()
    movie = MovieTitlesMetadata(*list)
    print "title: " + movie.title.encode("utf-8") + " (" + str(movie.year) + ")"
    print "rating: " + str(movie.rating) + ", votes: " + str(movie.votes)
    print "genre: " + ", ".join(genres)
    print ""

    line = f.readline()
f.close
