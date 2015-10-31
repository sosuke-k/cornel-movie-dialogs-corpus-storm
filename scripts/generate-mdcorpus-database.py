#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os.path
import argparse
from storm.locals import *
from mdcorpus.orm import *
from mdcorpus.parser import *

# generate-mdcorpus-database.py --corpus-dir "cornell movie-dialogs corpus" corpus.db


def generate(corpus_dir, dtype="sqlite", dpath="corpus.db"):
    print "create " + dpath
    database = create_database(dtype + ":" + dpath)
    # database = create_database(dtype + ":")
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
        print "parsing genres..."
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
        print "commiting genres..."
        store.commit()

    # insert movies
    with open(os.path.join(corpus_dir, "movie_titles_metadata.txt"), "r") as f:
        print "parsing movies..."
        line = f.readline()
        while line:
            data = parser.movie_titles_metadata(line)
            genres = data.pop()
            movie = store.add(MovieTitlesMetadata(*data))
            for genre_name in genres:
                genre = store.find(Genre, Genre.name == genre_name.decode('utf-8')).one()
                movie.genres.add(genre)
            line = f.readline()
        print "commiting movies..."
        store.commit()

    # insert characters
    with open(os.path.join(corpus_dir, "movie_characters_metadata.txt"), "r") as f:
        print "parsing characters..."
        line = f.readline()
        while line:
            data = parser.movie_characters_metadata(line)
            movie_id = data[2]
            character = store.add(MovieCharactersMetadata(data[0], data[1], data[-2], data[-1]))
            character.movie_id = movie_id
            line = f.readline()
        print "commiting characters..."
        store.commit()

    # insert lines
    with open(os.path.join(corpus_dir, "movie_lines.txt"), "r") as f:
        print "parsing lines..."
        line = f.readline()
        while line:
            data = parser.movie_lines(line)
            store.add(MovieLine(data[0], data[-1]))
            line = f.readline()
        print "commiting lines..."
        store.commit()

    # insert conversations
    with open(os.path.join(corpus_dir, "movie_conversations.txt"), "r") as f:
        print "parsing conversations..."
        line = f.readline()
        while line:
            data = parser.movie_conversations(line)
            line_id_list = data.pop()
            conversation = store.add(MovieConversation(*data))
            for (i, line_id) in enumerate(line_id_list):
                line = store.find(MovieLine, MovieLine.id == line_id).one()
                line.number = i + 1
                conversation.lines.add(line)
            line = f.readline()
        print "commiting conversations..."
        store.commit()

    # insert urls
    with open(os.path.join(corpus_dir, "raw_script_urls.txt"), "r") as f:
        print "parsing urls..."
        line = f.readline()
        while line:
            data = parser.raw_script_urls(line)
            movie_id = data[0]
            url = RawScriptUrl(data[-1])
            url.movie_id = movie_id
            line = f.readline()
        print "commiting urls..."
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

    lines = store.find(MovieLine)
    if lines.count() == 304713:
        print "all lines inserted"
    else:
        print "something wrong with MovieLine"

    conversations = store.find(MovieConversation)
    if conversations.count() == 83097:
        print "all conversations inserted"
    else:
        print "something wrong with MovieConversation"


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
