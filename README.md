# SheRivF
Sherpa,Rivet &amp; FastNLO configs


## Needed:
* Sherpa 2.2.0
* Rivet 2.3
* MCgrid 2.0
* fastNLO 2.3.1pre-2125


## Workflow MC
Build Rivet plugin:
* `rivet-buildplugin RivetMyAnalyses.so MCgrid_CMS_2015_Zee.cc -Wl,--export-dynamic,-z,defs  $(pkg-config mcgrid --cflags) $(pkg-config mcgrid --libs)  -lHepMC -lYODA  -DUSE_FNLO=1`

Rivet output: Rivet.yoda
* (multiple files: `yodamerge *.yoda > Rivet.yoda`)
* convert to root: `yoda_2_root.py Rivet.yoda`

fastNLO output: fnlo_yZ.tab
* (multiple files: `fnlo-tk-append *.tab fnlo.tab`)
* convert to root: `evaluate_fnlotable.py -i fnlo.tab`
* make all correlation root files (needed for correlation plots): `calculate_all_correlations`

`sherivf.py`
30000000 -> 10h job


Evaluate PDF sets and save as root files:
* `pdf_2_root.py --folder pdf_sets -p NNPDF23_nlo_as_0118`

Generate ROOT files for PDF plots:
* `pdfs_for_plotting.py`

Correlation plots

## Workflow Data Analysis
make sure the Excalibur outputs are present

`make_analysis`
(`clear_analysis`)


## Workflow PDF fits
* send to batch with `hera.py`
* NNPDF reweighting with `nnpdf.py`
* from the outputs, create PDF root file with `make_pdfuncs`
* delete PDF root files with `clear_pdfuncs`


![My image](test.png?raw=true)
