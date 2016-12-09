Moriond17 Campaign Production
====

# Setup
```bash
export VO_CMS_SW_DIR=/cvmfs/cms.cern.ch
source $VO_CMS_SW_DIR/cmsset_default.sh
export SCRAM_ARCH=SCRAM_ARCH=slc6_amd64_gcc481
cmsrel CMSSW_7_1_18
cd CMSSW_7_1_18/src
cmsenv
git-cms-init
git clone git@github.com:jedori0228/sample_production.git
cd sample_production.git
git checkout -b CMSSW_7_1_18 origin/CMSSW_7_1_18
```

#GEN-SIM
```bash
cd GEN-SIM
```
* Make a txt file of input lhe file path
  * (SE)  /store/<SOMEWHERE>
  * (Local file) file:/LOCAL/FILE/PATH
* Fix submit_batch.sh file properly
```bash
source submit_batch.sh
```
