#!/bin/bash


# Generate specific proposals
SPECIFIC_PROP_LOC=./output/intermediate/specific_proposals
if [ ! -d "$SPECIFIC_PROP_LOC" ]; then
  echo "################# GENERATING SPECIFIC PROPOSALS #################"
  PROP_NET_SPECIFIC_WEIGHTS=./weights/PReMVOS_weights/proposal_net/specific_weights/proposal_specific_weights
  ./code/proposal_net/train.py --forward "$SPECIFIC_PROP_LOC" --agnostic --second_head --forward_dataset DAVIS --load "$PROP_NET_SPECIFIC_WEIGHTS" --davis_name "$PWD/seq_to_run.txt"
fi

