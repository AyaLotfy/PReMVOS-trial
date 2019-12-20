#!/bin/bash



# Refine proposals
REFINED_PROP_LOC=./output/intermediate/refined_proposals
if [ ! -d "$REFINED_PROP_LOC" ]; then
  echo "################# GENERATING REFINED PROPOSALS #################"
  cd code
  REFINEMENT_CONFIG=./refinement_net/configs/run
  echo "$REFINEMENT_CONFIG"
  ./refinement_net/main.py "$REFINEMENT_CONFIG"
  cd ..
fi

