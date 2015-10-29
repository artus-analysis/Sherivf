import FWCore.ParameterSet.Config as cms

process = cms.Process("TagProbe")
process.source = cms.Source("EmptySource")
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(1) )

process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.destinations = ['cout', 'cerr']
process.MessageLogger.cerr.FwkReport.reportEvery = 1000


##                      _              _       
##   ___ ___  _ __  ___| |_ __ _ _ __ | |_ ___ 
##  / __/ _ \| '_ \/ __| __/ _` | '_ \| __/ __|
## | (_| (_) | | | \__ \ || (_| | | | | |_\__ \
##  \___\___/|_| |_|___/\__\__,_|_| |_|\__|___/
##                                              
################################################


isMC = False
InputFileName = "tnp_{0}.root".format('mc' if isMC else 'data')
OutputFilePrefix = "efficiency-{0}-".format('mc' if isMC else 'data')

################################################
HLTDef = "probe_passingHLT"
PDFName = "pdfSignalPlusBackground"

################################################

#specifies the binning of parameters
EfficiencyBins = cms.PSet(
    probe_sc_et = cms.vdouble(25, 30, 35, 40, 45, 50, 200),
    probe_sc_eta = cms.vdouble(0.0, 0.5, 1.0, 1.5, 2.0, 2.5)
)

## for super clusters
EfficiencyBinsSC = cms.PSet(
    probe_et = cms.vdouble(25, 30, 35, 40, 45, 50, 200),
    probe_eta = cms.vdouble(0.0, 0.5, 1.0, 1.5, 2.0, 2.5)
)

#### For data: except for HLT step
EfficiencyBinningSpecification = cms.PSet(
    #specifies what unbinned variables to include in the dataset, the mass is needed for the fit
    UnbinnedVariables = cms.vstring("mass"),
    #specifies the binning of parameters
    BinnedVariables = cms.PSet(EfficiencyBins),
    #first string is the default followed by binRegExp - PDFname pairs
    BinToPDFmap = cms.vstring(PDFName)
)


#### For super clusters
EfficiencyBinningSpecificationSC = cms.PSet(
    UnbinnedVariables = cms.vstring("mass"),
    BinnedVariables = cms.PSet(EfficiencyBinsSC),
    BinToPDFmap = cms.vstring(PDFName)
)
EfficiencyBinningSpecificationSCMC = cms.PSet(
    UnbinnedVariables = cms.vstring("mass"),
    BinnedVariables = cms.PSet(EfficiencyBinsSC,mcTrue = cms.vstring("true")),
    BinToPDFmap = cms.vstring()  
)


#### For MC truth: do truth matching
EfficiencyBinningSpecificationMC = cms.PSet(
    UnbinnedVariables = cms.vstring("mass"),
    BinnedVariables = cms.PSet(
    #probe_et = cms.vdouble( 25, 30, 35, 40, 45, 50, 200 ),
    #probe_eta = cms.vdouble( -2.5, -2.0, -1.5, -1.0, -0.5, 0.0, 0.5, 1.0, 1.5, 2.0, 2.5 ),
    probe_et = cms.vdouble( 25, 200 ),
    probe_eta = cms.vdouble(0, 2.5 ),
    mcTrue = cms.vstring("true")
    ),
    BinToPDFmap = cms.vstring()  
)

#### For HLT step: just do cut & count
EfficiencyBinningSpecificationHLT = cms.PSet(
    UnbinnedVariables = cms.vstring("mass"),
    BinnedVariables = cms.PSet(EfficiencyBins),
    BinToPDFmap = cms.vstring()  
)

##########################################################################################
############################################################################################
if False:#isMC:
    mcTruthModules = cms.PSet(
##         MCtruth_WP95 = cms.PSet(
##         EfficiencyBinningSpecificationMC,
##         EfficiencyCategoryAndState = cms.vstring("probe_isWP95","pass"),
##         ),
        MCtruth_WPTight = cms.PSet(
        EfficiencyBinningSpecificationMC,
        EfficiencyCategoryAndState = cms.vstring("probe_passConvRej","pass","probe_isWPTight","pass"),
        ),
        MCtruth_WPLoose = cms.PSet(
        EfficiencyBinningSpecificationMC,
        EfficiencyCategoryAndState = cms.vstring("probe_passConvRej","pass","probe_isWPLoose","pass"),
        ),
    )
else:
    mcTruthModules = cms.PSet()
##########################################################################################
##########################################################################################


        

############################################################################################
############################################################################################
####### GsfElectron->Id / selection efficiency 
############################################################################################
############################################################################################

