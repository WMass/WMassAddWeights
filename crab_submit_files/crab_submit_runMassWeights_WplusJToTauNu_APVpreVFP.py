from CRABClient.UserUtilities import config
config = config()

config.General.requestName = 'runMassWeights_WplusJToTauNu_APVpreVFP'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.numCores = 1
config.JobType.maxMemoryMB = 2000
config.JobType.maxJobRuntimeMin = 2400
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = '../configs/runMassWeights_WplusJToTauNu_cfg.py'
config.JobType.allowUndistributedCMSSW = True

config.Data.inputDataset = '/WplusJetsToTauNu_TauToMu_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos/RunIISummer20UL16MiniAODAPV-106X_mcRun2_asymptotic_preVFP_v8-v2/MINIAODSIM'
config.Data.allowNonValidInputDataset = True

config.Data.splitting = 'EventAwareLumiBased'
config.Data.unitsPerJob = 20000
config.Data.outLFNDirBase = '/store/group/cmst3/group/wmass/w-mass-13TeV/edmLHE' 
config.Data.publication = True
config.Data.outputDatasetTag = 'LHE_massWeights_APVpreVFP'

config.Site.storageSite = 'T2_CH_CERN'
