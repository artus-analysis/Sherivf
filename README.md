# SheRivF
Sherpa,Rivet &amp; FastNLO configs

## Installation
found in https://github.com/dhaitz/SheRivF/blob/master/INSTALLATION.md

## Usage
 bild mit komplettem workflow


### Monte Carlo simulation and fastNLO table production
fastNLO tables allow
they are necessary for 
needed for PDF fits

are created from Monte Carlo events
Rivet, which implements phase space cuts and e.g. Z boson reconstruction 
MCgrid, rivet plugin, generates fastNLO tables


 
 

sherivf
Different modes:
Rivet analysis compilation
Integration run of sherpa
warmup
local for testing  
* sherivf.py -s zjet --rivet MCgrid_CMS_2015_Zee -n 1000
batch mode for large-scale production for enough events in distant phase space


* convert fastNLO table to root: `evaluate_fnlotable.py -i fnlo.tab`

* correlation plots


`sherivf.py`
3000000 events correspond to 1h runtime


other scripts
* fnlostatana
* pdf to root
	`pdf_2_root.py --folder pdf_sets -p NNPDF23_nlo_as_0118`
* yoda2root

Build Rivet plugin:
* `rivet-buildplugin RivetMyAnalyses.so MCgrid_CMS_2015_Zee.cc -Wl,--export-dynamic,-z,defs  $(pkg-config mcgrid --cflags) $(pkg-config mcgrid --libs)  -lHepMC -lYODA  -DUSE_FNLO=1`




### PDF fits
* send to batch with `hera.py`
 


![My image](docs/test.png?raw=true)
