#! /usr/bin/env python
# -*- coding: utf-8 -*-

from storm.locals import *
from mdcorpus.orm import *
from mdcorpus.parser import *

parser = Parser()

f = open("sample_movie_conversations.txt")
line = f.readline()
while line:
    print "=== parse this line ==="
    print line
    list = parser.movie_conversations(line)
    line_id_list = list.pop()
    conversation = MovieConversation(*list)
    print "This conversation is between people whose ids are " + str(conversation.first_character_id) + " and " + str(conversation.second_character_id)
    print "line ids is here in order:"
    for line_id in line_id_list:
        print "  * " + str(line_id)
    print ""

    line = f.readline()
f.close
