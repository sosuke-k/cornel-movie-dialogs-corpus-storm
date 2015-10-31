#!/bin/bash

for pyfile in $( ls . | grep .py$ ); do
python "${pyfile}"
done
