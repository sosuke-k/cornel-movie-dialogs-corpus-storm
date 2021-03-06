#! /usr/bin/env python
# -*- coding: utf-8 -*-

from sets import Set
import re


class Parser:

    def __init__(self, separator=" +++$+++ "):
        self.separator = separator

    def split(self, line):
        return line.rstrip("\n").split(self.separator)

    def movie_titles_metadata(self, line):
        metadata = self.split(line)
        id = int(metadata[0][1:])                   # e.g. m0
        title = metadata[1]                         # e.g. 10 things i hate about you
        year = int(metadata[2][0:4])                # e.g. 1999
        rating = float(metadata[3])                 # e.g. 6.90
        votes = int(metadata[4])                    # e.g. 62847
        genre_list = metadata[5][1:-1].split(", ")  # e.g. ['comedy', 'romance']
        genres = Set([])
        for genre_name in genre_list:
            if genre_name != "":
                genres.add(genre_name[1:-1])
        return [id, title, year, rating, votes, genres]

    def movie_characters_metadata(self, line):
        metadata = self.split(line)
        id = int(metadata[0][1:])                   # e.g. u0
        name = metadata[1]                          # e.g. BIANCA
        movie_id = int(metadata[2][1:])             # e.g. m0
        movie_title = metadata[3]                   # e.g. 10 things i hate about you
        gender = metadata[4]                        # e.g. f
        position = metadata[5]                      # e.g. 4
        position = int(position) if position != "?" else position
        return [id, name, movie_id, movie_title, gender, position]

    def movie_conversations(self, line):
        # u0 +++$+++ u2 +++$+++ m0 +++$+++ ['L194', 'L195', 'L196', 'L197']
        metadata = self.split(line)
        first_character_id = int(metadata[0][1:])     # e.g. u0
        second_character_id = int(metadata[1][1:])    # e.g. u2
        movie_id = int(metadata[2][1:])               # e.g. m0
        line_id_list = metadata[3][1:-1].split(", ")  # e.g. ['L194', 'L195', 'L196', 'L197']
        line_ids = []
        for line_id in line_id_list:
            line_ids.append(int(line_id[2:-1]))
        return [first_character_id, second_character_id, movie_id, line_ids]

    def movie_lines(self, line):
        # L203 +++$+++ u2 +++$+++ m0 +++$+++ CAMERON +++$+++ Seems like she could
        # get a date easy enough...
        metadata = self.split(line)
        id = int(metadata[0][1:])                   # e.g. L203
        character_id = int(metadata[1][1:])         # e.g. u2
        movie_id = int(metadata[2][1:])             # e.g. m0
        character_name = metadata[3]                # e.g. CAMERON
        # e.g. Seems like she could get a date easy enough...
        text = metadata[4]
        return [id, character_id, movie_id, character_name, text]

    def raw_script_urls(self, line):
        # m0 +++$+++ 10 things i hate about you +++$+++
        # http://www.dailyscript.com/scripts/10Things.html
        metadata = self.split(line)
        movie_id = int(metadata[0][1:])                   # e.g. m0
        movie_title = metadata[1]                         # e.g. 10 things i hate about you
        # e.g. http://www.dailyscript.com/scripts/10Things.html
        url = metadata[2]
        return [movie_id, movie_title, url]
