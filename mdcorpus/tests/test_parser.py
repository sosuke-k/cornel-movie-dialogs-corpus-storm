"""Testing for Parser"""

from unittest import TestCase
from nose.tools import eq_

from sets import Set
from mdcorpus.parser import *


class ParserTestCase(TestCase):

    def setUp(self):
        self.parser = Parser()

    def tearDown(self):
        print "done"

    def test_movie_titles_metadata(self):
        line = "m0 +++$+++ 10 things i hate about you +++$+++ 1999 +++$+++ 6.90 +++$+++ 62847 +++$+++ ['comedy', 'romance']\n"
        l = self.parser.movie_titles_metadata(line)
        eq_(l[0], 0)
        eq_(l[1], "10 things i hate about you")
        eq_(l[2], 1999)
        eq_(l[3], 6.90)
        eq_(l[4], 62847)
        eq_(l[5], Set(["comedy", "romance"]))

    def test_movie_characters_metadata(self):
        line = "u0 +++$+++ BIANCA +++$+++ m0 +++$+++ 10 things i hate about you +++$+++ f +++$+++ 4\n"
        l = self.parser.movie_characters_metadata(line)
        eq_(l[0], 0)
        eq_(l[1], "BIANCA")
        eq_(l[2], 0)
        eq_(l[3], "10 things i hate about you")
        eq_(l[4], "f")
        eq_(l[5], 4)

    def test_movie_conversations(self):
        line = "u0 +++$+++ u2 +++$+++ m0 +++$+++ ['L194', 'L195', 'L196', 'L197']\n"
        l = self.parser.movie_conversations(line)
        eq_(l[0], 0)
        eq_(l[1], 2)
        eq_(l[2], 0)
        eq_(l[3], [194, 195, 196, 197])

    def test_movie_lines(self):
        line = "L203 +++$+++ u2 +++$+++ m0 +++$+++ CAMERON +++$+++ Seems like she could get a date easy enough...\n"
        l = self.parser.movie_lines(line)
        eq_(l[0], 203)
        eq_(l[1], 2)
        eq_(l[2], 0)
        eq_(l[3], "CAMERON")
        eq_(l[4], "Seems like she could get a date easy enough...")

    def test_raw_script_urls(self):
        line = "m0 +++$+++ 10 things i hate about you +++$+++ http://www.dailyscript.com/scripts/10Things.html\n"
        l = self.parser.raw_script_urls(line)
        eq_(l[0], 0)
        eq_(l[1], "10 things i hate about you")
        eq_(l[2], "http://www.dailyscript.com/scripts/10Things.html")
