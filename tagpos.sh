#!/bin/bash

if [ $# -ne 1 ]; then
    echo "Usage: $0 <input file>"
    exit 1
fi

cat $1 | curl 'http://localhost:9000/?properties={%22annotators%22%3A%22tokenize%2Cssplit%2Cpos%22%2C%22outputFormat%22%3A%22json%22}' -o - -d @- > $1.json
