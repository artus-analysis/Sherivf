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

The important configuration files are:
* The Sherpa runcard `sherpa/zjet/Run.dat`, which ...
* The Rivet analysis `rivet/MCgrid_CMS_2015_Zee.cc`, which ...
* The fastNLO steering file , which ...

### `sherivf.py`
This is the main tool for event generation and fastNLO table production.
It is a wrapper script, i.e. it mainly executes other commands in a convenient way for the user.
It has different modes which are detailed below.
After checkout, when using the default configuration, you can skip the *Integration* and *Warmup* steps.
Always make sure you are in the SheRivF directory and have sourced the ini script:

    cd SheRivF
    . scripts/ini_sherivf.sh


* **Rivet analysis compilation**

After every time something in the Rivet analysis file is changed:

    sherivf.py compile

This simply executes a compilation command for the Rivet analysis plugin, located in `rivet/`.

* **Integration run of sherpa**

After every time some physical parameter in the Sherpa runcard `sherpa/zjet/Run.dat` is changed:

    sherivf.py integrate
This deletes old integration files and executes a Sherpa phase space integration run.
This integration run is necessary if a Sherpa configuration is executed for the first time.

* **Warmup run for fastNLO**

After every time something in the Sherpa runcard or the Rivet analysis is changed, the
fastNLO warmup files have to be recreated:

    sherivf.py warmup

The warmup files contain information on the ranges in x and Q^2 in the analysis bins.
The output files are copied into the respective directories.

* **Local testing**

Full run of Sherpa and Rivet.
Use this mode to check if everything works before starting batch production.

    sherivf.py -n 1000

Creates a time-stamped output directory in `test/` which contains the Rivet output (`Rivet.yoda`) and the fastNLO tables.
`-n` specifies the number of events.
With a Z+1Jet@NLO config, 3000000 events roughly correspond to 1h runtime.

* **Batch mode**

For large-scale parallel MC production; get sufficient events even in sparsely poulated phase space regions

    sherivf.py batch -n 1000000 -j 20 -b ekpcluster

`-j` specifies the number of jobs, `-b` the batch resource.

sherivf.py creates a work directory (on a storage server), submits the jobs 
(via grid-control), merges the output `Rivet.yoda` files and the fastNLO
tables and creates a link to the work directory in `results/`.

For debugging of individual jobs, the grid-control and job outputs are located in
`<work-directory>/work.sherpa-rivet_<config>/output/job_<Number>/`, i.e. the
`gc.stdout`, `gc.stderr`, `job.stderr.gz` and `job.stdout.gz` files.

### Helper scripts
* Calculate a cross section from a fastNLO table (with a certain PDF set)
and save as ROOT: 

    evaluate_fnlotable.py -i results/MCgrid_CMS_2015_Zee_zjet/zpt.tab -p NNPDF23_nlo_as_0118

* Correlation plots
The red-blue PDF correlation plots are created with two scripts.
First, the correlations have to be calculated with a fastNLO table and saved as 
ROOT file.
Then, the ROOT 2D-histogram has to be plotted.

    calculate_correlation.py  -t results/MCgrid_CMS_2015_Zee_zjet/zpt.tab -p NNPDF23_nlo_as_0118 -o zpt.root
    plot_correlation.py -i zpt.root -f gluon -o zpt_gluon_corr.png


* fnlostatana script
* pdf to root
    pdf_2_root.py --folder pdf_sets -p NNPDF23_nlo_as_0118




## PDF fits

PDFs are determined by comparing data and theory. 
These PDF fits are performed with [xFitter](https://wiki-zeuthen.desy.de/xFitter/),
a software developed by the HERA collaborations.

For PDF fits, the PDF uncertainties have to be estimated.
This requires to perform multiple fits, each with a slightly different
configuration. This is what requires the parallel execution of xFitter via 
grid-control.


xFitter needs 3 files:
* The steering file `steering.txt` which contains information on data and theory
files and fit settings
* The `minuit.in.txt` file which contains information on the PDF parametrisation,
which parameters are fitted and their starting values
* The `ewparam.txt` which sets the values for some physical parameters like quark
masses

These files are located in the `xfitter/` directory. Some of the variables are
not explicitly set, e.g. `Q02 = @Q02@`. This means the value is set by 
grid-control, perhaps for each job differently.
See also the grid-control steering file  `xfitter/xfitter.conf`.

Right now, 19 jobs are submitted:
1. central fit
2. vary strange quark fraction f_s downwards
...

The script which manages the fitting is `xfit.py` (basically a wrapper to
 grid-control).
Similar to the batch mode of `sherivf.py`, it creates a working directory on 
storage, copies the necessary files there, launches grid-control, handles the
outputs (creates the PDF uncertainties from the results of the different jobs)
and creates a link to the working directory in `results/`.

Two modes:
* `xfit.py hera` to fit only HERA data
* `xfit.py heracms` to fit the combined HERA and CMS data

The precise HERA data are the basis for PDF determination.
With the inclusion of CMS data, i.e. for the comparison between the results from
HERA-only and HERA+CMS, we are interested in two things:

* How does the PDFs change? (Does the gluon become harder)?
* How do the PDF uncertainties change? (Are the uncertainties reduced with CMS
data?)



Plot the results:

    plot_pdf.py

