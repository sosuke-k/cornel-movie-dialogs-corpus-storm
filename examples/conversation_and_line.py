#! /usr/bin/env python
# -*- coding: utf-8 -*-

from storm.locals import *
from mdcorpus.orm import *

database = create_database("sqlite:")
store = Store(database)

store.execute(MovieConversation.CREATE_SQL)
store.execute(MovieLine.CREATE_SQL)

conversation = store.add(MovieConversation(0, 2, 0))
line194 = store.add(MovieLine(
    194, "Can we make this quick?  Roxanne Korrine and Andrew Barrett are having an incredibly horrendous public break- up on the quad.  Again."))
line195 = store.add(MovieLine(
    195, "Well, I thought we'd start with pronunciation, if that's okay with you."))
line196 = store.add(MovieLine(
    196, "Not the hacking and gagging and spitting part.  Please."))
line197 = store.add(MovieLine(
    197, "Okay... then how 'bout we try out some French cuisine.  Saturday?  Night?"))
store.flush()

line_id_list = [194, 195, 196, 197]

for (i, line_id) in enumerate(line_id_list):
    line = store.find(MovieLine, MovieLine.id == line_id).one()
    line.number = i + 1
    conversation.lines.add(line)

store.commit()

for line in conversation.line_list():
    print "'" + line.text + "'"
