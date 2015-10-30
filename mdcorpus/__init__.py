#! /usr/bin/env python
# -*- coding: utf-8 -*-

__version__ = "0.1.0"
__all__ = ["orm", "parser"]

from storm.locals import *
from orm import *

# initializing the relationships
MovieTitlesMetadata.genres = ReferenceSet(MovieTitlesMetadata.id,
                                          MovieGenreLine.movie_id,
                                          MovieGenreLine.genre_id,
                                          Genre.id)

MovieTitlesMetadata.raw_script_url = ReferenceSet(MovieTitlesMetadata.id, RawScriptUrl.movie_id)

Genre.movies = ReferenceSet(Genre.id,
                            MovieGenreLine.genre_id,
                            MovieGenreLine.movie_id,
                            MovieTitlesMetadata.id)

MovieTitlesMetadata.characters = ReferenceSet(
    MovieTitlesMetadata.id, MovieCharactersMetadata.movie_id)

MovieTitlesMetadata.conversations = ReferenceSet(
    MovieTitlesMetadata.id, MovieConversation.movie_id)

MovieConversation.lines = ReferenceSet(MovieConversation.id, MovieLine.conversation_id)
