RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic__RECO__TO__MiniAOD
====

RECO to MiniAOD : Based on [HIG-RunIIFall17MiniAODv2-00355](https://cms-pdmv.cern.ch/mcm/requests?prepid=HIG-RunIIFall17MiniAODv2-00355&page=0&shown=127)

# Setup

```bash
export VO_CMS_SW_DIR=/cvmfs/cms.cern.ch
source $VO_CMS_SW_DIR/cmsset_default.sh
export SCRAM_ARCH=slc6_amd64_gcc630
scram p CMSSW CMSSW_9_4_6_patch1
cd CMSSW_9_4_6_patch1/src
cmsenv
git-cms-init
git clone git@github.com:jedori0228/sample_production.git sample_production
cd sample_production
git checkout -b RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic__RECO__TO__MiniAOD origin/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic__RECO__TO__MiniAOD
```

cfg file for "AODSIM__TO__MINIAODSIM"

```bash
cd $CMSSW_BASE/src/sample_production/AODSIM__TO__MINIAODSIM/
cmsDriver.py step1 \
--filein file:AODSIM.root \
--fileout MINIAODSIM.root \
--mc \
--eventcontent MINIAODSIM \
--runUnscheduled \
--datatier MINIAODSIM \
--conditions 94X_mc2017_realistic_v14 \
--step PAT \
--nThreads 4 \
--scenario pp \
--era Run2_2017,run2_miniAOD_94XFall17 \
--python_filename AODSIM__TO__MINIAODSIM.py \
--no_exec \
-n 4800
```

# Submitting Jobs with CRAB

Write a txt file with das names of samples

e.g.,

```bash
$ cat filelist.txt
/TEST_CRAB/jskim-CMSSW_9_4_0_patch1_AODSIM-351414bbda2cdc38d49da1680cef2a3f/USER
```

Then, 

```bash
python make_crab_cfg.py &> script_crab_submit.sh
```

This create a script for submittion

```bash
$ cat script_crab_submit.sh 
## TEST_CRAB
cd crab_TEST_CRAB
crab submit -c crab_TEST_CRAB.py
cd -
```

Then,

```bash
source script_crab_submit.sh
```

