#!/bin/bash


# Run method on sequences defined in ./seq_to_run.txt

# Calculate optical flow
FLOW_LOC=./output/intermediate/flow
if [ ! -d "$FLOW_LOC" ]; then
  echo "################# GENERATING FLOW #################"
  ./code/optical_flow_net-PWC-Net/script_pwc_multi.py
fi

