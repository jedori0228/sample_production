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
cd sample_production
git checkout -b CMSSW_8_0_21 origin/CMSSW_8_0_21
## To Use CRAB3,
source /cvmfs/cms.cern.ch/crab3/crab.sh
```

# SIM to RAWSIM (KISTI condor)
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

# SIM to RAWSIM (KNU TIER 2 CRAB3)

* **SIM_to_RAWSIM/CRAB_KNU_TIER2/skeletons/crab_skeleton.py** :
```python
...
##requestName## E.g., config.General.requestName = 'MajoranaNeutrinoToMuMuMu_M-40_CMSSW_8_0_21_RAWSIM'
...
##psetName## E.g., config.JobType.psetName = 'SIM_to_RAWSIM.py'
...
##inputDataset## E.g., config.Data.inputDataset = '/MajoranaNeutrinoToMuMuMu_M-150/jskim-CMSSW_7_1_18_GEN-SIM-c2345211336d5844e3ea1a8a7fbfc845/USER'
...
```
* If you have your GEN-SIM Datasetname in google spreadsheet format like [this](https://docs.google.com/spreadsheets/d/1aUoEq40MjpZ4LpcEoxXdd9-prrDmJkWWgeKPLPsmBhk/edit?usp=sharing), you can make use of the script to craete crab job directory
  * **File** -> **Publish to the web** -> Change **Web page** to **Comma-separated values (.csv)** -> **Publish** -> Copy the link
  * SIM_to_RAWSIM/CRAB_KNU_TIER2/make_crab_cfg.py :
```python
    url = 'https://docs.google.com/spreadsheets/d/1aUoEq40MjpZ4LpcEoxXdd9-prrDmJkWWgeKPLPsmBhk/pub?gid=0&single=true&output=csv'
```

# RAWSIM to AODSIM (KISTI condor)
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

# RAWSIM to AODSIM (KNU TIER 2 CRAB3)

* **RAWSIM_to_AODSIM/KNU_TIRE2_CRAB3/skeletons/crab_skeleton.py** :
```python
...
##requestName## E.g., config.General.requestName = 'MajoranaNeutrinoToMuMuMu_M-40_CMSSW_8_0_21_AODSIM'
...
##psetName## E.g., config.JobType.psetName = 'RAWSIM_to_AODSIM.py'
...
##inputDataset## E.g., config.Data.inputDataset = '/MajoranaNeutrinoToMuMuMu_M-5/jskim-CMSSW_8_0_21_RAWSIM-16ca0fac1b892ff3c3d45d801745cbbf/USER'
...
```
* If you have your RAWSIM Datasetname in google spreadsheet format like [this](https://docs.google.com/spreadsheets/d/1aUoEq40MjpZ4LpcEoxXdd9-prrDmJkWWgeKPLPsmBhk/edit?usp=sharing), you can make use of the script to craete crab job directory
  * **File** -> **Publish to the web** -> Change **Web page** to **Comma-separated values (.csv)** -> **Publish** -> Copy the link
  * RAWSIM_to_AODSIM/CRAB_KNU_TIER2/make_crab_cfg.py :
```python
    url = 'https://docs.google.com/spreadsheets/d/1aUoEq40MjpZ4LpcEoxXdd9-prrDmJkWWgeKPLPsmBhk/pub?gid=0&single=true&output=csv'
```

# AODSIM to MiniAOD (KISTI condor)
```bash
cd AODSIM_to_MiniAOD
```
* Make a txt file of input lhe file path
  * (SE)  /store/<SOMEWHERE>
  * (Local file) file:/LOCAL/FILE/PATH
* Fix submit_batch.sh file properly
```bash
source submit_batch.sh
