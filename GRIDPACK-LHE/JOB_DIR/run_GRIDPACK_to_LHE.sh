#!/bin/bash
SECTION=`printf %03d $1`
WORKDIR=`pwd`
export CMS_PATH=/cvmfs/cms.cern.ch
source $CMS_PATH/cmsset_default.sh
export SCRAM_ARCH=slc6_amd64_gcc481
echo "#### unzip CMSSW ####"
tar -zxvf CMSSW_7_1_16_patch2.tar.gz
cd CMSSW_7_1_16_patch2/src
echo "#### Project Rename ####"
scram build ProjectRename
echo "#### cmsenv ####"
eval `scram runtime -sh`
mkdir work
cd $WORKDIR
echo "#### unzip gripack ####"
tar -xaf <GRIDPACK_FILENAME> -C CMSSW_7_1_16_patch2/src/work
cd CMSSW_7_1_16_patch2/src/work
echo "#### generating! ####"
./runcmsgrid.sh <N_EVENT> $(expr $SECTION \* 9) 1
for FILE in cmsgrid_final.lhe; do
    EXT=${FILE##*.}
    PREFIX=${FILE%%.${EXT}}
    xrdcp $FILE root://cms-xrdr.sdfarm.kr:1094//xrd///store/user/<USERNAME>/SOMEWHERE//${PREFIX}_${SECTION}.${EXT}
done
