# Sherivf 
Toolkit for PDF studies with  **She**rpa, **Riv**et, **f**astNLO and xFitter.

![Workflow](docs/workflow.png?raw=true)


## Installation instructions 
can be found in a separate file [here](https://github.com/artus-analysis/Sherivf/blob/master/INSTALLATION.md).


## Introduction to PDF fits
For PDF determination, theory calculations for different PDF sets are compared
with data. The PDFs which lead to the best agreement with data are determined.

For fast cross section predictions with different PDFs, *fastNLO* tables are needed.
These can be produced by *Rivet* which processes events generated by *Sherpa*
(and Blackhat). The fastNLO tables are used by *xFitter* which compares data and
theory and thereby determines the PDF.

## Monte Carlo simulation and fastNLO table production
Sherpa is used for Monte Carlo event generation.
The events are then passed to Rivet which implements analysis steps such as phase space cuts or Z boson reconstruction.
MCgrid, a Rivet plugin, generates the fastNLO tables necessary for PDF fits.

The important configuration files are:
* The Sherpa runcard `sherpa/zjet/Run.dat`, which defines what process is simulated
* The Rivet analysis `rivet/MCgrid_CMS_2015_Zee.cc`, which defines event selection
and histogram / fastNLO table creation
* The fastNLO steering file `fastnlo/MCgrid_CMS_2015_Zee.str`, which defines a few fastNLO settings

### `sherivf.py`
This is the main tool for event generation and fastNLO table production.
It is a wrapper script, i.e. it mainly executes other commands in a convenient way for the user.
It has different modes which are detailed below.
After checkout, when using the default configuration, you can skip the *Integration* and *Warmup* steps.
Always make sure you are in the Sherivf directory and have sourced the ini script:

    cd Sherivf
    . scripts/ini_sherivf.sh


**Rivet analysis compilation**

After every time something in the Rivet analysis file is changed:

    sherivf.py compile

This simply executes a compilation command for the Rivet analysis plugin, located in `rivet/`.

**Integration run of sherpa**

After every time some physical parameter in the Sherpa runcard `sherpa/zjet/Run.dat` is changed:

    sherivf.py integrate
This deletes old integration files and executes a Sherpa phase space integration run.
This integration run is necessary if a Sherpa configuration is executed for the first time.

**Warmup run for fastNLO**

After every time something in the Sherpa runcard or the Rivet analysis is changed, the
fastNLO warmup files have to be recreated:

    sherivf.py warmup

The warmup files contain information on the ranges in x and Q^2 in the analysis bins.
The output files are copied into the respective directories.
It might be necessary to increase the number of events 

**Local testing**

Full run of Sherpa and Rivet.
Use this mode to check if everything works before starting batch production.

    sherivf.py local -n 10000

Creates a time-stamped output directory in `test/` which contains the Rivet output (`Rivet.yoda`) and the fastNLO tables.
`-n` specifies the number of events.
With a Z+1Jet@NLO config, 3000000 events roughly correspond to 1h runtime.

**Batch mode**

For large-scale parallel MC production; get sufficient events even in sparsely populated phase space regions

    sherivf.py batch -n 1000000 -j 20

`-j` specifies the number of jobs, `-b` the batch resource.

sherivf.py creates a work directory (on a storage server), submits the jobs 
(via grid-control), merges the output `Rivet.yoda` files and the fastNLO
tables and creates a link to the work directory in `results/`.
The cross section in the merged `Rivet.yoda` file needs to be manually scaled by
the inverse of the number of jobs.

For debugging of individual jobs, the grid-control and job outputs are located in
`<work-directory>/work.sherpa-rivet_<config>/output/job_<Number>/`, i.e. the
`gc.stdout`, `gc.stderr`, `job.stderr.gz` and `job.stdout.gz` files.

Depending of the batch system you use it may be possible that the merging of the job outputs fails (for example on the NAF when the tables are too big). In this case, the job will finish with status failed. Don't worry, if this happens, you can merge the job outputs manually using

    fnlo-tk-merge name_of_joboutput_*.tab some_filename.tab

### Helper scripts
Some handy scripts located in the `scripts/` folder:

**fastNLO table evaluation**

Calculate a cross section from a fastNLO table (with a certain PDF set)
and save as ROOT: 


    evaluate_fnlotable.py -i results/MCgrid_CMS_2015_Zee_zjet/zpt.tab -p NNPDF23_nlo_as_0118

**Correlation plots**

The red-blue PDF correlation plots are created with two scripts.
First, the correlations have to be calculated with a fastNLO table and saved as 
ROOT file.
Then, the ROOT 2D-histogram has to be plotted.
E.g., for the correlation plot of the gluon PDF and the cross section as a 
function of Z pT, using the NNPDF 2.3 PDF set:

    calculate_correlation.py  -t results/MCgrid_CMS_2015_Zee_zjet/zpt.tab -p NNPDF23_nlo_as_0118 -o zpt.root
    plot_correlation.py -i zpt.root -f gluon -o zpt_gluon_corr.png


**Statistical check of fastNLO tables**
For sparsely populated (= only few events) bins, large NLO event weights 
can bias the bin cross section.
If you have a number of fastNLO tables, you can identify tables for which the
cross section in a bin deviated by more than X sigma from the median of all tables:

    fnlostatana.py -i /storage/a/dhaitz/sherivf/ekpcluster_2016-06-16_13-35/output/ -r "^zpt.*$"

The `-r` argument is a regex expression to match the relevant files in the folder.
The script will create plots for all bins. With `--filter` the 'critical' tables
are automatically moved to a subfolder.
Use this script if you have produced a lot of events but still have some
fluctuations in the outer bins. 

**PDFs as ROOT graphs**

To get a PDF from a LHAPDF set a certain energy scale, use

    pdf_2_root.py -p NNPDF30_nlo_as_0118 -q 91.2  # Q=91.2
    pdf_2_root.py -p NNPDF30_nlo_as_0118 -q 1.9 --q2  # Q^2=1.9
(ToDo: `--q2` to have a squared value: should this be made more intuitive?)

### Instructions for using fastNLO tables with Artus

HarryPlotter offers the possibility to import fastNLO tables to calculate e.g. theory uncertainties. You can use the input_module InputFastNLO for this purpose. You have to execute ini_sherivf.sh to use this input module. 
Scale calculations with HOPPET are included in the module, make sure you have HOPPET interfaced in fastNLO for an adequate calculation of scale uncertainties.

## PDF fits

PDFs are determined by comparing data and theory.
These PDF fits are performed with [xFitter](https://wiki-zeuthen.desy.de/xFitter/),
a software developed by the HERA collaborations.

For PDF fits, the PDF uncertainties have to be estimated.
This requires to perform multiple fits, each with a slightly different
configuration. This is what requires the parallel execution of xFitter via
grid-control.

xFitter needs 3 files:
* The steering file `steering.txt` which contains information on data files and fit settings
* The `minuit.in.txt` file which contains information on the PDF parametrisation,
which parameters are fitted and their starting values
* The `ewparam.txt` which sets the values for some physical parameters like quark
masses

These files are located in the `xfitter/` directory. Some of the variables are
not explicitly set, e.g. `Q02 = @Q02@`. This means the value is set by
grid-control, perhaps for each job differently.
See also the grid-control steering file  `xfitter/xfitter.conf`.

Right now, 19 jobs are submitted.
The first job (job 0) is the central fit with the experimental errors.
Jobs 1-8 are for the model uncertainties,
Jobs 9-18 for the parametrisation uncertainties.

* Job 0: Central fit
* Job 1: Vary strange quark fraction f_s downwards
* Job 2: Vary strange quark fraction f_s upwards
* Job 3: Vary charm quark mass downwards
* Job 4: Vary charm quark mass upwards
* Job 5: Vary bottom quark mass downwards
* Job 6: Vary bottom quark mass upwards
* Job 7: Vary minimum Q^2 for DIS data downwards
* Job 8: Vary minimum Q^2 for DIS data upwards
* Job 9: Vary the starting scale of the PDF fit Q_0^2 downwards
* Job 10: Vary the starting scale of the PDF fit Q_0^2 upwards
* Job 11 -- Job 18: For each job an additional parameter is added

The script which manages the fitting is `xfit.py` (basically a wrapper to
 grid-control).
Similar to the batch mode of `sherivf.py`, it creates a working directory on
storage, copies the necessary files there, launches grid-control, handles the
outputs (creates the PDF uncertainties from the results of the different jobs)
and creates a link to the working directory in `results/`.

It has two modes:
* `xfit.py hera` to fit only HERA data
* `xfit.py heracms` to fit the combined HERA and CMS data

###### Datafile format
For the CMS mode, you can edit which data files are used, see [here](https://github.com/artus-analysis/Sherivf/blob/941675807d/scripts/xfit.py#L30-L34)
(set `self.corrfiles_cms = []` if you have no correlation files).
An example for a datafile is [here](https://github.com/artus-analysis/Sherivf/blob/94167580/datafiles/zjet/CMS_Zee_HFinput_zpt_inclusive.txt).
Edit the binning (1st and 2nd column), cross section values (3rd column) and
statistical uncertainties (4th column).
The following columns are for the systematic errors.
[NData](https://github.com/artus-analysis/Sherivf/blob/94167580/datafiles/zjet/CMS_Zee_HFinput_zpt_inclusive.txt#L9)
has to match the number of data points,
[NColumn](https://github.com/artus-analysis/Sherivf/blob/94167580/datafiles/zjet/CMS_Zee_HFinput_zpt_inclusive.txt#L10)
has to match the number of columns.
*TheoryInfoFile* is the fastNLO table you produced (of course for the same
process that was measured!)

###### Output
The output are the fitted PDFs `pdf_?.root` at three scales: Q^2=1.9, Q^2=10.0 and Q=91.2 GeV.
For debugging, have a look at the individual job log files as described in the
*Batch mode* section for `sherivf.py`.

For each job, the `job_?_fittedresults.txt` file contains information about the
theory and data values as well as the nuisance parameter shifts/pulls.
The `job_?_plots.pdf` contains plots of these values created with 
xFitter's own plotting tool.
Chi^2 values are written to `job_?_Results.txt`.
The PDF parameter values can be found in `job_?_minuit.out.txt`.

The precise HERA data are the basis for PDF determination.
With the inclusion of CMS data, i.e. for the comparison between the results from
HERA-only and HERA+CMS, we are interested in two things:

* How does the PDFs change? (Does the gluon become harder)?
* How do the PDF uncertainties change? (Are the uncertainties reduced with CMS
data?)


#### Important notes for `xfit.py` usage:
* In the xfitter steering file, a [cut on the Z pT above 200 GeV](https://github.com/artus-analysis/Sherivf/blob/a63bd84/xfitter/steering.txt#L250-L252)
is implemented because of insufficiencies of the 8 TeV cross section calculation.
Should be disabled for future (13 TeV) studies.
* Because of unresolved reconstruction issues at 8 TeV,
the datafiles for the highest rapidity was not used, see [this line](https://github.com/artus-analysis/Sherivf/blob/a63bd8409d24b18624b3a848dd49d2d7c1c4589f/scripts/xfit.py#L32)
This should probably be deactivated for 13 TeV studies.
* The [chi^2](https://github.com/artus-analysis/Sherivf/blob/7dae32703fce664112fd1bd637292a22253adc20/xfitter/steering.txt#L138)
 does currently not include the Poisson Correction (perhaps it should ...)
* For testing purposes, the [HF (Heavy Flavour) Scheme used by xFitter](https://github.com/artus-analysis/Sherivf/blob/7dae32703fce664112fd1bd637292a22253adc20/xfitter/steering.txt#L97)
 can be set to `RT OPT FAST`.
This accelerates the fitting procedure.
However, it yields slightly different values so don't use it for results
you want to present.
* To also fit alpha_s together with the PDFs, the value for the alphas *step*
 (the first value [here]( https://github.com/artus-analysis/Sherivf/blob/7dae32703fce664112fd1bd637292a22253adc20/xfitter/steering.txt#L155))
could be set to > 0.


#### Plot the resulting PDFs:

    plot_pdf.py -i results/hera/pdf_1_9_squared.root -f gluon -o out.png

ToDo: modify the script (or write a new one) to enable comparison plots, i.e.
plot the total (experimental+model+parametrisation) uncertainties for two PDF sets.
