#!/bin/bash


# Generate general proposals
GENERAL_PROP_LOC=./output/intermediate/general_proposals
if [ ! -d "$GENERAL_PROP_LOC" ]; then
  echo "################# GENERATING GENERAL PROPOSALS #################"
  PROP_NET_GENERAL_WEIGHTS=./weights/PReMVOS_weights/proposal_net/general_weights/proposal_general_weights
  ./code/proposal_net/train.py --forward "$GENERAL_PROP_LOC" --agnostic --second_head --forward_dataset DAVIS --load "$PROP_NET_GENERAL_WEIGHTS" --davis_name "$PWD/seq_to_run.txt"
fi

