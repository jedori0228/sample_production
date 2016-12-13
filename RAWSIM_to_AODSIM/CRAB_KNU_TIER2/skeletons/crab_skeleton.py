from CRABClient.UserUtilities import config, getUsernameFromSiteDB

config = config()

##requestName## E.g., config.General.requestName = 'MajoranaNeutrinoToMuMuMu_M-40_CMSSW_8_0_21_AODSIM'
config.General.workArea = 'crab_projects'
config.General.transferLogs = True
config.General.transferOutputs = True

config.JobType.pluginName = 'Analysis'
##psetName## E.g., config.JobType.psetName = 'RAWSIM_to_AODSIM.py'
config.JobType.maxMemoryMB = 4000

##inputDataset## E.g., config.Data.inputDataset = '/MajoranaNeutrinoToMuMuMu_M-5/jskim-CMSSW_8_0_21_RAWSIM-16ca0fac1b892ff3c3d45d801745cbbf/USER'
config.Data.inputDBS = 'phys03'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())
config.Data.publication = True
config.Data.outputDatasetTag = 'CMSSW_8_0_21_AODSIM'
config.Data.ignoreLocality = True

config.Site.storageSite = 'T2_KR_KNU'
