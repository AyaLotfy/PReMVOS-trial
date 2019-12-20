#!/bin/bash



# Add ReID to proposals
ReID_PROP_LOC=./output/intermediate/ReID_proposals
if [ ! -d "$ReID_PROP_LOC" ]; then
  echo "################# GENERATING ReID PROPOSALS #################"
  cd code
  ReID_CONFIG=./ReID_net/configs/run
  echo "$ReID_CONFIG"
  ./ReID_net/main.py "$ReID_CONFIG"
  cd ..
fi