process.GsfElectronToId = cms.EDAnalyzer("TagProbeFitTreeAnalyzer",
    # IO parameters:
    InputFileNames = cms.vstring(InputFileName),
    InputDirectoryName = cms.string("GsfElectronToId"),
    InputTreeName = cms.string("fitter_tree"),
    OutputFileName = cms.string(OutputFilePrefix+"GsfElectronToId.root"),
    #numbrer of CPUs to use for fitting
    NumCPU = cms.uint32(16),
    # specifies wether to save the RooWorkspace containing the data for each bin and
    # the pdf object with the initial and final state snapshots
    SaveWorkspace = cms.bool(True),
    floatShapeParameters = cms.bool(True),
    #fixVars = cms.vstring("mean"),

    # defines all the real variables of the probes available in the input tree and intended for use in the efficiencies
    Variables = cms.PSet(
        mass = cms.vstring("Tag-Probe Mass", "60.0", "120.0", "GeV/c^{2}"),
        probe_sc_et = cms.vstring("Probe E_{T}", "0", "1000", "GeV/c"),
        probe_sc_eta = cms.vstring("Probe #eta", "0", "2.5", ""),                
    ),

    # defines all the discrete variables of the probes available in the input tree and intended for use in the efficiency calculations
    Categories = cms.PSet(
        mcTrue = cms.vstring("MC true", "dummy[true=1,false=0]"),
        probe_passConvRej = cms.vstring("probe_passConvRej", "dummy[pass=1,fail=0]"), 
        probe_isWPTight = cms.vstring("probe_isWPTight", "dummy[pass=1,fail=0]"),
        probe_isWPMedium = cms.vstring("probe_isWPMedium", "dummy[pass=1,fail=0]"),
        probe_isWPLoose = cms.vstring("probe_isWPLoose", "dummy[pass=1,fail=0]"),
        probe_isWPNone = cms.vstring("probe_isWPNone", "dummy[pass=1,fail=0]"),
    ),
    # defines all the PDFs that will be available for the efficiency calculations; uses RooFit's "factory" syntax;
    # each pdf needs to define "signal", "backgroundPass", "backgroundFail" pdfs, "efficiency[0.9,0,1]" and "signalFractionInPassing[0.9]" are used for initial values  

    PDFs = cms.PSet(
        pdfSignalPlusBackground = cms.vstring(
#        "gaussPlusLinear", "*pt_bin0*", "gaussPlusQuadratic"
#"""     "CBExGaussShape::signalRes(mass, mean[2.0946e-01], sigma[8.5695e-04],alpha[3.8296e-04], n[6.7489e+00], sigma_2[2.5849e+00], frac[6.5704e-01])",  ### the signal function goes here
#     "CBExGaussShape::signalResPass(mass, meanP[0.], sigmaP[8.5695e-04, 0., 3.],alphaP[3.8296e-04], nP[6.7489e+00], sigmaP_2[2.5849e+00], fracP[6.5704e-01])",  ### signal resolution for "pass" sample
#     "CBExGaussShape::signalResFail(mass, meanF[2.0946e-01, -5., 5.], sigmaF[8.5695e-04, 0., 5.],alphaF[3.8296e-04], nF[6.7489e+00], sigmaF_2[2.5849e+00], fracF[6.5704e-01])",  ### signal resolution for "fail" sample     
#    "ZGeneratorLineShape::signalPhy(mass)", ### NLO line shape
#    "RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], betaPass, peakPass[90.0])",
#    "RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], betaFail, peakFail[90.0])",
#    "FCONV::signalPass(mass, signalPhy, signalResPass)",
#    "FCONV::signalFail(mass, signalPhy, signalResFail)",     
#    "efficiency[0.9,0,1]",
#    "signalFractionInPassing[1.0]"   """
      
    "Gaussian::signal(mass, mean[91.2, 89.0, 93.0], sigma[2.3, 0.5, 10.0])",
    "RooExponential::backgroundPass(mass, cPass[-0.02,-5,0])",
    "RooExponential::backgroundFail(mass, cFail[-0.02,-5,0])",
    "efficiency[0.9,0,1]",
    "signalFractionInPassing[0.9]",
        ),
    ),

    # defines a set of efficiency calculations, what PDF to use for fitting and how to bin the data;
    # there will be a separate output directory for each calculation that includes a simultaneous fit, side band subtraction and counting. 
    Efficiencies = cms.PSet(
        mcTruthModules,
         #the name of the parameter set becomes the name of the directory

         WPTight = cms.PSet(
             EfficiencyBinningSpecification,
             #specifies the efficiency of which category and state to measure 
             EfficiencyCategoryAndState = cms.vstring("probe_isWPTight","pass"),
         ),
         WPMedium = cms.PSet(
             EfficiencyBinningSpecification,
             EfficiencyCategoryAndState = cms.vstring("probe_isWPMedium","pass"),
         ),
         WPLoose = cms.PSet(
             EfficiencyBinningSpecification,
             EfficiencyCategoryAndState = cms.vstring("probe_isWPLoose","pass"),
         ),
         WPNone = cms.PSet(
             EfficiencyBinningSpecification,
             EfficiencyCategoryAndState = cms.vstring("probe_isWPNone","pass"),
         ),

############################################################################################
############################################################################################
    )
)


