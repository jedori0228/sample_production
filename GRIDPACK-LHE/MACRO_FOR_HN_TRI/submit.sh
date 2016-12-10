#!/bin/bash
finalstate="SSSF_MuMuE"
for m in 5 10 20 30 40 50 60 70 90 100 150 200 300 400 500 700 1000
#for m in 10 20 30 40 50 60 70 90 100 150 200 300 400 500 700 1000
do
  cd "MajoranaNeutrinoTo"$finalstate"_M-"$m
  condor_submit submit.jds
  cd ..
done
