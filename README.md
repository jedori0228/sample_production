RunIIFall17MiniAOD-94X_mc2017_realistic
====

GEN-SIM to HLT : Based on [HIG-RunIIFall17DRPremix-00035](https://cms-pdmv.cern.ch/mcm/requests?prepid=HIG-RunIIFall17DRPremix-00035&page=0&shown=127)

HLT to RECO : Based on [HIG-RunIIFall17DRPremix-00035](https://cms-pdmv.cern.ch/mcm/requests?prepid=HIG-RunIIFall17DRPremix-00035&page=0&shown=127)

RECO to MiniAOD : Based on [HIG-RunIIFall17MiniAOD-00032](https://cms-pdmv.cern.ch/mcm/requests?prepid=HIG-RunIIFall17MiniAOD-00032&page=0&shown=127)

# Setup

```bash
export VO_CMS_SW_DIR=/cvmfs/cms.cern.ch
source $VO_CMS_SW_DIR/cmsset_default.sh
export SCRAM_ARCH=slc6_amd64_gcc630
scram p CMSSW CMSSW_9_4_0_patch1
cd CMSSW_9_4_0_patch1/src
cmsenv
git-cms-init
git clone git@github.com:jedori0228/sample_production.git sample_production
cd sample_production
git checkout -b RunIIFall17MiniAOD-94X_mc2017_realistic__GEN-SIM__TO__MiniAOD origin/RunIIFall17MiniAOD-94X_mc2017_realistic__GEN-SIM__TO__MiniAOD
```

cfg file for "GEN-SIM to HLT"

```bash
cd $CMSSW_BASE/src/sample_production/GEN-SIM__TO__HLT/
cmsDriver.py step1 \
--filein file:GEN-SIM.root \
--fileout HLT.root  \
--pileup_input pu.root \
--mc \
--eventcontent PREMIXRAW \
--datatier GEN-SIM-RAW \
--conditions 94X_mc2017_realistic_v10 \
--step DIGIPREMIX_S2,DATAMIX,L1,DIGI2RAW,HLT:2e34v40 \
--nThreads 8 \
--datamix PreMix --era Run2_2017 \
--python_filename GEN-SIM__TO__HLT.py \
--no_exec \
-n 1751
```

# Submitting Jobs with CRAB

