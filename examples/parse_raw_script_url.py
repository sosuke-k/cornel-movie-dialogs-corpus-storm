#! /usr/bin/env python
# -*- coding: utf-8 -*-

from storm.locals import *
from mdcorpus.orm import *
from mdcorpus.parser import *

parser = Parser()

f = open("sample_raw_script_urls.txt")
line = f.readline()
while line:
    print "=== parse this line ==="
    print line
    list = parser.raw_script_urls(line)
    script_url = RawScriptUrl(list[-1])
    print script_url.url
    print ""

    line = f.readline()
f.close
