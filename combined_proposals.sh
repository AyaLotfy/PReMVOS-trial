#!/bin/bash



# Combine general and specific proposals
COMBINED_PROP_LOC=./output/intermediate/combined_proposals
if [ ! -d "$COMBINED_PROP_LOC" ]; then
  echo "################# GENERATING COMBINED PROPOSALS #################"
  ./code/proposal_net/combine_general_and_specific.py
fi
