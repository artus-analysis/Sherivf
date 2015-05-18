# SheRivF
Sherpa,Rivet &amp; FastNLO configs


## Needed:
* Sherpa
* Rivet
* MCgrid
* fastNLO


Build Rivet plugin:
	`rivet-buildplugin RivetMyAnalyses.so MCgrid_CMS_2015_Zee.cc -Wl,--export-dynamic,-z,defs  $(pkg-config mcgrid --cflags) $(pkg-config mcgrid --libs)  -lHepMC -lYODA  -DUSE_FNLO=1"`

Rivet output: Rivet.yoda
* (multiple files: `yodamerge *.yoda > Rivet.yoda`)
* convert to root: `yoda_2_root.py Rivet.yoda`

fastNLO output: fnlo_yZ.txt
* (multiple files: `fnlo-tk-append *.txt fnlo.txt`)
* convert to root: `evaluate_fnlotable.py -i fnlo.txt`
