# SheRivF 
Toolkit for PDF studies with  Sherpa, Rivet, fastNLO and xFitter.

TODO: bild mit komplettem workflow


## Installation instructions 
can be found [here](https://github.com/dhaitz/SheRivF/blob/master/INSTALLATION.md).


## Introduction to PDF fits


## Monte Carlo simulation and fastNLO table production
Sherpa is used for Monte Carlo event generation.
The events are then passed to Rivet which implements analysis steps such as phase space cuts or Z boson reconstruction.
MCgrid, a Rivet plugin, generates the fastNLO tables necessary for PDF fits.


### `sherivf.py`
This is the main tool for event generation and fastNLO table production.
It is a wrapper script, i.e. it mainly executes other commands in a convenient way for the user.
It has different modes which are detailed below.
After checkout, when using the default configuration, you can start with the *Local testing* step.
Always make sure you are in the SheRivF directory and have sourced the ini script:

    cd SheRivF
    . scripts/ini_sherivf.sh


* **Rivet analysis compilation**

After every time something in the Rivet analysis file is changed:

    `sherivf.py --compile`

This simply executes a compilation command in the for the Rivet analysis plugin.

* **Integration run of sherpa**

After every time some physical parameter in the Sherpa runcard is changed:

    `sherivf.py --integrate`
This deletes old integration files and executes a Sherpa phase space integration run.
This integration run is necessary if a Sherpa configuration is executed for the first time.

* **Warmup run for fastNLO**

After every time something in the Sherpa runcard or the Rivet analysis is changed, the
fastNLO warmup files have to be recreated:

    `sherivf.py --integrate`

The warmup files contain information on the ranges in x and Q^2 in the analysis bins.
The output files are copied into the respective directories.

* **Local testing**

Full run of Sherpa and Rivet.
Use this mode to check if everything works before starting batch production.

    `sherivf.py -n 1000`

Creates a time-stamped output directory in `test/` which contains the Rivet output (`Rivet.yoda`) and the fastNLO tables.
`-n` specifies the number of events.

* **Batch mode**

For large-scale parallel MC production; get sufficient events even in sparsely poulated phase space regions

    `sherivf.py -n 1000000 -j 20 -b ekpcluster`

`-j` specifies the number of events.

create workdir, send jobs, merge fnlo, link

debug

### Helper scripts
* convert fastNLO table to root: `evaluate_fnlotable.py -i fnlo.tab`

* correlation plots

    calculate_correlation.py
    plot_correlation.py


`sherivf.py`
3000000 events correspond to 1h runtime


* fnlostatana
* pdf to root
	`pdf_2_root.py --folder pdf_sets -p NNPDF23_nlo_as_0118`




## PDF fits
Send to batch with `xfit.py`
Two modes:

* `xfit.py hera` to fit only HERA data
* `xfit.py heracms` to fit the combined HERA and cms data

