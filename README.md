Moriond17 Campaign Production
====

# Setup
```bash
export VO_CMS_SW_DIR=/cvmfs/cms.cern.ch
source $VO_CMS_SW_DIR/cmsset_default.sh
export SCRAM_ARCH=slc6_amd64_gcc481
scram p CMSSW CMSSW_7_1_18
cd CMSSW_7_1_18/src
cmsenv
git-cms-init
git clone git@github.com:jedori0228/sample_production.git
cd sample_production
git checkout -b CMSSW_7_1_18 origin/CMSSW_7_1_18
```

#GEN-SIM (KISTI condor)
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

#GEN-SIM (KNU TIER 2)
* CRAB3 setup
```bash
source /cvmfs/cms.cern.ch/crab3/crab.sh
```

* Change two files in GEN-SIM/CRAB_KNU_TIER2/skeletons/
  * GEN-SIM_crab_skeleton.py
    * CRAB recommends using only one LHE file as an input LHESource. So, if you want to make 100k event, generate a lhe with containing 100k events.
```python
...
# Input source
process.source = cms.Source("LHESource",
    fileNames = cms.untracked.vstring(
##LHE_INPUTS_ARE_HERE## <- your lhe file path
    ),
    inputCommands = cms.untracked.vstring('keep *', 
        'drop LHEXMLStringProduct_*_*_*'),
    dropDescendantsOfDroppedBranches = cms.untracked.bool(False)
)
...
```

    * Below, I assume your cfg file name is GEN-SIM_crab.py
  * crab_skeleton.py : 
```python
...
##requestName## E.g., config.General.requestName = 'MajoranaNeutrinoToMuMuMu_M-40_CMSSW_7_1_18_GEN-SIM'
...
##psetName## E.g., config.JobType.psetName = 'GEN-SIM_crab.py'
...
##outputPrimaryDataset## E.g., config.Data.outputPrimaryDataset = 'MajoranaNeutrinoToMuMuMu_M-40'
...
```

    * Below, I assume your crab cfg file name is crab.py
```bash
crab submit -c crab.py
```
