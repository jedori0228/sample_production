#!/bin/bash

channel=MuMuMU

for i in 5 10 20 30 40 50 60 70 90 100 150 200 300 400 500 700 1000
#for i in 5
#for i in 10 20 30 50 70 90 100 150 200 300 400 500 700 1000
do
  cd crab_MuMuMu_$i
  echo "############################"
  echo "resubmitting "MajoranaNeutrinoToMuMuMu_M-$i
  crab resubmit -d crab_projects/crab_MajoranaNeutrinoToMuMuMu_M-$i"_CMSSW_7_1_18_GEN-SIM/"
  cd ..
done
