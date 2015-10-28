#! /usr/bin/env python
# -*- coding: utf-8 -*-

from sets import Set
from storm.locals import *


class MovieTitlesMetadata(object):
    __storm_table__ = "movie_titles_metadata"
    CREATE_SQL = "CREATE TABLE " + __storm_table__ + \
        " (id INTEGER PRIMARY KEY, title VARCHAR, year INTEGER, rating FLOAT, votes INTEGER)"
    id = Int(primary=True)
    title = Unicode()
    year = Int()
    rating = Float()
    votes = Int()

    def __init__(self, id, title, year, rating, votes):
        self.id = id
        self.title = title.decode("utf-8")
        self.year = year
        self.rating = rating
        self.votes = votes


class Genre(object):
    __storm_table__ = "genres"
    CREATE_SQL = "CREATE TABLE " + __storm_table__ + " (id INTEGER PRIMARY KEY, name VARCHAR)"
    id = Int(primary=True)
    name = Unicode()

    def __init__(self, name):
        self.name = name.decode("utf-8")


class MovieGenreLine(object):
    __storm_table__ = "movie_genre_lines"
    __storm_primary__ = "movie_id", "genre_id"
    CREATE_SQL = "CREATE TABLE " + __storm_table__ + \
        " (movie_id INTEGER, genre_id INTEGER, PRIMARY KEY (movie_id, genre_id))"
    movie_id = Int()
    genre_id = Int()


class MovieCharactersMetadata(object):
    __storm_table__ = "movie_characters_metadata"
    CREATE_SQL = "CREATE TABLE " + __storm_table__ + \
        " (id INTEGER PRIMARY KEY, name VARCHAR, movie_id INTEGER, gender_idx INTEGER, position INTEGER)"
    GENDER = ["m", "f", "?"]
    id = Int(primary=True)
    name = Unicode()
    movie_id = Int()
    movie = Reference(movie_id, MovieTitlesMetadata.id)
    gender_idx = Int()
    position = Int()

    def __init__(self, id, name, gender, position):
        self.id = id
        self.name = name.decode("utf-8")
        self.gender_idx = self.GENDER.index(gender)
        self.position = position if isinstance(position, int) else 0

    def gender(self):
        return self.GENDER[self.gender_idx]
