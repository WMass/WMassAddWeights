# source /cvmfs/cms.cern.ch/common/crab-setup.sh
# ls $DBS3_CLIENT_ROOT/examples/DataOpsScripts/

SAMPLES=(/WminusJetsToMuNu_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos/mseidel-LHE_massWeights-4a2bb86276b1969ddeeb407ab73f93f5/USER /WminusJetsToMuNu_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos/mseidel-LHE_massWeights-50c3a2a176cbcdb1adbe28619c6bf254/USER /WminusJetsToMuNu_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos/mseidel-LHE_massWeights-5627df1619a9340d11b065994372dffa/USER /WminusJetsToMuNu_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos/mseidel-LHE_massWeights-5ae5fd1369f6eb9ec974beb5f0ec0d4d/USER /WminusJetsToMuNu_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos/mseidel-LHE_massWeights-b80465f0830b5b897efef5078a24dcb2/USER /WminusJetsToMuNu_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos/mseidel-LHE_massWeights_APVpreVFP-4a2bb86276b1969ddeeb407ab73f93f5/USER /WminusJetsToMuNu_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos/mseidel-LHE_massWeights_APVpreVFP-50c3a2a176cbcdb1adbe28619c6bf254/USER /WminusJetsToMuNu_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos/mseidel-LHE_massWeights_APVpreVFP-5627df1619a9340d11b065994372dffa/USER /WminusJetsToMuNu_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos/mseidel-LHE_massWeights_APVpreVFP-5ae5fd1369f6eb9ec974beb5f0ec0d4d/USER /WminusJetsToMuNu_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos/mseidel-LHE_massWeights_APVpreVFP-b80465f0830b5b897efef5078a24dcb2/USER)

# python $DBS3_CLIENT_ROOT/examples/DataOpsScripts/DBS3SetDatasetStatus.py --dataset=<datasetname> --url=https://cmsweb.cern.ch/dbs/prod/phys03/DBSWriter --status=INVALID --recursive=False

for SAMPLE in ${SAMPLES[@]}
do
    echo ${SAMPLE}
    python $DBS3_CLIENT_ROOT/examples/DataOpsScripts/DBS3SetDatasetStatus.py --dataset=${SAMPLE} --url=https://cmsweb.cern.ch/dbs/prod/phys03/DBSWriter --status=INVALID --recursive=False
done