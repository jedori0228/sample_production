Moriond17 Campaign Production
====

# Setup
```bash
export VO_CMS_SW_DIR=/cvmfs/cms.cern.ch
source $VO_CMS_SW_DIR/cmsset_default.sh
export SCRAM_ARCH=SCRAM_ARCH=slc6_amd64_gcc481
cmsrel CMSSW_7_1_16_patch2
cd CMSSW_7_1_16_patch2/src
cmsenv
git-cms-init
git clone git@github.com:jedori0228/sample_production.git
cd sample_production.git
git checkout -b CMSSW_7_1_16_patch2 origin/CMSSW_7_1_16_patch2
```

# GRIDPACK to LHE
```bash
cd GRIDPACK-LHE/JOB_DIR
```
* Fix submit.jds
  * change "\<GRIDPACK_FILEPATH\>" to your gridpack file **PATH**
* Fix run_GRIDPACK_to_LHE.sh
  * change "\<GRIDPACK_FILENAME\>" to your gridpack file **NAME**
  * change "\<USERNAME\>/SOMEWHERE" to output directory
```bash
condor_submit submit.jds
```
