RunIIFall17MiniAOD-94X_mc2017_realistic
====

# Setup
```bash
export VO_CMS_SW_DIR=/cvmfs/cms.cern.ch
source $VO_CMS_SW_DIR/cmsset_default.sh
export SCRAM_ARCH=slc6_amd64_gcc630
scram p CMSSW CMSSW_9_3_4
cd CMSSW_9_3_4/src
cmsenv
git-cms-init
git clone git@github.com:jedori0228/sample_production.git
cd sample_production
git checkout -b RunIIFall17MiniAOD-94X_mc2017_realistic__LHE__TO__GEN-SIM origin/RunIIFall17MiniAOD-94X_mc2017_realistic__LHE__TO__GEN-SIM
## Go to a separate directory to clone genproduction
## I will use home directory
cd ~
git clone git@github.com:cms-sw/genproductions.git
NLO_HADRONIZER=$PWD/genproductions/python/ThirteenTeV/Hadronizer/Hadronizer_TuneCP5_13TeV_aMCatNLO_0p_LHE_pythia8_cff.py
cd $CMSSW_BASE/src
mkdir -p Configuration/GenProduction/python/
cp $NLO_HADRONIZER Configuration/GenProduction/python/
scram b -j 8
cd $CMSSW_BASE/src/sample_production
```
