#cd /portal/ekpcms6/home/dhaitz/qcd/SHERPA-MC-2.1.1/Examples/V_plus_Jets/LHC_ZJets
#cd -
export LD_LIBRARY_PATH=/usr/users/dhaitz/local/lib:/usr/users/dhaitz/local/lib64:$LD_LIBRARY_PATH

echo $PWD
/usr/users/dhaitz/local/bin/Sherpa RESULT_DIRECTORY=$PWD -f /portal/ekpcms6/home/dhaitz/qcd/SHERPA-MC-2.1.1/Examples/V_plus_Jets/LHC_ZJets/Run.dat -R @SEED_j@
#sherpa_zjet.hepmc

