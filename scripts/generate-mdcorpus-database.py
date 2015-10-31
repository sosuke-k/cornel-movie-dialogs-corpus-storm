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
    database = create_database(dtype + ":" + dpath)
    store = Store(database)
    store.execute(MovieTitlesMetadata.CREATE_SQL)
    store.execute(Genre.CREATE_SQL)
    store.execute(MovieGenreLine.CREATE_SQL)
    store.execute(MovieCharactersMetadata.CREATE_SQL)
    store.execute(MovieConversation.CREATE_SQL)
    store.execute(MovieLine.CREATE_SQL)
    store.execute(RawScriptUrl.CREATE_SQL)

    parser = Parser()

    for file_name in FILES:
        parse_func = getattr(parser, file_name, None)
        with open(os.path.join(corpus_dirfile_name, file_name + ".txt"), "r") as f:
            line = f.readline()
            while line:
                print line
                l = parse_func(line)
                print l
                line = f.readline()


def main():

    parser = argparse.ArgumentParser(
        description="Generator of database from cornel movie-dialogs corpus")
    parser.add_argument("dpath", nargs=1, help="path to database file")
    parser.add_argument("--dtype", type=str, default="sqlite",
                        help="Select database type, but now alternatives is only sqlite XD")
    parser.add_argument("--corpus-dir", type=str, required=True)
    args = parser.parse_args()

    print args.__dict__         # 'dtype': 'sqlite', 'dpath': ['database.db']}

if __name__ == "__main__":
    main()
