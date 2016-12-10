import os

masses = [5, 10, 20, 30, 40, 50, 60, 70, 90, 100, 150, 200, 300, 400, 500, 700, 1000]

finalstate="MuMuMu"

for mass in masses:
  channel = 'MajoranaNeutrinoTo'+finalstate
  dirname = 'MajoranaNeutrinoTo'+finalstate+'_M-'+str(mass)

  os.system('mkdir /xrootd/store/user/jskim/lhe/'+dirname)

  os.system('mkdir '+dirname)
  runsh = open(dirname+'/run.sh', 'w')
  print>>runsh, """#!/bin/bash
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
tar -xaf {0}_5f_LO_tarball.tar.xz -C CMSSW_7_1_16_patch2/src/work
cd CMSSW_7_1_16_patch2/src/work
echo "#### generating! ####"
./runcmsgrid.sh 1000 $(expr $SECTION \* 9) 1
for FILE in cmsgrid_final.lhe; do""".format(dirname)
  runsh.write("    EXT=${FILE##*.}\n")
  runsh.write("    PREFIX=${FILE%%.${EXT}}\n")
  runsh.write("    xrdcp $FILE root://cms-xrdr.sdfarm.kr:1094//xrd///store/user/jskim/lhe/"+dirname+"//${PREFIX}_${SECTION}.${EXT}\n")
  runsh.write("done\n")
  runsh.close()

  submitjds = open(dirname+'/submit.jds', 'w')
  print>>submitjds, """executable = run.sh
universe   = vanilla
arguments  = $(Process)
requirements = OpSysMajorVer == 6
log = condor.log
getenv     = True
should_transfer_files = YES
when_to_transfer_output = ON_EXIT
output = job_$(Process).log
error = job_$(Process).err
transfer_input_files = /cms/scratch/jskim/gridpacks/{0}_gridpacks/{1}_5f_LO_tarball.tar.xz, ../CMSSW_7_1_16_patch2.tar.gz
queue 100""".format(channel,dirname)
  submitjds.close()

