from CRABClient.UserUtilities import config, getUsernameFromSiteDB

config = config()

##requestName## E.g., config.General.requestName = 'MajoranaNeutrinoToMuMuMu_M-40_CMSSW_8_0_21_MiniAOD'
config.General.workArea = 'crab_projects'
config.General.transferLogs = True
config.General.transferOutputs = True

config.JobType.pluginName = 'Analysis'
##psetName## E.g., config.JobType.psetName = 'AODSIM_to_MiniAOD.py'
config.JobType.maxMemoryMB = 4000

##inputDataset## E.g., config.Data.inputDataset = '/MajoranaNeutrinoToMuMuMu_M-5/jskim-CMSSW_8_0_21_AODSIM-e82b9d23b21065f4c0a0b29f84898dde/USER'
config.Data.inputDBS = 'phys03'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())
config.Data.publication = True
config.Data.outputDatasetTag = 'CMSSW_8_0_21_MiniAOD'
config.Data.ignoreLocality = True

config.Site.storageSite = 'T2_KR_KNU'
