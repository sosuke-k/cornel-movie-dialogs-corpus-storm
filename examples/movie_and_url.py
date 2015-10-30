#! /usr/bin/env python
# -*- coding: utf-8 -*-

from storm.locals import *
from mdcorpus.orm import *


database = create_database("sqlite:")
store = Store(database)

store.execute(MovieTitlesMetadata.CREATE_SQL)
store.execute(RawScriptUrl.CREATE_SQL)

movie = store.add(MovieTitlesMetadata(0,
                                      u"10 things i hate about you",
                                      1999,
                                      6.90,
                                      62847))
url = store.add(RawScriptUrl("http://www.dailyscript.com/scripts/10Things.html"))
store.flush()

url.movie = movie
store.commit()

print "'" + movie.title + "' script is from " + movie.url()
