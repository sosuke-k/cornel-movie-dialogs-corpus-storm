"""Testing for ORM"""

from unittest import TestCase
import nose
from nose.tools import eq_

from sets import Set
from mdcorpus.orm import *


class ORMTestCase(TestCase):

    def setUp(self):
        self.store = Store(create_database("sqlite:"))
        self.store.execute(MovieTitlesMetadata.CREATE_SQL)
        self.store.execute(MovieCharactersMetadata.CREATE_SQL)
        self.store.execute(RawScriptUrl.CREATE_SQL)
        self.store.execute(MovieConversation.CREATE_SQL)
        self.store.execute(MovieLine.CREATE_SQL)
        movie = self.store.add(MovieTitlesMetadata(0,
                                                   u"10 things i hate about you",
                                                   1999,
                                                   6.90,
                                                   62847))
        bianca = self.store.add(MovieCharactersMetadata(0,
                                                        "BIANCA",
                                                        "f",
                                                        4))
        bruce = self.store.add(MovieCharactersMetadata(1,
                                                       "BRUCE",
                                                       "?",
                                                       "?"))
        cameron = self.store.add(MovieCharactersMetadata(2,
                                                         "CAMERON",
                                                         "m",
                                                         "3"))
        url = self.store.add(RawScriptUrl("http://www.dailyscript.com/scripts/10Things.html"))
        conversation = self.store.add(MovieConversation(0, 2, 0))
        line194 = self.store.add(MovieLine(
            194, "Can we make this quick?  Roxanne Korrine and Andrew Barrett are having an incredibly horrendous public break- up on the quad.  Again."))
        line195 = self.store.add(MovieLine(
            195, "Well, I thought we'd start with pronunciation, if that's okay with you."))
        line196 = self.store.add(MovieLine(
            196, "Not the hacking and gagging and spitting part.  Please."))
        line197 = self.store.add(MovieLine(
            197, "Okay... then how 'bout we try out some French cuisine.  Saturday?  Night?"))
        self.store.flush()

        movie.characters.add(bianca)
        movie.characters.add(bruce)
        movie.characters.add(cameron)
        url.movie = movie
        line_id_list = [194, 195, 196, 197]
        for (i, line_id) in enumerate(line_id_list):
            line = self.store.find(MovieLine, MovieLine.id == line_id).one()
            line.number = i + 1
            conversation.lines.add(line)
        self.store.commit()

    def tearDown(self):
        print "done"


class MovieTitlesMetadataTestCase(ORMTestCase):

    @nose.with_setup(ORMTestCase.setUp, ORMTestCase.tearDown)
    def test_url(self):
        movie = self.store.find(MovieTitlesMetadata, MovieTitlesMetadata.id == 0).one()
        eq_(movie.url(), "http://www.dailyscript.com/scripts/10Things.html")


class MovieCharactersMetadataTestCase(ORMTestCase):

    @nose.with_setup(ORMTestCase.setUp, ORMTestCase.tearDown)
    def test_gender(self):
        bianca = self.store.find(MovieCharactersMetadata, MovieCharactersMetadata.id == 0).one()
        bruce = self.store.find(MovieCharactersMetadata, MovieCharactersMetadata.id == 1).one()
        cameron = self.store.find(MovieCharactersMetadata, MovieCharactersMetadata.id == 2).one()
        eq_(bianca.gender(), "f")
        eq_(bruce.gender(), "?")
        eq_(cameron.gender(), "m")


class MovieConversationTestCase(ORMTestCase):

    @nose.with_setup(ORMTestCase.setUp, ORMTestCase.tearDown)
    def test_consistency(self):
        conversation = self.store.find(MovieConversation, MovieConversation.id == 1).one()
        eq_(conversation.first_character.movie.title, conversation.movie.title)
        eq_(conversation.second_character.movie.title, conversation.movie.title)

    @nose.with_setup(ORMTestCase.setUp, ORMTestCase.tearDown)
    def test_line_list(self):
        conversation = self.store.find(MovieConversation, MovieConversation.id == 1).one()
        line_ids = [line.id for line in conversation.line_list()]
        eq_(line_ids, [194, 195, 196, 197])
