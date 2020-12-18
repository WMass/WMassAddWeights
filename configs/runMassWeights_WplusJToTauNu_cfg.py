import FWCore.ParameterSet.Config as cms

from Configuration.Eras.Era_Run2_2016_cff import Run2_2016

process = cms.Process('MassWeights',Run2_2016)
process.options   = cms.untracked.PSet( wantSummary = cms.untracked.bool(True) )

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(10)
)

# Input source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
      '/store/mc/RunIISummer20UL16MiniAOD/WplusJetsToTauNu_TauToMu_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/00000/00325874-34FD-0440-AAC2-51F755DA8AE5.root'
    ),
    secondaryFileNames = cms.untracked.vstring()
)

process.options = cms.untracked.PSet()


# Output definition

process.MINIAODSIMoutput = cms.OutputModule("PoolOutputModule",
    compressionAlgorithm = cms.untracked.string('LZMA'),
    compressionLevel = cms.untracked.int32(4),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('MINIAODSIM'),
        filterName = cms.untracked.string('')
    ),
    dropMetaData = cms.untracked.string('ALL'),
    eventAutoFlushCompressedSize = cms.untracked.int32(-900),
    fastCloning = cms.untracked.bool(False),
    fileName = cms.untracked.string('file:SMP-RunIISummer20UL16MiniAOD-massWeights.root'),
    outputCommands = cms.untracked.vstring(
        'drop *',
        'keep *_correctMassWeights_*_*',
        'keep GenRunInfoProduct_*_*_*',
        'keep LHERunInfoProduct_*_*_*',
        'keep GenFilterInfo_*_*_*',
        'keep GenLumiInfoHeader_*_*_*',
        'keep GenLumiInfoProduct_*_*_*',
    ),
    overrideInputFileSplitLevels = cms.untracked.bool(True),
    splitLevel = cms.untracked.int32(0)
)


process.correctMassWeights = cms.EDProducer("ExternalLHEProducer",
    args = cms.vstring('/cvmfs/cms.cern.ch/phys_generator/gridpacks/slc6_amd64_gcc700/13TeV/powheg/Vj_NNLOPS/Wj_slc6_amd64_gcc700_CMSSW_10_2_23_WplusJToTauNu-suggested-nnpdf31-ncalls-doublefsr-q139-ckm-powheg-MiNNLO31-svn3756-ew-rwl6-j200-st2fix-ana-hoppetweights-ymax20-addmassweights.tgz'),
    nEvents = cms.untracked.int32(-1),
    numberOfParameters = cms.uint32(1),
    outputFile = cms.string('cmsgrid_final.lhe'),
    scriptName = cms.FileInPath('GeneratorInterface/LHEInterface/data/run_generic_tarball_cvmfs.sh'),
    generateConcurrently = cms.untracked.bool(False),
)
process.RandomNumberGeneratorService.correctMassWeights = cms.PSet(
  initialSeed = cms.untracked.uint32(234567),
  engineName = cms.untracked.string('MixMaxRng')
)


process.lhe_Step = cms.Path(process.correctMassWeights)
process.MINIAODSIMoutput_step = cms.EndPath(process.MINIAODSIMoutput)

process.schedule = cms.Schedule(process.lhe_Step, process.MINIAODSIMoutput_step)
