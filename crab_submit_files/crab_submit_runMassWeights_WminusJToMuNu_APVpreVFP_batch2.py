from CRABClient.UserUtilities import config
config = config()

config.General.requestName = 'runMassWeights_WminusJToMuNu_APVpreVFP_batch2'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.numCores = 1
config.JobType.maxMemoryMB = 2000
config.JobType.maxJobRuntimeMin = 2400
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = '../configs/runMassWeights_WminusJToMuNu_cfg.py'
config.JobType.scriptExe = 'custom_crab.sh'
config.JobType.inputFiles = ['custom_crab.py']
config.JobType.scriptArgs = ['remainder=2']
config.JobType.allowUndistributedCMSSW = True

config.Data.inputDataset = '/WminusJetsToMuNu_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM'
config.Data.allowNonValidInputDataset = True

config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.outLFNDirBase = '/store/group/cmst3/group/wmass/w-mass-13TeV/edmLHE' 
config.Data.publication = True
config.Data.outputDatasetTag = 'LHE_massWeights_miniv2_APVpreVFP'

config.Site.storageSite = 'T2_CH_CERN'
config.Site.blacklist = ['T2_US_Caltech']