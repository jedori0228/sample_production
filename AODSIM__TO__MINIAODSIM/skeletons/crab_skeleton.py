from CRABClient.UserUtilities import config, getUsernameFromSiteDB

config = config()

##requestName## E.g., config.General.requestName = 'MajoranaNeutrinoToMuMuMu_M-40_CMSSW_8_0_21_RAWSIM'
config.General.workArea = 'crab_projects'
config.General.transferLogs = True
config.General.transferOutputs = True

config.JobType.pluginName = 'Analysis'
##psetName## E.g., config.JobType.psetName = 'SIM_to_RAWSIM.py'
#config.JobType.numCores = 8
#config.JobType.maxMemoryMB = 4000

##inputDataset## E.g., config.Data.inputDataset = '/MajoranaNeutrinoToMuMuMu_M-150/jskim-CMSSW_7_1_18_GEN-SIM-c2345211336d5844e3ea1a8a7fbfc845/USER'
config.Data.inputDBS = 'phys03'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())
config.Data.publication = True
config.Data.outputDatasetTag = 'CMSSW_9_4_0_patch1_MINIAODSIM'

config.Site.storageSite = 'T3_KR_KNU'
