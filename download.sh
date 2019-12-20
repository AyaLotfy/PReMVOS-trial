#!/bin/bash

# Download and unzip DAVIS train/val if it is not already there (~800MB)
if [ ! -d "./data/DAVIS" ]; then
  echo "################# DOWNLOADING DAVIS DATA #################"
  wget -P ./data https://data.vision.ee.ethz.ch/csergi/share/davis/DAVIS-2017-trainval-480p.zip
  echo "################# UNZIPPING DAVIS DATA #################"
  unzip ./data/DAVIS-2017-trainval-480p.zip -d ./data
fi

# Download and unzip weights if they are not already there  (~3GB)
if [ ! -d "./weights/PReMVOS_weights" ]; then
  echo "################# DOWNLOADING WEIGHTS #################"
  wget -P ./weights https://www.vision.rwth-aachen.de/media/resource_files/PReMVOS_weights.zip
  echo "################# UNZIPPING WEIGHTS #################"
  unzip ./weights/PReMVOS_weights.zip -d ./weights
fi

