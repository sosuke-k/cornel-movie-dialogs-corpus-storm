# cornel-movie-dialogs-corpus-storm
A set of python modules for cornel movie-dialogs corpus with storm.

## Abstract

This module include some classes extending [storm](https://storm.canonical.com/) ORM for [cornel movie-dialogs corpus](http://www.mpi-sws.org/~cristian/Cornell_Movie-Dialogs_Corpus.html) data.

## Install

```
pip install storm                # if you not
pip install cornel-movie-dialogs-corpus-storm
```

## Usage

```
from mdcorpus.orm import *
from mdcorpus.parser import *

...

```

## Class List

* MovieTitlesMetadata
* Genre
* MovieGenreLine
* MovieCharactersMetadata
* MovieConversation
* MovieLine
* RawScriptUrl

## Corpus Problem

This is memo when I dealt with corpus problems.

### movie_titles_metadata.txt

* I ignored an **alphabet** following year.
    * for example, line 34, `1989/I`
* I ignored **duplication** for genre data.
    * line 58, `['horror', 'mystery', 'mystery', 'sci-fi', 'sci-fi']`

## Code Problem

I use `Python2.7` and I don't know how to use `codecs` module.([Unicode HOWTO — Python 2.7ja1 documentation](http://docs.python.jp/2/howto/unicode.html))

### movie_titles_metadata.txt

* I adjust title data for **Acute accent** manually.
    * line 115, `léon`

### movie_characters_metadata.txt

* I adjust title data for **Acute accent** manually.
    * line 1727 - 1736, `léon`
