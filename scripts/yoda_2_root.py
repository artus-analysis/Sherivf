#! /usr/bin/env python

"""
	originally from http://www-pnp.physics.ox.ac.uk/~henderson/Other_stuff/scripts/yoda2root.python
"""

import os, sys, array, ROOT
ROOT.gROOT.SetBatch()

input_files = []

#if len(sys.argv) == 2:
input_files.append(sys.argv[1])
#elif len(sys.argv) > 1:
#    input_files = sys.argv[1,-1]
#else:
#    for f in os.listdir("."):
#        if ".yoda" in f: input_files.append( f )
#        pass
#    pass

if len(sys.argv) > 2:
    num_batchJobs = float(sys.argv[2])
else:
    num_batchJobs = 1

for f in input_files:
    convert_command = "yoda2flat " + f
    print convert_command
    os.system( convert_command )
    
    in_f = open( os.path.basename(f).replace(".yoda",".dat") , "r" )
    
    histos = []
    bins = []
    errors = []
    values = []
    last_bin_upper = 0
    histName = ""
    in_plot = False
    for i, line in enumerate(in_f):
        
        if "# BEGIN HISTOGRAM" in line: 
            histName = line.split("/")[-1][:-1] # -> sth like d01-x01-y01
        elif "# END HISTOGRAM" in line: 
            bins.append( last_bin_upper )
            in_plot = False
            new_histo = ROOT.TH1D( histName, histName, len(bins) - 1, array.array('d', bins ) )
            for bin,v in enumerate(values):
                new_histo.SetBinContent( bin + 1, v )
                new_histo.SetBinError( bin + 1, errors[bin] )
                pass
            histos.append( new_histo )
            bins = []
            values = []
            errors = []
            histName = ""
            last_bin_upper = 0
            continue
        
        elif "# xlow" in line:
            in_plot = True
            continue

        elif "# BEGIN HISTOGRAM /MC_VBF/" in line:
            histName = line.split("# BEGIN HISTOGRAM /MC_VBF/")[1].strip()
            continue
        
        elif in_plot:
            bins.append( float(line.split()[0]) )
            values.append( float(line.split()[2]) )
            errors.append( float(line.split()[3]) )
            last_bin_upper = float(line.split()[1])
            pass

        
        pass
    out_file = ROOT.TFile( f.replace(".yoda",".root"), "RECREATE" )
    for h in histos:
        h.Scale( 1. / num_batchJobs );
        h.Write()
        pass
    out_file.Close()
    in_f.close()
    pass

