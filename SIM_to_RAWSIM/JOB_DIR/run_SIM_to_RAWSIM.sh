#!/bin/bash
SECTION=`printf %03d $1`
WORKDIR=`pwd`
export CMS_PATH=/cvmfs/cms.cern.ch
source $CMS_PATH/cmsset_default.sh
export SCRAM_ARCH=slc6_amd64_gcc530

echo "#### ls ####"
ls
echo "#### copy grid cert ####"
cp "x509up_u"* "/tmp/x509up_u"`id -u`
echo "#### unzip CMSSW ####"
tar -zxvf CMSSW_8_0_21.tar.gz
cd CMSSW_8_0_21/src
echo "#### Project Rename ####"
scram build ProjectRename
echo "#### cmsenv ####"
eval `scram runtime -sh`
mkdir work
cd $WORKDIR
cd CMSSW_8_0_21/src/work
echo "#### copying input and MinBias filelist ####"
cp $WORKDIR/SIM_to_RAWSIM.py ./
cp $WORKDIR/filelist_GEN-SIM.txt ./
cp $WORKDIR/filelist_MinBias.txt ./
echo "#### running! ####"
echo "cmsRun SIM_to_RAWSIM.py filelist_GEN-SIM.txt "$SECTION" filelist_MinBias.txt"
cmsRun SIM_to_RAWSIM.py filelist_GEN-SIM.txt $SECTION filelist_MinBias.txt
for FILE in RAWSIM.root; do
    EXT=${FILE##*.}
    PREFIX=${FILE%%.${EXT}}
    xrdcp $FILE root://cms-xrdr.sdfarm.kr:1094//xrd///store/user/jskim/CMSSW_8_0_21_RAWSIM/MajoranaNeutrinoToMuMuMu_M-40//${PREFIX}_${SECTION}.${EXT}
done
