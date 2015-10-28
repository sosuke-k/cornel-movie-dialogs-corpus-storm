#! /usr/bin/env python
# -*- coding: utf-8 -*-

__version__ = "0.0.3"
__all__ = ["orm", "parser"]

from storm.locals import *
from orm import *

# initializing the relationships
MovieTitlesMetadata.genres = ReferenceSet(MovieTitlesMetadata.id,
                                          MovieGenreLine.movie_id,
                                          MovieGenreLine.genre_id,
                                          Genre.id)

Genre.movies = ReferenceSet(Genre.id,
                            MovieGenreLine.genre_id,
                            MovieGenreLine.movie_id,
                            MovieTitlesMetadata.id)
