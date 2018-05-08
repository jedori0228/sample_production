from CRABClient.UserUtilities import config, getUsernameFromSiteDB

config = config()

##requestName## E.g., config.General.requestName = 'MajoranaNeutrinoToMuMuMu_M-40_CMSSW_7_1_18_GEN-SIM'
config.General.workArea = 'crab_projects'
config.General.transferLogs = True
config.General.transferOutputs = True

config.JobType.pluginName = 'PrivateMC'
##psetName## E.g., config.JobType.psetName = 'GEN-SIM_crab.py'
config.JobType.numCores = 8

##outputPrimaryDataset## E.g., config.Data.outputPrimaryDataset = 'MajoranaNeutrinoToMuMuMu_M-40'
config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())
config.Data.outputDatasetTag = 'CMSSW_9_3_4_GEN-SIM'
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 1000
NJOBS = 100

config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.publication = True

config.Site.storageSite = 'T3_KR_KNU'
