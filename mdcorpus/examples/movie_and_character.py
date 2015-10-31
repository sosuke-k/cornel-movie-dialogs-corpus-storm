#! /usr/bin/env python
# -*- coding: utf-8 -*-

from storm.locals import *
from mdcorpus.orm import *


database = create_database("sqlite:")
store = Store(database)

store.execute(MovieTitlesMetadata.CREATE_SQL)
store.execute(MovieCharactersMetadata.CREATE_SQL)

movie0 = store.add(MovieTitlesMetadata(0,
                                       u"10 things i hate about you",
                                       1999,
                                       6.90,
                                       62847))

chara0 = store.add(MovieCharactersMetadata(0,
                                           "BIANCA",
                                           "f",
                                           4))
chara1 = store.add(MovieCharactersMetadata(1,
                                           "BRUCE",
                                           "?",
                                           "?"))
chara2 = store.add(MovieCharactersMetadata(2,
                                           "CAMERON",
                                           "m",
                                           "3"))

store.flush()

chara0.movie = movie0
movie0.characters.add(chara1)
chara2.movie_id = movie0.id

print "the characters of '" + movie0.title + "' :"
for character in movie0.characters:
    print "  * " + character.name + "(" + character.gender() + ")"
