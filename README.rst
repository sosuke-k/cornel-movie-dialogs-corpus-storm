cornel-movie-dialogs-corpus-storm
=================================

A set of python modules for cornel movie-dialogs corpus with storm.

Abstract
--------

This module include some classes extending
`storm <https://storm.canonical.com/>`__ ORM for `cornel movie-dialogs
corpus <http://www.mpi-sws.org/~cristian/Cornell_Movie-Dialogs_Corpus.html>`__
data.

Install
-------

::

    pip install storm                # if you not
    pip install cornel-movie-dialogs-corpus-storm

Setup
-----

1. download corpus and unzip
2. generate database and insert with ``generate-mdcorpus-database.py``

for example:

::

    generate-mdcorpus-database.py --corpus-dir "cornell movie-dialogs corpus" corpus.db

Usage
-----

::

    from mdcorpus.orm import *
    from mdcorpus.parser import *

    ...

Class List
----------

-  MovieTitlesMetadata
-  Genre
-  MovieGenreLine
-  MovieCharactersMetadata
-  MovieConversation
-  MovieLine
-  RawScriptUrl

Corpus Problem
--------------

This is memo when I dealt with corpus problems.

movie\_titles\_metadata.txt
~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  I ignored an **alphabet** following year.

   -  for example, line 34, ``1989/I``

-  I ignored **duplication** for genre data.

   -  line 58, ``['horror', 'mystery', 'mystery', 'sci-fi', 'sci-fi']``

Code Problem
------------

I use ``Python2.7`` and I don't know how to use ``codecs``
module.(\ `Unicode HOWTO — Python 2.7ja1
documentation <http://docs.python.jp/2/howto/unicode.html>`__)

mime
~~~~

convert text-code to ``utf-8`` with `Mi <http://www.mimikaki.net/>`__

before
^^^^^^

::

    cornell movie-dialogs corpus$ file --mime {(ls)}
    README.txt:                    text/plain; charset=iso-8859-1
    chameleons.pdf:                application/pdf; charset=binary
    movie_characters_metadata.txt: text/plain; charset=iso-8859-1
    movie_conversations.txt:       text/plain; charset=us-ascii
    movie_lines.txt:               text/plain; charset=us-ascii
    movie_titles_metadata.txt:     text/plain; charset=iso-8859-1
    raw_script_urls.txt:           text/plain; charset=iso-8859-1

after
^^^^^

::

    cornell movie-dialogs corpus$ file --mime {(ls)}
    README.txt:                    text/plain; charset=utf-8
    chameleons.pdf:                application/pdf; charset=binary
    movie_characters_metadata.txt: text/plain; charset=utf-8
    movie_conversations.txt:       text/plain; charset=us-ascii
    movie_lines.txt:               text/plain; charset=us-ascii
    movie_titles_metadata.txt:     text/plain; charset=utf-8
    raw_script_urls.txt:           text/plain; charset=utf-8

movie\_titles\_metadata.txt
~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  line 115, ``léon``

movie\_characters\_metadata.txt
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  line 1727 - 1736, ``léon``

result
~~~~~~

::

    sqlite> select * from movie_titles_metadata where title = 'léon';
    sqlite> select * from movie_titles_metadata where title = 'l駮n';
    114|l駮n|1994|8.6|204901
