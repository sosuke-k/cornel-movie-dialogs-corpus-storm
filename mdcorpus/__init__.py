#! /usr/bin/env python
# -*- coding: utf-8 -*-

__version__ = "0.1.0"
__all__ = ["mdcorpus", "parser"]

from storm.locals import *
from mdcorpus import *

# initializing the relationships
MovieTitlesMetadata.genres = ReferenceSet(MovieTitlesMetadata.id,
                                          MovieGenreLine.movie_id,
                                          MovieGenreLine.genre_id,
                                          Genre.id)

Genre.movies = ReferenceSet(Genre.id,
                            MovieGenreLine.genre_id,
                            MovieGenreLine.movie_id,
                            MovieTitlesMetadata.id)
