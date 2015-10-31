#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os.path
import argparse
from storm.locals import *
from mdcorpus.orm import *
from mdcorpus.parser import *

# generate-mdcorpus-database.py dataset/corpus.db --dtype sqlite

FILES = ["movie_titles_metadata",
         "movie_characters_metadata",
         "movie_lines",
         "movie_conversations",
         "raw_script_urls"]


def generate(corpus_dir, dtype="sqlite", dpath="corpus.db"):
    # print "created " + dpath
    # database = create_database(dtype + ":" + dpath)
    database = create_database(dtype + ":")
    store = Store(database)
    store.execute(MovieTitlesMetadata.CREATE_SQL)
    store.execute(Genre.CREATE_SQL)
    store.execute(MovieGenreLine.CREATE_SQL)
    store.execute(MovieCharactersMetadata.CREATE_SQL)
    store.execute(MovieConversation.CREATE_SQL)
    store.execute(MovieLine.CREATE_SQL)
    store.execute(RawScriptUrl.CREATE_SQL)

    parser = Parser()

    # insert genres
    with open(os.path.join(corpus_dir, "movie_titles_metadata.txt"), "r") as f:
        genre_set = Set([])
        line = f.readline()
        while line:
            data = parser.movie_titles_metadata(line)
            genres = data.pop()
            for genre in genres:
                if genre != '':
                    genre_set.add(genre)
            line = f.readline()
        for genre in genre_set:
            store.add(Genre(genre))
        store.flush()

    # insert movies
    with open(os.path.join(corpus_dir, "movie_titles_metadata.txt"), "r") as f:
        line = f.readline()
        while line:
            data = parser.movie_titles_metadata(line)
            genres = data.pop()
            movie = store.add(MovieTitlesMetadata(*data))
            for genre_name in genres:
                genre = store.find(Genre, Genre.name == genre_name.decode('utf-8')).one()
                movie.genres.add(genre)
            line = f.readline()
        store.flush()

    # insert characters
    with open(os.path.join(corpus_dir, "movie_characters_metadata.txt"), "r") as f:
        line = f.readline()
        while line:
            data = parser.movie_characters_metadata(line)
            movie_id = data[2]
            character = store.add(MovieCharactersMetadata(data[0], data[1], data[-2], data[-1]))
            character.movie_id = movie_id
            line = f.readline()
        store.flush()

    store.commit()

    # check
    # - 220,579 conversational exchanges between 10,292 pairs of movie characters
    # - involves 9,035 characters from 617 movies
    # - in total 304,713 utterances
    movies = store.find(MovieTitlesMetadata)
    if movies.count() == 617:
        print "all movies inserted"
    else:
        print "something wrong with MovieTitlesMetadata"
    characters = store.find(MovieCharactersMetadata)
    if characters.count() == 9035:
        print "all characters inserted"
    else:
        print "something wrong with MovieCharactersMetadata"


def main():

    parser = argparse.ArgumentParser(
        description="Generator of database from cornel movie-dialogs corpus")
    parser.add_argument("dpath", nargs=1, help="path to database file")
    parser.add_argument("--dtype", type=str, default="sqlite",
                        help="Select database type, but now alternatives is only sqlite XD")
    parser.add_argument("--corpus-dir", type=str, required=True)
    args = parser.parse_args()

    generate(args.corpus_dir, dtype=args.dtype, dpath=args.dpath[0])

if __name__ == "__main__":
    main()
