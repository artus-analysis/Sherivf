# SheRivF
Sherpa,Rivet &amp; FastNLO configs


## Needed:
* Sherpa
* Rivet
* MCgrid
* fastNLO


## Workflow MC
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

## Workflow Data Analysis
make sure the Excalibur outputs are present

1. Subtract backgrounds: `merlin.py --py subtract_backgrounds #--no-ybins`
	root outputs will be stored in `1_background-subtracted` folder
2. Unfold: `merlin.py --py unfold  #--no-ybins --no-mcs`
	root outputs will be stored in `2_unfolded` folder
3. Export unfolded data into herafitter format: `merlin.py --py unfolded_to_hera`




## Plots
##### PDFs
* PDF evaluation at different Q: `merlin.py --py pdfs_thesis`
* Correlation plots: `merlin.py --py pdf_correlations`

##### Electron performance plots
* HLT efficiency: `merlin.py --py z_hlt`
* Electron ID efficiency: `merlin.py --py electron_id`
* Electron corrections: `merlin.py --py electron_corr`
* Effect of electron corrections on Z reconstruction: `merlin.py --py z_corr`

##### Backgrounds
* Distributions with backgrounds: `merlin.py --py zee_bkgrs`
* Background estimation with the e-mu method: `merlin.py --py emu`

##### Unfolding
* Unfolding for different iterations: `merlin.py --py different_iterations`
* Unfolding response matrices: `merlin.py --py response_matrix`
* Comparison of unfolded, reco, gen distributions: `merlin.py --py unfolding_comparison`

