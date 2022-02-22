echo "================== START OF CUSTOM CRAB SCRIPT========================="

echo "Add lumi sections to input file"
python custom_crab.py $2
echo "Run CMSSW"
cmsRun -j FrameworkJobReport.xml -p PSet.py

echo "============= END OF CUSTOM CRAB SCRIPT ========================="