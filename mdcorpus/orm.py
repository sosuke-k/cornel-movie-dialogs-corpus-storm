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

    def url(self):
        u = ""
        for v in self.raw_script_url:
            u = v.url
            break
        return u


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


class MovieConversation(object):
    __storm_table__ = "movie_conversations"
    CREATE_SQL = "CREATE TABLE " + __storm_table__ + \
        " (id INTEGER PRIMARY KEY, first_character_id INTEGER, second_character_id INTEGER, movie_id INTEGER)"
    id = Int(primary=True)
    first_character_id = Int()
    first_character = Reference(first_character_id, MovieCharactersMetadata.id)
    second_character_id = Int()
    second_character = Reference(second_character_id, MovieCharactersMetadata.id)
    movie_id = Int()
    movie = Reference(movie_id, MovieTitlesMetadata.id)

    def __init__(self, first_character_id, second_character_id, movie_id):
        self.first_character_id = first_character_id
        self.second_character_id = second_character_id
        self.movie_id = movie_id

    def line_list(self):
        return sorted(self.lines, key=lambda x: x.number)


class MovieLine(object):
    __storm_table__ = "movie_lines"
    CREATE_SQL = "CREATE TABLE " + __storm_table__ + \
        " (id INTEGER PRIMARY KEY, conversation_id INTEGER, number INTEGER, text VARCHAR)"
    id = Int(primary=True)
    conversation_id = Int()
    conversion = Reference(conversation_id, MovieConversation.id)
    number = Int()
    text = Unicode()

    def __init__(self, id, text):
        self.id = id
        self.text = text.decode("utf-8")


class RawScriptUrl(object):
    __storm_table__ = "raw_script_urls"
    CREATE_SQL = "CREATE TABLE " + __storm_table__ + \
        " (id INTEGER PRIMARY KEY, movie_id INTEGER, url VARCHAR)"
    id = Int(primary=True)
    movie_id = Int()
    movie = Reference(movie_id, MovieTitlesMetadata.id)
    url = Unicode()

    def __init__(self, url):
        self.url = url.decode("utf-8")
