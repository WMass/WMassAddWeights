# WMassAddWeights

## How to run

release to use: >= CMSSW_10_6_17_patch1, <= analysis release (https://twiki.cern.ch/twiki/bin/viewauth/CMS/WmassAnalysis)


```
cmsrel CMSSW_10_6_17_patch1
cd CMSSW_10_6_17_patch1/src
cmsenv
# Patch ExternalLHEProducer
git cms-init
git cms-merge-topic intrepid42:ExternalLHEProducer_int_106X
scram b -j 5

mkdir Configuration
cd Configuration
git clone git@github.com:intrepid42/WMassAddWeights.git
scram b

cd WMassAddWeights/configs
cmsRun runMassWeights_ZJToMuMu_cfg.py
```

## Input datasets

```
dasgoclient -query "dataset=/*powhegMiNNLO-pythia8-photos/*/MINIAODSIM"

/DYJetsToMuMu_M-50_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos/RunIISummer20UL16MiniAOD-106X_mcRun2_asymptotic_v13-v2/MINIAODSIM
/DYJetsToMuMu_M-50_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos/RunIISummer20UL16MiniAODAPV-106X_mcRun2_asymptotic_preVFP_v8-v2/MINIAODSIM
/DYJetsToTauTau_M-50_AtLeastOneEorMuDecay_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos/RunIISummer20UL16MiniAOD-106X_mcRun2_asymptotic_v13-v2/MINIAODSIM
/DYJetsToTauTau_M-50_AtLeastOneEorMuDecay_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos/RunIISummer20UL16MiniAODAPV-106X_mcRun2_asymptotic_preVFP_v8-v2/MINIAODSIM
<WminusJetsToMuNu missing>
/WminusJetsToTauNu_TauToMu_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos/RunIISummer20UL16MiniAOD-106X_mcRun2_asymptotic_v13-v2/MINIAODSIM
/WminusJetsToTauNu_TauToMu_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos/RunIISummer20UL16MiniAODAPV-106X_mcRun2_asymptotic_preVFP_v8-v2/MINIAODSIM
/WplusJetsToMuNu_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos/RunIISummer20UL16MiniAOD-106X_mcRun2_asymptotic_v13-v2/MINIAODSIM
/WplusJetsToMuNu_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos/RunIISummer20UL16MiniAODAPV-106X_mcRun2_asymptotic_preVFP_v8-v2/MINIAODSIM
/WplusJetsToTauNu_TauToMu_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos/RunIISummer20UL16MiniAOD-106X_mcRun2_asymptotic_v13-v2/MINIAODSIM
/WplusJetsToTauNu_TauToMu_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos/RunIISummer20UL16MiniAODAPV-106X_mcRun2_asymptotic_preVFP_v8-v2/MINIAODSIM
```

## Output datasets

```
dasgoclient -query "dataset=/*/mseidel-LHE_massWeights*/USER instance=prod/phys03"

/DYJetsToMuMu_M-50_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos/mseidel-LHE_massWeights-883f8224005bb85ca71ea2ca271fa8bd/USER
```
