#!/bin/bash




# Run merging algorithm
MERGE_OUT_LOC=./output/final
if [ ! -d "$MERGE_OUT_LOC" ]; then
  echo "################# Merging #################"
  cd code
  ./MergeTrack/merge.py
  cd ..
fi
