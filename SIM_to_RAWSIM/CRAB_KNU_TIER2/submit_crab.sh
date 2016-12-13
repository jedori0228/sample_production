#!/bin/bash

channel=MuMuMU

#for i in 5 10 20 30 40 50 60 70 90 100 150 200 300 400 500 700 1000
for i in 10 30 50 70
do
  cd "crab_"$channel"_"$i
  echo "############################"
  echo "sumbmiting "crab_"$channel"_"$i.py
  crab submit -c crab_"$channel"_$i.py
  cd ..
done
