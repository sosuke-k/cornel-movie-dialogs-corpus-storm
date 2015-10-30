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

-  I adjust title data for **Acute accent** manually.

   -  line 115, ``léon``

-  I ignored **duplication** for genre data.

   -  line 58, ``['horror', 'mystery', 'mystery', 'sci-fi', 'sci-fi']``
