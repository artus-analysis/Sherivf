# SheRivF 
Sherpa,Rivet &amp; FastNLO configs

## Installation
found [here](https://github.com/dhaitz/SheRivF/blob/master/INSTALLATION.md)

## Usage
 bild mit komplettem workflow


### Monte Carlo simulation and fastNLO table production
fastNLO tables are necessary for PDF fits.

are created from Monte Carlo events
Rivet, which implements phase space cuts and e.g. Z boson reconstruction 
MCgrid, rivet plugin, generates fastNLO tables


 
 
#### `sherivf.py`
This is the main
it has Different modes.
After checkout, when using the default configuration, you can start with the *Local testing* step.

* **Rivet analysis compilation**
After every time something in the rivet analysis file is changed:

    `sherivf.py --compile`

* **Integration run of sherpa**
After every time something in Sherpa runcard is changed:

    `sherivf.py --integrate`

* **Warmup run for fastNLO**
After every time something in the Sherpa runcard or the Rivet analysis is changed, the
fastNLO warmup files have to be recreated:

    `sherivf.py --integrate`

* **Local testing**
Full run of Sherpa and Rivet.
Creates time-stamped output directories in `test/`.
Use this mode to check if everything works before going to batch production.

    `sherivf.py -n 1000`

* **Batch mode**
for large-scale MC production; get enough sufficient events even in sparsely poulated phase space regions

    `sherivf.py -n 1000`

#### Helper scripts
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
Send to batch with `xfit.py`
Two modes:

* `xfit.py hera` to fit only HERA data
* `xfit.py heracms` to fit the combined HERA and cms data




![My image](docs/test.png?raw=true)