############################################################################################
############################################################################################
####### SC->GsfElectron efficiency 
############################################################################################
############################################################################################
if False:#isMC:
    SCmcTruthModules = cms.PSet(
        MCtruth_efficiency = cms.PSet(
        EfficiencyBinningSpecificationSCMC,
        EfficiencyCategoryAndState = cms.vstring( "probe_passingGsf", "pass" ),
        ),
    )
else:
    SCmcTruthModules = cms.PSet()    


process.SCToGsfElectron = process.GsfElectronToId.clone()
process.SCToGsfElectron.InputDirectoryName = cms.string("SuperClusterToGsfElectron")
process.SCToGsfElectron.OutputFileName = cms.string(OutputFilePrefix+"SCToGsfElectron.root")
process.SCToGsfElectron.Variables = cms.PSet(
        mass = cms.vstring("Tag-Probe Mass", "60.0", "120.0", "GeV/c^{2}"),
        probe_et = cms.vstring("Probe E_{T}", "0", "1000", "GeV/c"),
        probe_eta = cms.vstring("Probe #eta", "0", "2.5", ""),                
    )
process.SCToGsfElectron.Categories = cms.PSet(
    mcTrue = cms.vstring("MC true", "dummy[true=1,false=0]"),           
    probe_passingGsf = cms.vstring("probe_passingGsf", "dummy[pass=1,fail=0]"),                        
    )
process.SCToGsfElectron.Efficiencies = cms.PSet(
    SCmcTruthModules,
    efficiency = cms.PSet(
        EfficiencyBinningSpecificationSC,
        EfficiencyCategoryAndState = cms.vstring( "probe_passingGsf", "pass" ),
    ),
)

############################################################################################
############################################################################################
####### HLT efficiency 
############################################################################################
############################################################################################


if isMC:
    HLTmcTruthModules = cms.PSet(
        MCtruth_efficiency = cms.PSet(
        EfficiencyBinningSpecificationMC,
        EfficiencyCategoryAndState = cms.vstring( HLTDef, "pass" ),
        ),    
    )
else:
    HLTmcTruthModules = cms.PSet()


EfficienciesPset = cms.PSet(
    HLTmcTruthModules,
    efficiency = cms.PSet(
        #EfficiencyBinningSpecificationHLT,
        EfficiencyBinningSpecification,
        EfficiencyCategoryAndState = cms.vstring( HLTDef, "pass" ),
    ),
)

########
process.WPTightToHLT = process.GsfElectronToId.clone()
process.WPTightToHLT.InputDirectoryName = cms.string("WPTightToHLT")
#process.WPTightToHLT.InputDirectoryName = cms.string("GsfElectronToId")
process.WPTightToHLT.OutputFileName = cms.string(OutputFilePrefix+"WPTightToHLT.root")
process.WPTightToHLT.Categories = cms.PSet(
    mcTrue = cms.vstring("MC true", "dummy[true=1,false=0]"),           
    #probe_passingHLT = cms.vstring("probe_passingHLT", "dummy[pass=1,fail=0]"), 
    probe_passingHLT = cms.vstring("probe_passingHLT", "dummy[pass=1,fail=0]"), 
    )
process.WPTightToHLT.Efficiencies = EfficienciesPset

process.WPMediumToHLT = process.WPTightToHLT.clone()
process.WPMediumToHLT.InputDirectoryName = cms.string("WPMediumToHLT")
process.WPMediumToHLT.OutputFileName = cms.string(OutputFilePrefix+"WPMediumToHLT.root")

process.WPLooseToHLT = process.WPTightToHLT.clone()
process.WPLooseToHLT.InputDirectoryName = cms.string("WPLooseToHLT")
process.WPLooseToHLT.OutputFileName = cms.string(OutputFilePrefix+"WPLooseToHLT.root")

process.WPNoneToHLT = process.WPTightToHLT.clone()
process.WPNoneToHLT.InputDirectoryName = cms.string("WPNoneToHLT")
process.WPNoneToHLT.OutputFileName = cms.string(OutputFilePrefix+"WPNoneToHLT.root")


process.fit = cms.Path(
    process.GsfElectronToId
    + process.SCToGsfElectron
    + process.WPTightToHLT
    + process.WPMediumToHLT
    + process.WPLooseToHLT
    + process.WPNoneToHLT
    )
