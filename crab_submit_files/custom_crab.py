#! /usr/bin/env python

import sys
import subprocess
import pickle
import json
import FWCore.ParameterSet.Config as cms

assert(len(sys.argv)==2)

period = 5
remainder = int(sys.argv[1].split('=')[1])
print('period, remainder', period, remainder)

cfg = pickle.load(open('PSet.pkl'))
print('original source:')
print(cfg.source)

xrdNames = []
for fileName in cfg.source.fileNames:
    xrdNames.append('root://xrootd-cms.infn.it/'+fileName)

runlumis = json.loads(subprocess.check_output('edmLumisInFiles.py ' + ' '.join(xrdNames), shell=True))

cfg.source.lumisToProcess = cms.untracked.VLuminosityBlockRange()

for run in runlumis:
    lumipairs = runlumis[run]
    for l1,l2 in lumipairs:
        for li in range(l1,l2+1):
            if li%period == remainder:
                cfg.source.lumisToProcess.append('%s:%i-%s:%i' % (run.encode(),li,run.encode(),li))

print('modified source:')
print(cfg.source)

with open('PSet.pkl', 'wb') as handle:
    pickle.dump(cfg, handle)

# edmLumisInFiles.py root://xrootd-cms.infn.it//store/mc/RunIISummer20UL16MiniAOD/WminusJetsToTauNu_TauToMu_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/00000/006B67C5-B922-D646-B0AC-9774918B1987.root