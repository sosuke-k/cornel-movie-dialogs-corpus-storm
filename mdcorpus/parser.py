#! /usr/bin/env python
# -*- coding: utf-8 -*-

from sets import Set


class Parser:

    def __init__(self, separator=" +++$+++ "):
        self.separator = separator

    def movie_titles_metadata(self, line):
        metadata = line.split(self.separator)
        id = int(metadata[0][1:])                   # e.g. m0
        title = metadata[1]                         # e.g. 10 things i hate about you
        year = int(metadata[2][0:4])                # e.g. 1999
        rating = float(metadata[3])                 # e.g. 6.90
        votes = int(metadata[4])                    # e.g. 62847
        genre_list = metadata[5][1:-2].split(", ")  # e.g. ['comedy', 'romance']\n
        genres = Set([])
        for genre_name in genre_list:
            if genre_name != "":
                genres.add(genre_name[1:-1])
        return [id, title, year, rating, votes, genres]
