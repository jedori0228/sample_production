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
git clone git@github.com:jedori0228/sample_production.git RunIIFall17MiniAOD-94X_mc2017_realistic__LHE__TO__GEN-SIM
cd RunIIFall17MiniAOD-94X_mc2017_realistic__LHE__TO__GEN-SIM
git checkout -b RunIIFall17MiniAOD-94X_mc2017_realistic__LHE__TO__GEN-SIM origin/RunIIFall17MiniAOD-94X_mc2017_realistic__LHE__TO__GEN-SIM
```
Go to a separate directory to clone genproduction

I will use home directory

```bash
cd ~
git clone git@github.com:cms-sw/genproductions.git
NLO_HADRONIZER=$PWD/genproductions/python/ThirteenTeV/Hadronizer/Hadronizer_TuneCP5_13TeV_aMCatNLO_0p_LHE_pythia8_cff.py
cd $CMSSW_BASE/src
mkdir -p Configuration/GenProduction/python/
cp $NLO_HADRONIZER Configuration/GenProduction/python/
scram b -j 8
cd $CMSSW_BASE/src/RunIIFall17MiniAOD-94X_mc2017_realistic__LHE__TO__GEN-SIM
```

# Submitting Jobs with CRAB

Write a txt file with,

\<Sample Alias\> \<lhefile path, starting with /store\>

e.g.,

```bash
$ cat filelist.txt 
PairProduction_MuMu_ZR3000_N200_WR5000_NLO /store/user/jskim/SE_UserHome/lhe/LRSM/PairProduction_MuMu_ZR3000_N200_WR5000_NLO/events.lhe 
```

Then, 

```bash
python make_crab_cfg.py &> script_crab_submit.sh
```

This create a script for submittion

```bash
$ cat script_crab_submit.sh 
## PairProduction_MuMu_ZR3000_N200_WR5000_NLO
cd crab_PairProduction_MuMu_ZR3000_N200_WR5000_NLO
crab submit -c crab_PairProduction_MuMu_ZR3000_N200_WR5000_NLO.py
cd -
```

Then,

```bash
source script_crab_submit.sh
```
