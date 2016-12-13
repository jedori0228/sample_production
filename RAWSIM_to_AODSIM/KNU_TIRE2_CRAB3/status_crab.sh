#!/bin/bash

channel=MuMuMU

#for i in 5 10 20 30 40 50 60 70 90 100 150 200 300 400 500 700 1000
for i in 5 30
do
  cd crab_MajoranaNeutrinoToMuMuMu_$i
  echo "############################"
  echo "Status of "MajoranaNeutrinoToMuMuMu_M-$i
  crab status -d crab_projects/crab_MajoranaNeutrinoToMuMuMu_M-$i"_CMSSW_8_0_21_AODSIM/"
  cd ..
done
