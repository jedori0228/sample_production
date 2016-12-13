#!/bin/bash                                                                                                                                                                                                                                                                     

channel=MupEp
for i in 40
do
  cd "crab_MajoranaNeutrinoTo"$channel"_"$i
  echo "############################"
  echo "sumbmiting crab_"$channel"_"$i.py
  crab submit -c crab_MajoranaNeutrinoTo"$channel"_$i.py
  cd ..
done
