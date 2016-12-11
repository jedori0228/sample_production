Moriond17 Campaign Production
====

# Setup
```bash
export VO_CMS_SW_DIR=/cvmfs/cms.cern.ch
source $VO_CMS_SW_DIR/cmsset_default.sh
export SCRAM_ARCH=slc6_amd64_gcc530
scram p CMSSW CMSSW_8_0_21
cd CMSSW_8_0_21/src
cmsenv
git-cms-init
git clone git@github.com:jedori0228/sample_production.git
cd sample_production.git
git checkout -b CMSSW_8_0_21 origin/CMSSW_8_0_21
```

# SIM to RAWSIM
```bash
cd SIM_to_RAWSIM
voms-proxy-init --voms cms -valid 24:00
```
* Make a txt file of input lhe file path
  * (SE)  /store/<SOMEWHERE>
  * (Local file) file:/LOCAL/FILE/PATH
```bash
cd JOB_DIR
```
* Fix submit.jds
  * change "/tmp/x509up_u\<ID\>" to your grid certificate, located in /tmp/
    * ID can be obatained, using "id -u" in command line
  * change "filelist_GEN-SIM.txt" to your input filelist
  * change "queue 10" to total # of input files
* Fix run_SIM_to_RAWSIM.sh
  * change "\<USERNAME\>/SOMEWHERE" to output directory
```bash
condor_submit submit.jds
```

# RAWSIM to AODSIM
```bash
cd RAWSIM_to_AODSIM
```
* Make a txt file of input lhe file path
  * (SE)  /store/<SOMEWHERE>
  * (Local file) file:/LOCAL/FILE/PATH
* Fix submit_batch.sh file properly
```bash
source submit_batch.sh
```

# AODSIM to MiniAOD
```bash
cd AODSIM_to_MiniAOD
```
* Make a txt file of input lhe file path
  * (SE)  /store/<SOMEWHERE>
  * (Local file) file:/LOCAL/FILE/PATH
* Fix submit_batch.sh file properly
```bash
source submit_batch.sh
