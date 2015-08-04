# SheRivF
Sherpa,Rivet &amp; FastNLO configs


## Needed:
* Sherpa
* Rivet
* MCgrid
* fastNLO


## Workflow
Build Rivet plugin:
* `rivet-buildplugin RivetMyAnalyses.so MCgrid_CMS_2015_Zee.cc -Wl,--export-dynamic,-z,defs  $(pkg-config mcgrid --cflags) $(pkg-config mcgrid --libs)  -lHepMC -lYODA  -DUSE_FNLO=1`

Rivet output: Rivet.yoda
* (multiple files: `yodamerge *.yoda > Rivet.yoda`)
* convert to root: `yoda_2_root.py Rivet.yoda`

fastNLO output: fnlo_yZ.tab
* (multiple files: `fnlo-tk-append *.tab fnlo.tab`)
* convert to root: `evaluate_fnlotable.py -i fnlo.tab`


Save data in herafitter format
* `makeherafile`, alias defined in ini.sh

Run herafitter
* `herafit`, alias defined in ini.sh

Evaluate PDF sets and save as root files:
* `pdf_2_root.py --folder pdf_sets -p NNPDF23_nlo_as_0118`


Plot the evaluated pdf sets:
* `merlin.py --py pdf -i original.root new.root`
* `merlin.py --py nnpdf`






## Plots
### PDFs
PDF evaluation at different Q:
* merlin.py --py pdfs_thesis

### Data Analysis
* Performance and Efficiencies: electron_plots.py
* Spectra: 

