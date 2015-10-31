#! /usr/bin/env python
# -*- coding: utf-8 -*-

from storm.locals import *
from mdcorpus.orm import *


database = create_database("sqlite:")
store = Store(database)

store.execute(MovieTitlesMetadata.CREATE_SQL)
store.execute(Genre.CREATE_SQL)
store.execute(MovieGenreLine.CREATE_SQL)

store.add(Genre("comedy"))
store.add(Genre("romance"))
store.add(Genre("adventure"))
store.add(Genre("biography"))
store.add(Genre("drama"))
store.add(Genre("history"))
store.add(Genre("action"))
store.add(Genre("crime"))
store.add(Genre("thriller"))
store.flush()

movie0 = store.add(MovieTitlesMetadata(0,
                                       u"10 things i hate about you",
                                       1999,
                                       6.90,
                                       62847))
movie0.genres.add(store.find(Genre, Genre.name == u"comedy").one())
movie0.genres.add(store.find(Genre, Genre.name == u"romance").one())

movie1 = store.add(MovieTitlesMetadata(1,
                                       "1492: conquest of paradise",
                                       1992,
                                       6.20,
                                       10421))
movie1.genres.add(store.find(Genre, Genre.name == u"adventure").one())
movie1.genres.add(store.find(Genre, Genre.name == u"biography").one())
movie1.genres.add(store.find(Genre, Genre.name == u"drama").one())
movie1.genres.add(store.find(Genre, Genre.name == u"history").one())

movie2 = store.add(MovieTitlesMetadata(2,
                                       "15 minutes",
                                       2001,
                                       6.10,
                                       25854))
movie2.genres.add(store.find(Genre, Genre.name == u"action").one())
movie2.genres.add(store.find(Genre, Genre.name == u"crime").one())
movie2.genres.add(store.find(Genre, Genre.name == u"drama").one())
movie2.genres.add(store.find(Genre, Genre.name == u"thriller").one())

store.commit()

print "'" + movie0.title + "' belongs to the following genres:"
for genre in movie0.genres:
    print "  * " + genre.name.encode("utf-8")

drama = store.find(Genre, Genre.name == u"drama").one()
print "'" + drama.name + "' genre includes the following movies:"
for movie in drama.movies:
    print "  * " + movie.title.encode("utf-8")
