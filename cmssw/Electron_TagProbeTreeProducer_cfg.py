## /*****************************************************************************
##  * Project: CMS detector at the CERN
##  *
##  * Package: PhysicsTools/TagAndProbe
##  *
##  *
##  * Authors:
##  *
##  *   Kalanand Mishra, Fermilab - kalanand@fnal.gov
##  *
##  * Description:
##  *   - Produces tag & probe TTree for further analysis and computing efficiency
##  *
##  * History:
##  *   
##  *
##  * Copyright (C) 2010 FNAL 
##  *****************************************************************************/


import FWCore.ParameterSet.Config as cms

##                      _              _       
##   ___ ___  _ __  ___| |_ __ _ _ __ | |_ ___ 
##  / __/ _ \| '_ \/ __| __/ _` | '_ \| __/ __|
## | (_| (_) | | | \__ \ || (_| | | | | |_\__ \
##  \___\___/|_| |_|___/\__\__,_|_| |_|\__|___/
##                                              
################################################


MC_flag = False

HLTPath = "HLT_Ele17_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_Ele8_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v"
HLTPath += "17" if MC_flag else "18"
HLTProcessName = "HLT"
if MC_flag:
    GLOBAL_TAG = 'START53_V27::All'
else:
	GLOBAL_TAG = 'FT53_V21A_AN6::All'

OUTPUT_FILE_NAME = "tnp_{0}.root".format('mc' if MC_flag else 'data')


ELECTRON_ET_CUT_MIN = 17.0
ELECTRON_COLL = "gsfElectrons"
#ELECTRON_CUTS = "ecalDrivenSeed==1 && (abs(superCluster.eta)<2.5) && !(1.4442<abs(superCluster.eta)<1.566) && (ecalEnergy*sin(superClusterPosition.theta)>" + str(ELECTRON_ET_CUT_MIN) + ")"
ELECTRON_CUTS = "!(1.4442<abs(superCluster.eta)<1.566)"
####

PHOTON_COLL = "photons"
PHOTON_CUTS = "hadronicOverEm<0.15 && (abs(superCluster.eta)<2.5) && !(1.4442<abs(superCluster.eta)<1.566) && ((isEB && sigmaIetaIeta<0.01) || (isEE && sigmaIetaIeta<0.03)) && (superCluster.energy*sin(superCluster.position.theta)>" + str(ELECTRON_ET_CUT_MIN) + ")"
####

#SUPERCLUSTER_COLL_EB = "hybridSuperClusters"
#SUPERCLUSTER_COLL_EE = "multi5x5SuperClustersWithPreshower"
#if MC_flag:
SUPERCLUSTER_COLL_EB = "correctedHybridSuperClusters"
SUPERCLUSTER_COLL_EE = "correctedMulti5x5SuperClustersWithPreshower"

SUPERCLUSTER_CUTS = "abs(eta)<2.5 && !(1.4442< abs(eta) <1.566) && et>" + str(ELECTRON_ET_CUT_MIN)


JET_COLL = "ak5PFJets"
JET_CUTS = "abs(eta)<2.6 && chargedHadronEnergyFraction>0 && electronEnergyFraction<0.1 && nConstituents>1 && neutralHadronEnergyFraction<0.99 && neutralEmEnergyFraction<0.99" 
########################

##    ___            _           _      
##   |_ _|_ __   ___| |_   _  __| | ___ 
##    | || '_ \ / __| | | | |/ _` |/ _ \
##    | || | | | (__| | |_| | (_| |  __/
##   |___|_| |_|\___|_|\__,_|\__,_|\___|
##
process = cms.Process("TagProbe")
process.load("Configuration.Geometry.GeometryIdeal_cff")
process.load("Configuration.StandardSequences.MagneticField_cff")
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
from Configuration.AlCa.autoCond import autoCond
process.GlobalTag.globaltag = GLOBAL_TAG
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load("SimGeneral.HepPDTESSource.pythiapdt_cfi")
#process.options   = cms.untracked.PSet( wantSummary = cms.untracked.bool(True) )
process.MessageLogger.cerr.FwkReport.reportEvery = 1000

##   ____             _ ____                           
##  |  _ \ ___   ___ | / ___|  ___  _   _ _ __ ___ ___ 
##  | |_) / _ \ / _ \| \___ \ / _ \| | | | '__/ __/ _ \
##  |  __/ (_) | (_) | |___) | (_) | |_| | | | (_|  __/
##  |_|   \___/ \___/|_|____/ \___/ \__,_|_|  \___\___|
##  
if MC_flag:
	process.source = cms.Source("PoolSource", 
		fileNames = cms.untracked.vstring(
			'file:/pnfs/desy.de/cms/tier2/store/mc/Summer12_DR53X/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball/AODSIM/PU_S10_START53_V7A-v1/0000/00037C53-AAD1-E111-B1BE-003048D45F38.root',
			'file:/pnfs/desy.de/cms/tier2/store/mc/Summer12_DR53X/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball/AODSIM/PU_S10_START53_V7A-v1/0000/00050BBE-D5D2-E111-BB65-001E67398534.root',
			'file:/pnfs/desy.de/cms/tier2/store/mc/Summer12_DR53X/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball/AODSIM/PU_S10_START53_V7A-v1/0000/00B16DF1-8FD1-E111-ADBB-F04DA23BCE4C.root',
			'file:/pnfs/desy.de/cms/tier2/store/mc/Summer12_DR53X/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball/AODSIM/PU_S10_START53_V7A-v1/0000/00D370C2-E3D2-E111-9C87-003048673F0A.root',
			'file:/pnfs/desy.de/cms/tier2/store/mc/Summer12_DR53X/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball/AODSIM/PU_S10_START53_V7A-v1/0000/00FB6563-58D2-E111-AFCB-001E67397D73.root',
			'file:/pnfs/desy.de/cms/tier2/store/mc/Summer12_DR53X/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball/AODSIM/PU_S10_START53_V7A-v1/0000/023889B1-3ED2-E111-B9A4-00304866C51E.root',
			'file:/pnfs/desy.de/cms/tier2/store/mc/Summer12_DR53X/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball/AODSIM/PU_S10_START53_V7A-v1/0000/026E25E5-65D2-E111-8481-00304867406E.root',
			'file:/pnfs/desy.de/cms/tier2/store/mc/Summer12_DR53X/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball/AODSIM/PU_S10_START53_V7A-v1/0000/02A03572-32D2-E111-A90C-001E67397314.root',
			'file:/pnfs/desy.de/cms/tier2//store/mc/Summer12_DR53X/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball/AODSIM/PU_S10_START53_V7A-v1/0000/02B0AB2A-ADD2-E111-8F7F-001E67397D7D.root',
			#'file:/pnfs/desy.de/cms/tier2/',
		)
	)
else:
	process.source = cms.Source("PoolSource", 
		fileNames = cms.untracked.vstring(
			'file:/pnfs/desy.de/cms/tier2/store/data/Run2012C/DoubleElectron/AOD/22Jan2013-v1/20002/0064F752-AF68-E211-B9C1-002618943898.root',
			'file:/pnfs/desy.de/cms/tier2/store/data/Run2012C/DoubleElectron/AOD/22Jan2013-v1/20002/0270AC35-C368-E211-BAEA-003048679070.root',
			'file:/pnfs/desy.de/cms/tier2/store/data/Run2012C/DoubleElectron/AOD/22Jan2013-v1/20002/0278C3AA-D968-E211-85C8-00304867916E.root',
			'file:/pnfs/desy.de/cms/tier2/store/data/Run2012C/DoubleElectron/AOD/22Jan2013-v1/20002/0294C846-B06B-E211-9C01-003048678B44.root',
			'file:/pnfs/desy.de/cms/tier2/store/data/Run2012C/DoubleElectron/AOD/22Jan2013-v1/20002/02D20766-E369-E211-B4AA-002618943876.root',
			'file:/pnfs/desy.de/cms/tier2/store/data/Run2012C/DoubleElectron/AOD/22Jan2013-v1/20002/046395B3-B268-E211-9707-002618943880.root',
			'file:/pnfs/desy.de/cms/tier2/store/data/Run2012C/DoubleElectron/AOD/22Jan2013-v1/20002/0636CFBA-D868-E211-B73A-0030486790B8.root',
			'file:/pnfs/desy.de/cms/tier2/store/data/Run2012C/DoubleElectron/AOD/22Jan2013-v1/20002/08C21A03-B268-E211-B5F3-00261894398C.root',
			'file:/pnfs/desy.de/cms/tier2/store/data/Run2012C/DoubleElectron/AOD/22Jan2013-v1/20002/08E73A5D-BD68-E211-9496-003048679070.root',
			'file:/pnfs/desy.de/cms/tier2/store/data/Run2012C/DoubleElectron/AOD/22Jan2013-v1/20002/0AC24B13-BA68-E211-8B9F-002618943902.root',
		)
	)
# Trigger in data:
######## DST_Ele8_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL_HT250_v4
######## HLT_CleanPFNoPUHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45_v2
######## HLT_CleanPFNoPUHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50_v2
######## HLT_CleanPFNoPUHT300_Ele40_CaloIdVT_TrkIdT_v2
######## HLT_CleanPFNoPUHT300_Ele60_CaloIdVT_TrkIdT_v2
######## HLT_CleanPFNoPUHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45_v2
######## HLT_CleanPFNoPUHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50_v2
######## HLT_DoubleEle10_CaloIdL_TrkIdVL_Ele10_CaloIdT_TrkIdVL_v12
######## HLT_DoubleEle14_CaloIdT_TrkIdVL_Mass8_PFMET40_v7
######## HLT_DoubleEle14_CaloIdT_TrkIdVL_Mass8_PFMET50_v7
######## HLT_DoubleEle33_CaloIdL_GsfTrkIdVL_v7
######## HLT_DoubleEle33_CaloIdL_v14
######## HLT_DoubleEle33_CaloIdT_v10
######## HLT_DoubleEle8_CaloIdT_TrkIdVL_Mass8_PFNoPUHT175_v3
######## HLT_DoubleEle8_CaloIdT_TrkIdVL_Mass8_PFNoPUHT225_v3
######## HLT_DoubleEle8_CaloIdT_TrkIdVL_v12
######## HLT_DoubleMu5_Ele8_CaloIdT_TrkIdVL_v16
######## HLT_DoubleMu8_Ele8_CaloIdT_TrkIdVL_v5
######## HLT_Ele12_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_DoubleCentralJet65_v4
######## HLT_Ele12_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_RsqMR30_Rsq0p04_MR200_v4
######## HLT_Ele12_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_RsqMR40_Rsq0p04_MR200_v4
######## HLT_Ele15_Ele8_Ele5_CaloIdL_TrkIdVL_v6
######## HLT_Ele17_CaloIdL_CaloIsoVL_v17
######## HLT_Ele17_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_Ele8_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v18
######## HLT_Ele17_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_Jet30_v7
######## HLT_Ele17_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v6
######## HLT_Ele17_CaloIdVT_CaloIsoVT_TrkIdT_TrkIsoVT_Ele8_Mass50_v6
######## HLT_Ele20_CaloIdVT_CaloIsoVT_TrkIdT_TrkIsoVT_SC4_Mass50_v6
######## HLT_Ele22_CaloIdL_CaloIsoVL_v6
######## HLT_Ele22_eta2p1_WP90NoIso_LooseIsoPFTau20_v6
######## HLT_Ele22_eta2p1_WP90Rho_LooseIsoPFTau20_v6
######## HLT_Ele23_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_HFT30_v7
######## HLT_Ele25_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_CentralPFNoPUJet30_BTagIPIter_v8
######## HLT_Ele25_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_CentralPFNoPUJet30_v7
######## HLT_Ele25_CaloIdVT_CaloIsoVL_TrkIdVL_TrkIsoT_DiCentralPFNoPUJet30_v1
######## HLT_Ele25_CaloIdVT_CaloIsoVL_TrkIdVL_TrkIsoT_TriCentralPFNoPUJet30_v3
######## HLT_Ele25_CaloIdVT_CaloIsoVL_TrkIdVL_TrkIsoT_TriCentralPFNoPUJet45_35_25_v1
######## HLT_Ele25_CaloIdVT_CaloIsoVL_TrkIdVL_TrkIsoT_TriCentralPFNoPUJet50_40_30_v3
######## HLT_Ele27_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL_v11
######## HLT_Ele27_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_Ele15_CaloIdT_CaloIsoVL_trackless_v7
######## HLT_Ele27_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_HFT15_v7
######## HLT_Ele27_WP80_CentralPFJet80_v8
######## HLT_Ele27_WP80_PFMET_MT50_v6
######## HLT_Ele27_WP80_v11
######## HLT_Ele27_WP80_WCandPt80_v8
######## HLT_Ele30_CaloIdVT_TrkIdT_PFNoPUJet100_PFNoPUJet25_v7
######## HLT_Ele30_CaloIdVT_TrkIdT_PFNoPUJet150_PFNoPUJet25_v7
######## HLT_Ele30_CaloIdVT_TrkIdT_v6
######## HLT_Ele32_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL_v11
######## HLT_Ele32_CaloIdT_CaloIsoT_TrkIdT_TrkIsoT_SC17_Mass50_v6
######## HLT_Ele32_WP80_CentralPFJet35_CentralPFJet25_PFMET20_v3
######## HLT_Ele32_WP80_CentralPFJet35_CentralPFJet25_v3
######## HLT_Ele32_WP80_PFJet30_PFJet25_Deta3_CentralPFJet30_v3
######## HLT_Ele32_WP80_PFJet30_PFJet25_Deta3_v3
######## HLT_Ele5_SC5_Jpsi_Mass2to15_v4
######## HLT_Ele80_CaloIdVT_GsfTrkIdT_v2
######## HLT_Ele8_CaloIdL_CaloIsoVL_v17
######## HLT_Ele8_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_Jet30_v7
######## HLT_Ele8_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v15
######## HLT_Ele8_CaloIdT_TrkIdT_DiJet30_v18
######## HLT_Ele8_CaloIdT_TrkIdT_QuadJet30_v18
######## HLT_Ele8_CaloIdT_TrkIdT_TriJet30_v18
######## HLT_Ele8_CaloIdT_TrkIdVL_EG7_v2
######## HLT_Ele8_CaloIdT_TrkIdVL_Jet30_v7
######## HLT_Ele8_CaloIdT_TrkIdVL_v5
######## HLT_Ele90_CaloIdVT_GsfTrkIdT_v2
######## HLT_Mu14_Ele14_CaloIdT_TrkIdVL_Mass8_PFMET40_v7
######## HLT_Mu14_Ele14_CaloIdT_TrkIdVL_Mass8_PFMET50_v7
######## HLT_Mu17_Ele8_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v9
######## HLT_Mu30_Ele30_CaloIdL_v8
######## HLT_Mu7_Ele7_CaloIdT_CaloIsoVL_v7
######## HLT_Mu8_DoubleEle8_CaloIdT_TrkIdVL_v7
######## HLT_Mu8_Ele17_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v9
######## HLT_Mu8_Ele8_CaloIdT_TrkIdVL_Ele8_CaloIdL_TrkIdVL_v7
######## HLT_Mu8_Ele8_CaloIdT_TrkIdVL_Mass8_PFNoPUHT175_v3
######## HLT_Mu8_Ele8_CaloIdT_TrkIdVL_Mass8_PFNoPUHT225_v3
######## HLT_RelIso1p0Mu5_Ele8_CaloIdT_TrkIdVL_Mass8_PFNoPUHT175_v3
######## HLT_RelIso1p0Mu5_Ele8_CaloIdT_TrkIdVL_Mass8_PFNoPUHT225_v3
######## HLT_TripleEle10_CaloIdL_TrkIdVL_v18

process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(-1))
process.source.inputCommands = cms.untracked.vstring("keep *","drop *_MEtoEDMConverter_*_*")

##   ____                         ____ _           _            
##  / ___| _   _ _ __   ___ _ __ / ___| |_   _ ___| |_ ___ _ __ 
##  \___ \| | | | '_ \ / _ \ '__| |   | | | | / __| __/ _ \ '__|
##   ___) | |_| | |_) |  __/ |  | |___| | |_| \__ \ ||  __/ |   
##  |____/ \__,_| .__/ \___|_|   \____|_|\__,_|___/\__\___|_|   
##  

#  SuperClusters  ################
process.superClusters = cms.EDProducer("SuperClusterMerger",
   src = cms.VInputTag(cms.InputTag( SUPERCLUSTER_COLL_EB ,"", "RECO"),
                       cms.InputTag( SUPERCLUSTER_COLL_EE ,"", "RECO") )  
)

process.superClusterCands = cms.EDProducer("ConcreteEcalCandidateProducer",
   src = cms.InputTag("superClusters"),
   particleType = cms.int32(11),
)

#   Get the above SC's Candidates and place a cut on their Et and eta
process.goodSuperClusters = cms.EDFilter("CandViewSelector",
      src = cms.InputTag("superClusterCands"),
      cut = cms.string( SUPERCLUSTER_CUTS ),
      filter = cms.bool(True)
)


#### remove real jets (with high hadronic energy fraction) from SC collection
##### this improves the purity of the probe sample without affecting efficiency

process.JetsToRemoveFromSuperCluster = cms.EDFilter("CaloJetSelector",   
    src = cms.InputTag("ak5CaloJets"),
    cut = cms.string('pt>5 && energyFractionHadronic > 0.15')
)
process.goodSuperClustersClean = cms.EDProducer("CandViewCleaner",
    srcObject = cms.InputTag("goodSuperClusters"),
    module_label = cms.string(''),
    srcObjectsToRemove = cms.VInputTag(cms.InputTag("JetsToRemoveFromSuperCluster")),
    deltaRMin = cms.double(0.1)
)

#  Photons!!! ################ 
process.goodPhotons = cms.EDFilter(
    "PhotonSelector",
    src = cms.InputTag( PHOTON_COLL ),
    cut = cms.string(PHOTON_CUTS)
    )


process.sc_sequence = cms.Sequence(
    process.superClusters +
    process.superClusterCands +
    process.goodSuperClusters +
    process.JetsToRemoveFromSuperCluster +
    process.goodSuperClustersClean +
    process.goodPhotons
    )


##    ____      __ _____ _           _                   
##   / ___|___ / _| ____| | ___  ___| |_ _ __ ___  _ __  
##  | |  _/ __| |_|  _| | |/ _ \/ __| __| '__/ _ \| '_ \ 
##  | |_| \__ \  _| |___| |  __/ (__| |_| | | (_) | | | |
##   \____|___/_| |_____|_|\___|\___|\__|_|  \___/|_| |_|
##  

process.load('TrackingTools.TransientTrack.TransientTrackBuilder_cfi')
process.load('PhysicsTools.PatAlgos.producersLayer1.electronProducer_cfi')
process.patElectrons.electronIDSources = cms.PSet(
	## default cut based Id
	eidRobustLoose      = cms.InputTag("eidRobustLoose"     ),
	eidRobustTight      = cms.InputTag("eidRobustTight"     ),
	eidLoose            = cms.InputTag("eidLoose"           ),
	eidTight            = cms.InputTag("eidTight"           ),
	eidRobustHighEnergy = cms.InputTag("eidRobustHighEnergy"),
)
process.patElectrons.genParticleMatch = ""
process.patElectrons.addGenMatch = False
process.patElectrons.embedGenMatch = False
process.patElectrons.embedGsfElectronCore          = True
process.patElectrons.embedGsfTrack                 = True
process.patElectrons.embedSuperCluster             = True
process.patElectrons.embedPflowSuperCluster        = True
process.patElectrons.embedSeedCluster              = True
process.patElectrons.embedBasicClusters            = True
process.patElectrons.embedPreshowerClusters        = True
process.patElectrons.embedPflowBasicClusters       = True
process.patElectrons.embedPflowPreshowerClusters   = True
process.patElectrons.embedPFCandidate              = True
process.patElectrons.embedTrack                    = True
process.patElectrons.embedRecHits                  = True

process.patElectrons.embedHighLevelSelection.pvSrc = "goodOfflinePrimaryVertices"


## CALIBRATIONS
# momentum corrections
process.load('EgammaAnalysis.ElectronTools.electronRegressionEnergyProducer_cfi')
process.eleRegressionEnergy.inputElectronsTag = cms.InputTag('patElectrons')
process.eleRegressionEnergy.inputCollectionType = cms.uint32(1)

process.load("Configuration.StandardSequences.Services_cff")
process.RandomNumberGeneratorService = cms.Service("RandomNumberGeneratorService",
		calibratedPatElectrons = cms.PSet(
			initialSeed = cms.untracked.uint32(1),
			engineName = cms.untracked.string('TRandom3')
		),
)

# calibrate pat electrons
process.load("EgammaAnalysis.ElectronTools.calibratedPatElectrons_cfi")
if not MC_flag:
	inputDataset =  "22Jan2013ReReco"
else:
	#inputDataset =  "Summer12_DR53X_HCP2012"
	inputDataset =  "Summer12_LegacyPaper"
print "Using electron calibration", inputDataset
process.calibratedPatElectrons.inputDataset = cms.string(inputDataset)
process.calibratedPatElectrons.isMC = cms.bool(MC_flag)

##  electron iso for cutbased ID
from CommonTools.ParticleFlow.Tools.pfIsolation import setupPFElectronIso
process.eleIsoSequence = setupPFElectronIso(process, 'patElectrons')
process.calibeleIsoSequence = setupPFElectronIso(process, 'calibratedPatElectrons', "PFIsoCal")

for size in ["3", "4"]:
	for typ in ["calib", ""]:
		getattr(process, typ+"eleIsoSequence").remove(getattr(process, "elPFIsoValueCharged0{0}NoPFIdPFIso".format(size) ))
		getattr(process, typ+"eleIsoSequence").remove(getattr(process, "elPFIsoValueChargedAll0{0}NoPFIdPFIso".format(size)))
		getattr(process, typ+"eleIsoSequence").remove(getattr(process, "elPFIsoValueGamma0{0}NoPFIdPFIso".format(size)))
		getattr(process, typ+"eleIsoSequence").remove(getattr(process, "elPFIsoValueNeutral0{0}NoPFIdPFIso".format(size)))
		getattr(process, typ+"eleIsoSequence").remove(getattr(process, "elPFIsoValuePU0{0}NoPFIdPFIso".format(size)))

	getattr(process, "elPFIsoValueGamma0{0}PFIdPFIso".format(size)).deposits[0].vetos      = cms.vstring('EcalEndcaps:ConeVeto(0.08)','EcalBarrel:ConeVeto(0.08)')
	getattr(process, "elPFIsoValueNeutral0{0}PFIdPFIso".format(size)).deposits[0].vetos    = cms.vstring()
	getattr(process, "elPFIsoValuePU0{0}PFIdPFIso".format(size)).deposits[0].vetos         = cms.vstring()
	getattr(process, "elPFIsoValueCharged0{0}PFIdPFIso".format(size)).deposits[0].vetos    = cms.vstring('EcalEndcaps:ConeVeto(0.015)')
	getattr(process, "elPFIsoValueChargedAll0{0}PFIdPFIso".format(size)).deposits[0].vetos = cms.vstring('EcalEndcaps:ConeVeto(0.015)','EcalBarrel:ConeVeto(0.01)')

process.pfiso = cms.Sequence(process.pfParticleSelectionSequence + process.eleIsoSequence + process.calibeleIsoSequence)

# rho for e isolation
from RecoJets.JetProducers.kt4PFJets_cfi import kt4PFJets
process.kt6PFJetsForIsolation = kt4PFJets.clone( rParam = 0.6, doRhoFastjet = True )
process.kt6PFJetsForIsolation.Rho_EtaMax = cms.double(2.5)

#ELECTRON_COLL = "patElectrons"




#  GsfElectron ################ 
process.goodElectrons = cms.EDFilter("GsfElectronRefSelector",
    src = cms.InputTag( ELECTRON_COLL ),
    cut = cms.string( ELECTRON_CUTS )    
)

process.GsfMatchedSuperClusterCands = cms.EDProducer("ElectronMatchedCandidateProducer",
   src     = cms.InputTag("goodSuperClustersClean"),
   ReferenceElectronCollection = cms.untracked.InputTag("goodElectrons"),
   deltaR =  cms.untracked.double(0.3)
)

process.GsfMatchedPhotonCands = process.GsfMatchedSuperClusterCands.clone()
process.GsfMatchedPhotonCands.src = cms.InputTag("goodPhotons")

            

##    _____ _           _                     ___    _ 
##   | ____| | ___  ___| |_ _ __ ___  _ __   |_ _|__| |
##   |  _| | |/ _ \/ __| __| '__/ _ \| '_ \   | |/ _` |
##   | |___| |  __/ (__| |_| | | (_) | | | |  | | (_| |
##   |_____|_|\___|\___|\__|_|  \___/|_| |_| |___\__,_|
##   
# Electron ID  ######
cutstring = (" \
&& (gsfTrack.trackerExpectedHitsInner.numberOfHits <= {missingHits}) \
&& ((isEB \
&& (-{dEtaIN_EB}<deltaEtaSuperClusterTrackAtVtx<{dEtaIN_EB}) \
&& (-{dPhiIN_EB}<deltaPhiSuperClusterTrackAtVtx<{dPhiIN_EB}) \
&& (sigmaIetaIeta<{sigmaIetaIeta_EB}) \
&& (hadronicOverEm<{hadronicOverEm_EB})"+
#&& (-{d0_EB} < gsfTrack.dxy < {d0_EB}) \
#&& (-{dZ_EB} < gsfTrack.dz < {dZ_EB}) \
"&& (-{Ep_EB} < ( (1./ecalEnergy) - (eSuperClusterOverP/ecalEnergy) ) < {Ep_EB}) \
) \
|| (isEE \
&& (-{dEtaIN_EE}<deltaEtaSuperClusterTrackAtVtx<{dEtaIN_EE}) \
&& (-{dPhiIN_EE}<deltaPhiSuperClusterTrackAtVtx<{dPhiIN_EE}) \
&& (sigmaIetaIeta<{sigmaIetaIeta_EE}) \
&& (hadronicOverEm<{hadronicOverEm_EE})"+
#&& (-{d0_EE} < gsfTrack.dxy < {d0_EE}) \
#&& (-{dZ_EE} < gsfTrack.dz < {dZ_EE}) \
"&& (-{Ep_EE} < ( (1./ecalEnergy) - (eSuperClusterOverP/ecalEnergy) ) < {Ep_EE}) \
))")


cutstring_tight=cutstring.format(
     missingHits=0,

     dEtaIN_EB=0.004,
     dPhiIN_EB=0.03,
     sigmaIetaIeta_EB=0.01,
     hadronicOverEm_EB=0.12,
     #d0_EB=0.02,
     #dZ_EB=0.1,
     Ep_EB=0.05,

     dEtaIN_EE=0.005,
     dPhiIN_EE=0.02,
     sigmaIetaIeta_EE=0.03,
     hadronicOverEm_EE=0.10,
     #d0_EE=0.02,
     #dZ_EE=0.1,
     Ep_EE=0.05,
)

cutstring_medium=cutstring.format(
     missingHits=1,

     dEtaIN_EB=0.004,
     dPhiIN_EB=0.06,
     sigmaIetaIeta_EB=0.01,
     hadronicOverEm_EB=0.12,
     #d0_EB=0.02,
     #dZ_EB=0.1,
     Ep_EB=0.05,

     dEtaIN_EE=0.007,
     dPhiIN_EE=0.03,
     sigmaIetaIeta_EE=0.03,
     hadronicOverEm_EE=0.10,
     #d0_EE=0.02,
     #dZ_EE=0.1,
     Ep_EE=0.05
)

cutstring_loose=cutstring.format(
     missingHits=1,

     dEtaIN_EB=0.007,
     dPhiIN_EB=0.15,
     sigmaIetaIeta_EB=0.01,
     hadronicOverEm_EB=0.12,
     #d0_EB=0.02,
     #dZ_EB=0.2,
     Ep_EB=0.05,

     dEtaIN_EE=0.009,
     dPhiIN_EE=0.1,
     sigmaIetaIeta_EE=0.03,
     hadronicOverEm_EE=0.10,
     #d0_EE=0.02,
     #dZ_EE=0.2,
     Ep_EE=0.05,
)

print "tight cuts:", cutstring_tight
process.PassingWPTight = process.goodElectrons.clone()
process.PassingWPTight.cut = cms.string(
    process.goodElectrons.cut.value() + cutstring_tight)

process.PassingWPMedium = process.goodElectrons.clone()
process.PassingWPMedium.cut = cms.string(
    process.goodElectrons.cut.value() + cutstring_medium)

process.PassingWPLoose = process.goodElectrons.clone()
process.PassingWPLoose.cut = cms.string(
    process.goodElectrons.cut.value() + cutstring_loose)

process.PassingWPNone = process.goodElectrons.clone()
process.PassingWPNone.cut = cms.string(
    process.goodElectrons.cut.value())


##     ____ _  ____ 
##    / ___(_)/ ___|
##   | |   | | |    
##   | |___| | |___ 
##    \____|_|\____|
##   
process.load("RecoEgamma.ElectronIdentification.cutsInCategoriesElectronIdentificationV06_DataTuning_cfi")
process.load("RecoEgamma.ElectronIdentification.electronIdLikelihoodExt_cfi")

process.eIDSequence = cms.Sequence(
    process.eidVeryLoose+ 
    process.eidLoose+                
    process.eidMedium+
    process.eidTight+
    process.eidSuperTight+
    process.eidLikelihoodExt 
    )


# select a subset of the GsfElectron collection based on the quality stored in a ValueMap
process.PassingCicVeryLoose = cms.EDProducer("BtagGsfElectronSelector",
   input     = cms.InputTag( ELECTRON_COLL ),
   selection = cms.InputTag('eidVeryLoose'),
   cut       = cms.double(14.5) ### 15== passing all iso,id,tip cuts
)
process.PassingCicLoose = process.PassingCicVeryLoose.clone()
process.PassingCicLoose.selection = cms.InputTag('eidLoose')
process.PassingCicMedium = process.PassingCicVeryLoose.clone()
process.PassingCicMedium.selection = cms.InputTag('eidMedium')
process.PassingCicTight = process.PassingCicVeryLoose.clone()
process.PassingCicTight.selection = cms.InputTag('eidTight')
process.PassingCicSuperTight = process.PassingCicVeryLoose.clone()
process.PassingCicSuperTight.selection = cms.InputTag('eidSuperTight')

                         
##    _____     _                         __  __       _       _     _             
##   |_   _| __(_) __ _  __ _  ___ _ __  |  \/  | __ _| |_ ___| |__ (_)_ __   __ _ 
##     | || '__| |/ _` |/ _` |/ _ \ '__| | |\/| |/ _` | __/ __| '_ \| | '_ \ / _` |
##     | || |  | | (_| | (_| |  __/ |    | |  | | (_| | || (__| | | | | | | | (_| |
##     |_||_|  |_|\__, |\__, |\___|_|    |_|  |_|\__,_|\__\___|_| |_|_|_| |_|\__, |
##                |___/ |___/                                                |___/ 
##   
# Trigger  ##################
process.PassingHLT = cms.EDProducer("trgMatchedGsfElectronProducer",    
    InputProducer = cms.InputTag( ELECTRON_COLL ),                          
    hltTags = cms.VInputTag(cms.InputTag(HLTPath,"", HLTProcessName)),
    triggerEventTag = cms.untracked.InputTag("hltTriggerSummaryAOD","",HLTProcessName),
    triggerResultsTag = cms.untracked.InputTag("TriggerResults","",HLTProcessName)   
)


##    _____      _                        _  __     __             
##   | ____|_  _| |_ ___ _ __ _ __   __ _| | \ \   / /_ _ _ __ ___ 
##   |  _| \ \/ / __/ _ \ '__| '_ \ / _` | |  \ \ / / _` | '__/ __|
##   | |___ >  <| ||  __/ |  | | | | (_| | |   \ V / (_| | |  \__ \
##   |_____/_/\_\\__\___|_|  |_| |_|\__,_|_|    \_/ \__,_|_|  |___/
##   
## Here we show how to use a module to compute an external variable
## process.load("JetMETCorrections.Configuration.DefaultJEC_cff")
## ak5PFResidual.useCondDB = False

process.superClusterDRToNearestJet = cms.EDProducer("DeltaRNearestJetComputer",
    probes = cms.InputTag("goodSuperClusters"),
       # ^^--- NOTA BENE: if probes are defined by ref, as in this case, 
       #       this must be the full collection, not the subset by refs.
    objects = cms.InputTag(JET_COLL),
    objectSelection = cms.string(JET_CUTS + " && pt > 20.0"),
)
process.JetMultiplicityInSCEvents = cms.EDProducer("CandMultiplicityCounter",
    probes = cms.InputTag("goodSuperClusters"),
    objects = cms.InputTag(JET_COLL),
    objectSelection = cms.string(JET_CUTS + " && pt > 20.0"),
)
process.SCConvRejVars = cms.EDProducer("ElectronConversionRejectionVars",
    probes = cms.InputTag("goodSuperClusters")
)
process.GsfConvRejVars = process.SCConvRejVars.clone()
process.GsfConvRejVars.probes = cms.InputTag( ELECTRON_COLL )
process.PhotonDRToNearestJet = process.superClusterDRToNearestJet.clone()
process.PhotonDRToNearestJet.probes =cms.InputTag("goodPhotons")
process.JetMultiplicityInPhotonEvents = process.JetMultiplicityInSCEvents.clone()
process.JetMultiplicityInPhotonEvents.probes = cms.InputTag("goodPhotons")
process.PhotonConvRejVars = process.SCConvRejVars.clone()
process.PhotonConvRejVars.probes = cms.InputTag("goodPhotons")

process.GsfDRToNearestJet = process.superClusterDRToNearestJet.clone()
process.GsfDRToNearestJet.probes = cms.InputTag( ELECTRON_COLL )
process.JetMultiplicityInGsfEvents = process.JetMultiplicityInSCEvents.clone()
process.JetMultiplicityInGsfEvents.probes = cms.InputTag( ELECTRON_COLL )

process.ext_ToNearestJet_sequence = cms.Sequence(
    #process.ak5PFResidual + 
    process.superClusterDRToNearestJet +
    process.JetMultiplicityInSCEvents +
    process.SCConvRejVars +
    process.PhotonDRToNearestJet +
    process.JetMultiplicityInPhotonEvents +    
    process.PhotonConvRejVars + 
    process.GsfDRToNearestJet +
    process.JetMultiplicityInGsfEvents +
    process.GsfConvRejVars
    )


##    _____             ____        __ _       _ _   _             
##   |_   _|_ _  __ _  |  _ \  ___ / _(_)_ __ (_) |_(_) ___  _ __  
##     | |/ _` |/ _` | | | | |/ _ \ |_| | '_ \| | __| |/ _ \| '_ \ 
##     | | (_| | (_| | | |_| |  __/  _| | | | | | |_| | (_) | | | |
##     |_|\__,_|\__, | |____/ \___|_| |_|_| |_|_|\__|_|\___/|_| |_|
##              |___/
## 
process.Tag = process.PassingHLT.clone()
process.Tag.InputProducer = cms.InputTag( "PassingWPNone" )
process.TagMatchedSuperClusterCandsClean = cms.EDProducer("ElectronMatchedCandidateProducer",
   src     = cms.InputTag("goodSuperClustersClean"),
   ReferenceElectronCollection = cms.untracked.InputTag("Tag"),
   deltaR =  cms.untracked.double(0.3)
)
process.TagMatchedPhotonCands = process.TagMatchedSuperClusterCandsClean.clone()
process.TagMatchedPhotonCands.src     = cms.InputTag("goodPhotons")
process.WPTightMatchedSuperClusterCandsClean = process.TagMatchedSuperClusterCandsClean.clone()
process.WPTightMatchedSuperClusterCandsClean.ReferenceElectronCollection = cms.untracked.InputTag("PassingWPTight")
process.WPMediumMatchedSuperClusterCandsClean = process.TagMatchedSuperClusterCandsClean.clone()
process.WPMediumMatchedSuperClusterCandsClean.ReferenceElectronCollection = cms.untracked.InputTag("PassingWPMedium")
process.WPLooseMatchedSuperClusterCandsClean = process.TagMatchedSuperClusterCandsClean.clone()
process.WPLooseMatchedSuperClusterCandsClean.ReferenceElectronCollection = cms.untracked.InputTag("PassingWPLoose")
process.WPNoneMatchedSuperClusterCandsClean = process.TagMatchedSuperClusterCandsClean.clone()
process.WPNoneMatchedSuperClusterCandsClean.ReferenceElectronCollection = cms.untracked.InputTag("PassingWPNone")
process.CicVeryLooseMatchedSuperClusterCandsClean = process.TagMatchedSuperClusterCandsClean.clone()
process.CicVeryLooseMatchedSuperClusterCandsClean.ReferenceElectronCollection = cms.untracked.InputTag("PassingCicVeryLoose")
process.CicLooseMatchedSuperClusterCandsClean = process.TagMatchedSuperClusterCandsClean.clone()
process.CicLooseMatchedSuperClusterCandsClean.ReferenceElectronCollection = cms.untracked.InputTag("PassingCicLoose")
process.CicMediumMatchedSuperClusterCandsClean = process.TagMatchedSuperClusterCandsClean.clone()
process.CicMediumMatchedSuperClusterCandsClean.ReferenceElectronCollection = cms.untracked.InputTag("PassingCicMedium")
process.CicTightMatchedSuperClusterCandsClean = process.TagMatchedSuperClusterCandsClean.clone()
process.CicTightMatchedSuperClusterCandsClean.ReferenceElectronCollection = cms.untracked.InputTag("PassingCicTight")
process.CicSuperTightMatchedSuperClusterCandsClean = process.TagMatchedSuperClusterCandsClean.clone()
process.CicSuperTightMatchedSuperClusterCandsClean.ReferenceElectronCollection = cms.untracked.InputTag("PassingCicSuperTight")


process.WPTightMatchedPhotonCands = process.GsfMatchedPhotonCands.clone()
process.WPTightMatchedPhotonCands.ReferenceElectronCollection = cms.untracked.InputTag("PassingWPTight")
process.WPMediumMatchedPhotonCands = process.GsfMatchedPhotonCands.clone()
process.WPMediumMatchedPhotonCands.ReferenceElectronCollection = cms.untracked.InputTag("PassingWPMedium")
process.WPLooseMatchedPhotonCands = process.GsfMatchedPhotonCands.clone()
process.WPLooseMatchedPhotonCands.ReferenceElectronCollection = cms.untracked.InputTag("PassingWPLoose")
process.WPNoneMatchedPhotonCands = process.GsfMatchedPhotonCands.clone()
process.WPNoneMatchedPhotonCands.ReferenceElectronCollection = cms.untracked.InputTag("PassingWPNone")
process.CicVeryLooseMatchedPhotonCands = process.GsfMatchedPhotonCands.clone()
process.CicVeryLooseMatchedPhotonCands.ReferenceElectronCollection = cms.untracked.InputTag("PassingCicVeryLoose")
process.CicLooseMatchedPhotonCands = process.GsfMatchedPhotonCands.clone()
process.CicLooseMatchedPhotonCands.ReferenceElectronCollection = cms.untracked.InputTag("PassingCicLoose")
process.CicMediumMatchedPhotonCands = process.GsfMatchedPhotonCands.clone()
process.CicMediumMatchedPhotonCands.ReferenceElectronCollection = cms.untracked.InputTag("PassingCicMedium")
process.CicTightMatchedPhotonCands = process.GsfMatchedPhotonCands.clone()
process.CicTightMatchedPhotonCands.ReferenceElectronCollection = cms.untracked.InputTag("PassingCicTight")
process.CicSuperTightMatchedPhotonCands = process.GsfMatchedPhotonCands.clone()
process.CicSuperTightMatchedPhotonCands.ReferenceElectronCollection = cms.untracked.InputTag("PassingCicSuperTight")

process.ele_sequence = cms.Sequence(
    process.goodElectrons +
    process.GsfMatchedSuperClusterCands +
    process.GsfMatchedPhotonCands +
    process.PassingWPTight +
    process.PassingWPMedium +
    process.PassingWPLoose +
    process.PassingWPNone +
    process.PassingCicVeryLoose +
    process.PassingCicLoose +
    process.PassingCicMedium +
    process.PassingCicTight +
    process.PassingCicSuperTight +
    process.PassingHLT +
    process.Tag +
    process.TagMatchedSuperClusterCandsClean +
    process.TagMatchedPhotonCands +
    process.WPTightMatchedSuperClusterCandsClean + 
    process.WPMediumMatchedSuperClusterCandsClean + 
    process.WPLooseMatchedSuperClusterCandsClean + 
    process.WPNoneMatchedSuperClusterCandsClean + 
    process.CicVeryLooseMatchedSuperClusterCandsClean +
    process.CicLooseMatchedSuperClusterCandsClean +
    process.CicMediumMatchedSuperClusterCandsClean +
    process.CicTightMatchedSuperClusterCandsClean +
    process.CicSuperTightMatchedSuperClusterCandsClean +
    process.WPTightMatchedPhotonCands +
    process.WPMediumMatchedPhotonCands +
    process.WPLooseMatchedPhotonCands +
    process.WPNoneMatchedPhotonCands +
    process.CicVeryLooseMatchedPhotonCands +
    process.CicLooseMatchedPhotonCands +
    process.CicMediumMatchedPhotonCands +
    process.CicTightMatchedPhotonCands +
    process.CicSuperTightMatchedPhotonCands
    )


##    _____ ___   ____    ____       _          
##   |_   _( _ ) |  _ \  |  _ \ __ _(_)_ __ ___ 
##     | | / _ \/\ |_) | | |_) / _` | | '__/ __|
##     | || (_>  <  __/  |  __/ (_| | | |  \__ \
##     |_| \___/\/_|     |_|   \__,_|_|_|  |___/
##                                              
##   
#  Tag & probe selection ######
process.tagSC = cms.EDProducer("CandViewShallowCloneCombiner",
    decay = cms.string("Tag goodSuperClustersClean"), # charge coniugate states are implied
    checkCharge = cms.bool(False),                           
    cut   = cms.string("40 < mass < 1000"),
)

process.tagPhoton = process.tagSC.clone()
process.tagPhoton.decay = cms.string("Tag goodPhotons")
process.GsfGsf = process.tagSC.clone()
process.GsfGsf.decay = cms.string("goodElectrons goodElectrons")
process.tagGsf = process.tagSC.clone()
process.tagGsf.decay = cms.string("Tag goodElectrons")
process.tagWPTight = process.tagSC.clone()
process.tagWPTight.decay = cms.string("Tag PassingWPTight")
process.tagWPMedium = process.tagSC.clone()
process.tagWPMedium.decay = cms.string("Tag PassingWPMedium")
process.tagWPLoose = process.tagSC.clone()
process.tagWPLoose.decay = cms.string("Tag PassingWPLoose")
process.tagWPNone = process.tagSC.clone()
process.tagWPNone.decay = cms.string("Tag PassingWPNone")
process.tagCicVeryLoose = process.tagSC.clone()
process.tagCicVeryLoose.decay = cms.string("Tag PassingCicVeryLoose")
process.tagCicLoose = process.tagSC.clone()
process.tagCicLoose.decay = cms.string("Tag PassingCicLoose")
process.tagCicMedium = process.tagSC.clone()
process.tagCicMedium.decay = cms.string("Tag PassingCicMedium")
process.tagCicTight = process.tagSC.clone()
process.tagCicTight.decay = cms.string("Tag PassingCicTight")
process.tagCicSuperTight = process.tagSC.clone()
process.tagCicSuperTight.decay = cms.string("Tag PassingCicSuperTight")
process.elecMet = process.tagSC.clone()
process.elecMet.decay = cms.string("pfMet PassingWPNone")
process.elecMet.cut = cms.string("mt > 0")

process.CSVarsTagGsf = cms.EDProducer("ColinsSoperVariablesComputer",
    parentBoson = cms.InputTag("tagGsf")
)
process.CSVarsGsfGsf = process.CSVarsTagGsf.clone()
process.CSVarsGsfGsf.parentBoson = cms.InputTag("GsfGsf")



process.allTagsAndProbes = cms.Sequence(
    process.tagSC +
    process.tagPhoton +
    process.tagGsf +
    process.GsfGsf +
    process.tagWPTight +
    process.tagWPMedium +
    process.tagWPLoose +
    process.tagWPNone +
    process.tagCicVeryLoose +
    process.tagCicLoose +
    process.tagCicMedium +
    process.tagCicTight +
    process.tagCicSuperTight +
    process.elecMet + 
    process.CSVarsTagGsf +
    process.CSVarsGsfGsf
)

##    __  __  ____   __  __       _       _               
##   |  \/  |/ ___| |  \/  | __ _| |_ ___| |__   ___  ___ 
##   | |\/| | |     | |\/| |/ _` | __/ __| '_ \ / _ \/ __|
##   | |  | | |___  | |  | | (_| | || (__| | | |  __/\__ \
##   |_|  |_|\____| |_|  |_|\__,_|\__\___|_| |_|\___||___/
##                                                        
process.McMatchTag = cms.EDProducer("MCTruthDeltaRMatcherNew",
    matchPDGId = cms.vint32(11),
    src = cms.InputTag("Tag"),
    distMin = cms.double(0.3),
    matched = cms.InputTag("genParticles"),
    checkCharge = cms.bool(True)
)
process.McMatchSC = cms.EDProducer("MCTruthDeltaRMatcherNew",
    matchPDGId = cms.vint32(11),
    src = cms.InputTag("goodSuperClustersClean"),
    distMin = cms.double(0.3),
    matched = cms.InputTag("genParticles")
)
process.McMatchPhoton = process.McMatchSC.clone()
process.McMatchPhoton.src = cms.InputTag("goodPhotons")
process.McMatchGsf = process.McMatchTag.clone()
process.McMatchGsf.src = cms.InputTag("goodElectrons")
process.McMatchWPTight = process.McMatchTag.clone()
process.McMatchWPTight.src = cms.InputTag("PassingWPTight")
process.McMatchWPMedium = process.McMatchTag.clone()
process.McMatchWPMedium.src = cms.InputTag("PassingWPMedium")
process.McMatchWPLoose = process.McMatchTag.clone()
process.McMatchWPLoose.src = cms.InputTag("PassingWPLoose")
process.McMatchWPNone = process.McMatchTag.clone()
process.McMatchWPNone.src = cms.InputTag("PassingWPNone")
process.McMatchCicVeryLoose = process.McMatchTag.clone()
process.McMatchCicVeryLoose.src = cms.InputTag("PassingCicVeryLoose")
process.McMatchCicLoose = process.McMatchTag.clone()
process.McMatchCicLoose.src = cms.InputTag("PassingCicLoose")
process.McMatchCicMedium = process.McMatchTag.clone()
process.McMatchCicMedium.src = cms.InputTag("PassingCicMedium")
process.McMatchCicTight = process.McMatchTag.clone()
process.McMatchCicTight.src = cms.InputTag("PassingCicTight")
process.McMatchCicSuperTight = process.McMatchTag.clone()
process.McMatchCicSuperTight.src = cms.InputTag("PassingCicSuperTight")
    
process.mc_sequence = cms.Sequence(
   process.McMatchTag +
   process.McMatchSC +
   process.McMatchPhoton +
   process.McMatchGsf + 
   process.McMatchWPTight +
   process.McMatchWPMedium +
   process.McMatchWPLoose +
   process.McMatchWPNone +
   process.McMatchCicVeryLoose +
   process.McMatchCicLoose +
   process.McMatchCicMedium +
   process.McMatchCicTight +
   process.McMatchCicSuperTight
)

############################################################################
##    _____           _       _ ____            _            _   _  ____  ##
##   |_   _|_ _  __ _( )_ __ ( )  _ \ _ __ ___ | |__   ___  | \ | |/ ___| ##
##     | |/ _` |/ _` |/| '_ \|/| |_) | '__/ _ \| '_ \ / _ \ |  \| | |  _  ##
##     | | (_| | (_| | | | | | |  __/| | | (_) | |_) |  __/ | |\  | |_| | ##
##     |_|\__,_|\__, | |_| |_| |_|   |_|  \___/|_.__/ \___| |_| \_|\____| ##
##              |___/                                                     ##
##                                                                        ##
############################################################################
##    ____                      _     _           
##   |  _ \ ___ _   _ ___  __ _| |__ | | ___  ___ 
##   | |_) / _ \ | | / __|/ _` | '_ \| |/ _ \/ __|
##   |  _ <  __/ |_| \__ \ (_| | |_) | |  __/\__ \
##   |_| \_\___|\__,_|___/\__,_|_.__/|_|\___||___/
##
## I define some common variables for re-use later.
## This will save us repeating the same code for each efficiency category
ZVariablesToStore = cms.PSet(
    eta = cms.string("eta"),
    pt  = cms.string("pt"),
    phi  = cms.string("phi"),
    et  = cms.string("et"),
    e  = cms.string("energy"),
    p  = cms.string("p"),
    px  = cms.string("px"),
    py  = cms.string("py"),
    pz  = cms.string("pz"),
    theta  = cms.string("theta"),    
    vx     = cms.string("vx"),
    vy     = cms.string("vy"),
    vz     = cms.string("vz"),
    rapidity  = cms.string("rapidity"),
    mass  = cms.string("mass"),
    mt  = cms.string("mt"),    
)   

ProbeVariablesToStore = cms.PSet(
    probe_gsfEle_eta = cms.string("eta"),
    probe_gsfEle_pt  = cms.string("pt"),
    probe_gsfEle_phi  = cms.string("phi"),
    probe_gsfEle_et  = cms.string("et"),
    probe_gsfEle_e  = cms.string("energy"),
    probe_gsfEle_p  = cms.string("p"),
    probe_gsfEle_px  = cms.string("px"),
    probe_gsfEle_py  = cms.string("py"),
    probe_gsfEle_pz  = cms.string("pz"),
    probe_gsfEle_theta  = cms.string("theta"),    
    probe_gsfEle_charge = cms.string("charge"),
    probe_gsfEle_rapidity  = cms.string("rapidity"),
    probe_gsfEle_missingHits = cms.string("gsfTrack.trackerExpectedHitsInner.numberOfHits"),
    probe_gsfEle_convDist = cms.string("convDist"),
    probe_gsfEle_convDcot = cms.string("convDcot"),
    probe_gsfEle_convRadius = cms.string("convRadius"),        
    probe_gsfEle_hasValidHitInFirstPixelBarrel = cms.string("gsfTrack.hitPattern.hasValidHitInFirstPixelBarrel"),
    ## super cluster quantities
    probe_sc_energy = cms.string("superCluster.energy"),
    probe_sc_et    = cms.string("superCluster.energy*sin(superClusterPosition.theta)"),    
    probe_sc_x      = cms.string("superCluster.x"),
    probe_sc_y      = cms.string("superCluster.y"),
    probe_sc_z      = cms.string("superCluster.z"),
    probe_sc_eta    = cms.string("abs(superCluster.eta)"),
    probe_sc_theta  = cms.string("superClusterPosition.theta"),   
    probe_sc_phi    = cms.string("superCluster.phi"),
    probe_sc_size   = cms.string("superCluster.size"), # number of hits
    ## track quantities
    probe_track_p      = cms.string("gsfTrack.p"),
    probe_track_pt     = cms.string("gsfTrack.pt"),    
    probe_track_px     = cms.string("gsfTrack.px"),
    probe_track_py     = cms.string("gsfTrack.py"),
    probe_track_pz     = cms.string("gsfTrack.pz"),
    probe_track_eta    = cms.string("gsfTrack.eta"),
    probe_track_theta  = cms.string("gsfTrack.theta"),   
    probe_track_phi    = cms.string("gsfTrack.phi"),
    probe_track_vx     = cms.string("gsfTrack.vx"),
    probe_track_vy     = cms.string("gsfTrack.vy"),
    probe_track_vz     = cms.string("gsfTrack.vz"),    
    probe_track_dxy    = cms.string("gsfTrack.dxy"),
    probe_track_d0     = cms.string("gsfTrack.d0"),
    probe_track_dsz    = cms.string("gsfTrack.dsz"),
    probe_track_charge = cms.string("gsfTrack.charge"),
    probe_track_qoverp = cms.string("gsfTrack.qoverp"),
    probe_track_normalizedChi2 = cms.string("gsfTrack.normalizedChi2"),
    ## isolation 
    probe_gsfEle_trackiso = cms.string("dr03TkSumPt"),
    probe_gsfEle_ecaliso  = cms.string("dr03EcalRecHitSumEt"),
    probe_gsfEle_hcaliso  = cms.string("dr03HcalTowerSumEt"),
    ## classification, location, etc.    
    probe_gsfEle_classification = cms.string("classification"),
    probe_gsfEle_numberOfBrems  = cms.string("numberOfBrems"),     
    probe_gsfEle_bremFraction   = cms.string("fbrem"),
    probe_gsfEle_mva            = cms.string("mva"),        
    probe_gsfEle_deltaEta       = cms.string("deltaEtaSuperClusterTrackAtVtx"),
    probe_gsfEle_deltaPhi       = cms.string("deltaPhiSuperClusterTrackAtVtx"),
    probe_gsfEle_deltaPhiOut    = cms.string("deltaPhiSeedClusterTrackAtCalo"),
    probe_gsfEle_deltaEtaOut    = cms.string("deltaEtaSeedClusterTrackAtCalo"),
    probe_gsfEle_isEB           = cms.string("isEB"),
    probe_gsfEle_isEE           = cms.string("isEE"),
    probe_gsfEle_isGap          = cms.string("isGap"),
    ## Hcal energy over Ecal Energy
    probe_gsfEle_HoverE         = cms.string("hcalOverEcal"),    
    probe_gsfEle_EoverP         = cms.string("eSuperClusterOverP"),
    probe_gsfEle_eSeedClusterOverP = cms.string("eSeedClusterOverP"),    
    ## Cluster shape information
    probe_gsfEle_sigmaEtaEta  = cms.string("sigmaEtaEta"),
    probe_gsfEle_sigmaIetaIeta = cms.string("sigmaIetaIeta"),
    probe_gsfEle_e1x5               = cms.string("e1x5"),
    probe_gsfEle_e2x5Max            = cms.string("e2x5Max"),
    probe_gsfEle_e5x5               = cms.string("e5x5"),
    ## is ECAL driven ? is Track driven ?
    probe_gsfEle_ecalDrivenSeed     = cms.string("ecalDrivenSeed"),
    probe_gsfEle_trackerDrivenSeed  = cms.string("trackerDrivenSeed")
)


TagVariablesToStore = cms.PSet(
    gsfEle_eta = cms.string("eta"),
    gsfEle_pt  = cms.string("pt"),
    gsfEle_phi  = cms.string("phi"),
    gsfEle_et  = cms.string("et"),
    gsfEle_e  = cms.string("energy"),
    gsfEle_p  = cms.string("p"),
    gsfEle_px  = cms.string("px"),
    gsfEle_py  = cms.string("py"),
    gsfEle_pz  = cms.string("pz"),
    gsfEle_theta  = cms.string("theta"),    
    gsfEle_charge = cms.string("charge"),
    gsfEle_rapidity  = cms.string("rapidity"),
    gsfEle_missingHits = cms.string("gsfTrack.trackerExpectedHitsInner.numberOfHits"),
    gsfEle_convDist = cms.string("convDist"),
    gsfEle_convDcot = cms.string("convDcot"),
    gsfEle_convRadius = cms.string("convRadius"),     
    gsfEle_hasValidHitInFirstPixelBarrel = cms.string("gsfTrack.hitPattern.hasValidHitInFirstPixelBarrel"),
    ## super cluster quantities
    sc_energy = cms.string("superCluster.energy"),
    sc_et     = cms.string("superCluster.energy*sin(superClusterPosition.theta)"),    
    sc_x      = cms.string("superCluster.x"),
    sc_y      = cms.string("superCluster.y"),
    sc_z      = cms.string("superCluster.z"),
    sc_eta    = cms.string("superCluster.eta"),
    sc_theta  = cms.string("superClusterPosition.theta"),      
    sc_phi    = cms.string("superCluster.phi"),
    sc_size   = cms.string("superCluster.size"), # number of hits
    ## track quantities
    track_p      = cms.string("gsfTrack.p"),
    track_pt     = cms.string("gsfTrack.pt"),    
    track_px     = cms.string("gsfTrack.px"),
    track_py     = cms.string("gsfTrack.py"),
    track_pz     = cms.string("gsfTrack.pz"),
    track_eta    = cms.string("gsfTrack.eta"),
    track_theta  = cms.string("gsfTrack.theta"),   
    track_phi    = cms.string("gsfTrack.phi"),
    track_vx     = cms.string("gsfTrack.vx"),
    track_vy     = cms.string("gsfTrack.vy"),
    track_vz     = cms.string("gsfTrack.vz"),    
    track_dxy    = cms.string("gsfTrack.dxy"),
    track_d0     = cms.string("gsfTrack.d0"),
    track_dsz    = cms.string("gsfTrack.dsz"),
    track_charge = cms.string("gsfTrack.charge"),
    track_qoverp = cms.string("gsfTrack.qoverp"),
    track_normalizedChi2 = cms.string("gsfTrack.normalizedChi2"),    
    ## isolation 
    gsfEle_trackiso = cms.string("dr03TkSumPt"),
    gsfEle_ecaliso  = cms.string("dr03EcalRecHitSumEt"),
    gsfEle_hcaliso  = cms.string("dr03HcalTowerSumEt"),
    ## classification, location, etc.    
    gsfEle_classification = cms.string("classification"),
    gsfEle_numberOfBrems  = cms.string("numberOfBrems"),     
    gsfEle_bremFraction   = cms.string("fbrem"),
    gsfEle_mva            = cms.string("mva"),        
    gsfEle_deltaEta       = cms.string("deltaEtaSuperClusterTrackAtVtx"),
    gsfEle_deltaPhi       = cms.string("deltaPhiSuperClusterTrackAtVtx"),
    gsfEle_deltaPhiOut    = cms.string("deltaPhiSeedClusterTrackAtCalo"),
    gsfEle_deltaEtaOut    = cms.string("deltaEtaSeedClusterTrackAtCalo"),
    gsfEle_isEB           = cms.string("isEB"),
    gsfEle_isEE           = cms.string("isEE"),
    gsfEle_isGap          = cms.string("isGap"),
    ## Hcal energy over Ecal Energy
    gsfEle_HoverE         = cms.string("hcalOverEcal"),    
    gsfEle_EoverP         = cms.string("eSuperClusterOverP"),
    gsfEle_eSeedClusterOverP = cms.string("eSeedClusterOverP"),  
    ## Cluster shape information
    gsfEle_sigmaEtaEta  = cms.string("sigmaEtaEta"),
    gsfEle_sigmaIetaIeta = cms.string("sigmaIetaIeta"),
    gsfEle_e1x5               = cms.string("e1x5"),
    gsfEle_e2x5Max            = cms.string("e2x5Max"),
    gsfEle_e5x5               = cms.string("e5x5"),
    ## is ECAL driven ? is Track driven ?
    gsfEle_ecalDrivenSeed     = cms.string("ecalDrivenSeed"),
    gsfEle_trackerDrivenSeed  = cms.string("trackerDrivenSeed")
)

CommonStuffForGsfElectronProbe = cms.PSet(
    variables = cms.PSet(ProbeVariablesToStore),
    ignoreExceptions =  cms.bool (False),
    addRunLumiInfo   =  cms.bool (True),
    addEventVariablesInfo   =  cms.bool (True),
    pairVariables =  cms.PSet(ZVariablesToStore),
    pairFlags     =  cms.PSet(
          mass60to120 = cms.string("60 < mass < 120")
    ),
    tagVariables   =  cms.PSet(TagVariablesToStore),
    tagFlags     =  cms.PSet(
          passingGsf = cms.InputTag("goodElectrons"),
          isWPTight = cms.InputTag("PassingWPTight"),
          isWPMedium = cms.InputTag("PassingWPMedium"),
          isWPLoose = cms.InputTag("PassingWPLoose"),
          isWPNone = cms.InputTag("PassingWPNone"),
          isCicVeryLoose = cms.InputTag("PassingCicVeryLoose"),
          isCicLoose = cms.InputTag("PassingCicLoose"),
          isCicMedium = cms.InputTag("PassingCicMedium"),
          isCicTight = cms.InputTag("PassingCicTight"),
          isCicSuperTight = cms.InputTag("PassingCicSuperTight"),
          passingHLT = cms.InputTag("PassingHLT")     
    ),    
)

CommonStuffForSuperClusterProbe = CommonStuffForGsfElectronProbe.clone()
CommonStuffForSuperClusterProbe.variables = cms.PSet(
    probe_eta = cms.string("abs(eta)"),
    probe_pt  = cms.string("pt"),
    probe_phi  = cms.string("phi"),
    probe_et  = cms.string("et"),
    probe_e  = cms.string("energy"),
    probe_p  = cms.string("p"),
    probe_px  = cms.string("px"),
    probe_py  = cms.string("py"),
    probe_pz  = cms.string("pz"),
    probe_theta  = cms.string("theta"),
    )


if False:#MC_flag:
    mcTruthCommonStuff = cms.PSet(
        isMC = cms.bool(MC_flag),
        tagMatches = cms.InputTag("McMatchTag"),
        motherPdgId = cms.vint32(22,23),
        makeMCUnbiasTree = cms.bool(MC_flag),
        checkMotherInUnbiasEff = cms.bool(MC_flag),
        mcVariables = cms.PSet(
        probe_eta = cms.string("abs(eta)"),
        probe_pt  = cms.string("pt"),
        probe_phi  = cms.string("phi"),
        probe_et  = cms.string("et"),
        probe_e  = cms.string("energy"),
        probe_p  = cms.string("p"),
        probe_px  = cms.string("px"),
        probe_py  = cms.string("py"),
        probe_pz  = cms.string("pz"),
        probe_theta  = cms.string("theta"),    
        probe_vx     = cms.string("vx"),
        probe_vy     = cms.string("vy"),
        probe_vz     = cms.string("vz"),   
        probe_charge = cms.string("charge"),
        probe_rapidity  = cms.string("rapidity"),    
        probe_mass  = cms.string("mass"),
        probe_mt  = cms.string("mt"),    
        ),
        mcFlags     =  cms.PSet(
        probe_flag = cms.string("pt>0")
        ),      
        )
else:
     mcTruthCommonStuff = cms.PSet(
         isMC = cms.bool(False)
         )


##    ____   ____       __     ____      __ 
##   / ___| / ___|      \ \   / ___|___ / _|
##   \___ \| |      _____\ \ | |  _/ __| |_ 
##    ___) | |___  |_____/ / | |_| \__ \  _|
##   |____/ \____|      /_/   \____|___/_|  
##
## super cluster --> gsf electron
process.SuperClusterToGsfElectron = cms.EDAnalyzer("TagProbeFitTreeProducer",
    ## pick the defaults
    CommonStuffForSuperClusterProbe, mcTruthCommonStuff,
    # choice of tag and probe pairs, and arbitration                 
    tagProbePairs = cms.InputTag("tagSC"),
    arbitration   = cms.string("Random2"),                      
    flags = cms.PSet(
        probe_passingGsf = cms.InputTag("GsfMatchedSuperClusterCands"),
        probe_isWPTight = cms.InputTag("WPTightMatchedSuperClusterCandsClean"),
        probe_isWPMedium = cms.InputTag("WPMediumMatchedSuperClusterCandsClean"),
        probe_isWPLoose = cms.InputTag("WPLooseMatchedSuperClusterCandsClean"),
        probe_isWPNone = cms.InputTag("WPNoneMatchedSuperClusterCandsClean"),
        probe_isCicVeryLoose = cms.InputTag("CicVeryLooseMatchedSuperClusterCandsClean"), 
        probe_isCicLoose = cms.InputTag("CicLooseMatchedSuperClusterCandsClean"), 
        probe_isCicMedium = cms.InputTag("CicMediumMatchedSuperClusterCandsClean"), 
        probe_isCicTight = cms.InputTag("CicTightMatchedSuperClusterCandsClean"), 
        probe_isCicSuperTight = cms.InputTag("CicSuperTightMatchedSuperClusterCandsClean"),        
        probe_passingHLT = cms.InputTag("TagMatchedSuperClusterCandsClean")
    ),
    probeMatches  = cms.InputTag("McMatchSC"),
    allProbes     = cms.InputTag("goodSuperClustersClean")
)
process.SuperClusterToGsfElectron.variables.probe_dRjet = cms.InputTag("superClusterDRToNearestJet")
process.SuperClusterToGsfElectron.variables.probe_nJets = cms.InputTag("JetMultiplicityInSCEvents")
process.SuperClusterToGsfElectron.variables.probe_dist = cms.InputTag("SCConvRejVars","dist")
process.SuperClusterToGsfElectron.variables.probe_dcot = cms.InputTag("SCConvRejVars","dcot")
process.SuperClusterToGsfElectron.variables.probe_convradius = cms.InputTag("SCConvRejVars","convradius")
process.SuperClusterToGsfElectron.variables.probe_passConvRej = cms.InputTag("SCConvRejVars","passConvRej")
process.SuperClusterToGsfElectron.tagVariables.dRjet = cms.InputTag("GsfDRToNearestJet")
process.SuperClusterToGsfElectron.tagVariables.nJets = cms.InputTag("JetMultiplicityInGsfEvents")
process.SuperClusterToGsfElectron.tagVariables.eidCicVeryLoose = cms.InputTag("eidVeryLoose")
process.SuperClusterToGsfElectron.tagVariables.eidCicLoose = cms.InputTag("eidLoose")
process.SuperClusterToGsfElectron.tagVariables.eidCicMedium = cms.InputTag("eidMedium")
process.SuperClusterToGsfElectron.tagVariables.eidCicTight = cms.InputTag("eidTight")
process.SuperClusterToGsfElectron.tagVariables.eidCicSuperTight = cms.InputTag("eidSuperTight")
process.SuperClusterToGsfElectron.tagVariables.eidLikelihood = cms.InputTag("eidLikelihoodExt")
process.SuperClusterToGsfElectron.tagVariables.dist = cms.InputTag("GsfConvRejVars","dist")
process.SuperClusterToGsfElectron.tagVariables.dcot = cms.InputTag("GsfConvRejVars","dcot")
process.SuperClusterToGsfElectron.tagVariables.convradius = cms.InputTag("GsfConvRejVars","convradius")
process.SuperClusterToGsfElectron.tagVariables.passConvRej = cms.InputTag("GsfConvRejVars","passConvRej")



## good photon --> gsf electron
process.PhotonToGsfElectron = process.SuperClusterToGsfElectron.clone()
process.PhotonToGsfElectron.tagProbePairs = cms.InputTag("tagPhoton")
process.PhotonToGsfElectron.flags = cms.PSet(
    probe_passingGsf = cms.InputTag("GsfMatchedPhotonCands"),
    probe_passingHLT = cms.InputTag("TagMatchedPhotonCands"),
    probe_isWPTight = cms.InputTag("WPTightMatchedPhotonCands"),
    probe_isWPMedium = cms.InputTag("WPMediumMatchedPhotonCands"),
    probe_isWPLoose = cms.InputTag("WPLooseMatchedPhotonCands"),
    probe_isWPNone = cms.InputTag("WPNoneMatchedPhotonCands"),
    probe_isCicVeryLoose = cms.InputTag("CicVeryLooseMatchedPhotonCands"), 
    probe_isCicLoose = cms.InputTag("CicLooseMatchedPhotonCands"), 
    probe_isCicMedium = cms.InputTag("CicMediumMatchedPhotonCands"), 
    probe_isCicTight = cms.InputTag("CicTightMatchedPhotonCands"), 
    probe_isCicSuperTight = cms.InputTag("CicSuperTightMatchedPhotonCands"), 
    )
process.PhotonToGsfElectron.probeMatches  = cms.InputTag("McMatchPhoton")
process.PhotonToGsfElectron.allProbes     = cms.InputTag("goodPhotons")
process.PhotonToGsfElectron.variables.probe_dRjet = cms.InputTag("PhotonDRToNearestJet")
process.PhotonToGsfElectron.variables.probe_nJets = cms.InputTag("JetMultiplicityInPhotonEvents")
process.PhotonToGsfElectron.variables.probe_trackiso = cms.string("trkSumPtHollowConeDR03")
process.PhotonToGsfElectron.variables.probe_ecaliso = cms.string("ecalRecHitSumEtConeDR03")
process.PhotonToGsfElectron.variables.probe_hcaliso = cms.string("hcalTowerSumEtConeDR03")
process.PhotonToGsfElectron.variables.probe_HoverE  = cms.string("hadronicOverEm")
process.PhotonToGsfElectron.variables.probe_sigmaIetaIeta = cms.string("sigmaIetaIeta")
process.PhotonToGsfElectron.variables.probe_dist = cms.InputTag("PhotonConvRejVars","dist")
process.PhotonToGsfElectron.variables.probe_dcot = cms.InputTag("PhotonConvRejVars","dcot")
process.PhotonToGsfElectron.variables.probe_convradius = cms.InputTag("PhotonConvRejVars","convradius")
process.PhotonToGsfElectron.variables.probe_passConvRej = cms.InputTag("PhotonConvRejVars","passConvRej")
process.PhotonToGsfElectron.tagVariables.dRjet = cms.InputTag("GsfDRToNearestJet")
process.PhotonToGsfElectron.tagVariables.nJets = cms.InputTag("JetMultiplicityInGsfEvents")
process.PhotonToGsfElectron.tagVariables.eidCicVeryLoose = cms.InputTag("eidVeryLoose")
process.PhotonToGsfElectron.tagVariables.eidCicLoose = cms.InputTag("eidLoose")
process.PhotonToGsfElectron.tagVariables.eidCicMedium = cms.InputTag("eidMedium")
process.PhotonToGsfElectron.tagVariables.eidCicTight = cms.InputTag("eidTight")
process.PhotonToGsfElectron.tagVariables.eidCicSuperTight = cms.InputTag("eidSuperTight")
process.PhotonToGsfElectron.tagVariables.eidLikelihood = cms.InputTag("eidLikelihoodExt")
process.PhotonToGsfElectron.tagVariables.dist = cms.InputTag("GsfConvRejVars","dist")
process.PhotonToGsfElectron.tagVariables.dcot = cms.InputTag("GsfConvRejVars","dcot")
process.PhotonToGsfElectron.tagVariables.convradius = cms.InputTag("GsfConvRejVars","convradius")
process.PhotonToGsfElectron.tagVariables.passConvRej = cms.InputTag("GsfConvRejVars","passConvRej")

##   ____      __       __    ___                 ___    _ 
##  / ___|___ / _|      \ \  |_ _|___  ___       |_ _|__| |
## | |  _/ __| |_   _____\ \  | |/ __|/ _ \       | |/ _` |
## | |_| \__ \  _| |_____/ /  | |\__ \ (_) |  _   | | (_| |
##  \____|___/_|        /_/  |___|___/\___/  ( ) |___\__,_|
##                                           |/            
##  gsf electron --> isolation, electron id  etc.
process.GsfElectronToId = cms.EDAnalyzer("TagProbeFitTreeProducer",
    mcTruthCommonStuff, CommonStuffForGsfElectronProbe,                        
    tagProbePairs = cms.InputTag("tagGsf"),
    arbitration   = cms.string("Random2"),
    flags = cms.PSet(
        probe_isWPTight = cms.InputTag("PassingWPTight"),
        probe_isWPMedium = cms.InputTag("PassingWPMedium"),
        probe_isWPLoose = cms.InputTag("PassingWPLoose"),
        probe_isWPNone = cms.InputTag("PassingWPNone"),
        probe_isCicVeryLoose = cms.InputTag("PassingCicVeryLoose"),
        probe_isCicLoose = cms.InputTag("PassingCicLoose"),
        probe_isCicMedium = cms.InputTag("PassingCicMedium"),
        probe_isCicTight = cms.InputTag("PassingCicTight"),
        probe_isCicSuperTight = cms.InputTag("PassingCicSuperTight"),
        probe_passingHLT = cms.InputTag("PassingHLT")        
    ),
    probeMatches  = cms.InputTag("McMatchGsf"),
    allProbes     = cms.InputTag("goodElectrons")
)
process.GsfElectronToId.variables.probe_dRjet = cms.InputTag("GsfDRToNearestJet")
process.GsfElectronToId.variables.probe_nJets = cms.InputTag("JetMultiplicityInGsfEvents")
process.GsfElectronToId.variables.probe_eidCicVeryLoose = cms.InputTag("eidVeryLoose")
process.GsfElectronToId.variables.probe_eidCicLoose = cms.InputTag("eidLoose")
process.GsfElectronToId.variables.probe_eidCicMedium = cms.InputTag("eidMedium")
process.GsfElectronToId.variables.probe_eidCicTight = cms.InputTag("eidTight")
process.GsfElectronToId.variables.probe_eidCicSuperTight = cms.InputTag("eidSuperTight")
process.GsfElectronToId.variables.probe_eidLikelihood = cms.InputTag("eidLikelihoodExt")
process.GsfElectronToId.variables.probe_dist = cms.InputTag("GsfConvRejVars","dist")
process.GsfElectronToId.variables.probe_dcot = cms.InputTag("GsfConvRejVars","dcot")
process.GsfElectronToId.variables.probe_convradius = cms.InputTag("GsfConvRejVars","convradius")
process.GsfElectronToId.variables.probe_passConvRej = cms.InputTag("GsfConvRejVars","passConvRej")
process.GsfElectronToId.tagVariables.dRjet = cms.InputTag("GsfDRToNearestJet")
process.GsfElectronToId.tagVariables.nJets = cms.InputTag("JetMultiplicityInGsfEvents")
process.GsfElectronToId.tagVariables.eidCicVeryLoose = cms.InputTag("eidVeryLoose")
process.GsfElectronToId.tagVariables.eidCicLoose = cms.InputTag("eidLoose")
process.GsfElectronToId.tagVariables.eidCicMedium = cms.InputTag("eidMedium")
process.GsfElectronToId.tagVariables.eidCicTight = cms.InputTag("eidTight")
process.GsfElectronToId.tagVariables.eidCicSuperTight = cms.InputTag("eidSuperTight")
process.GsfElectronToId.tagVariables.eidLikelihood = cms.InputTag("eidLikelihoodExt")
process.GsfElectronToId.tagVariables.dist = cms.InputTag("GsfConvRejVars","dist")
process.GsfElectronToId.tagVariables.dcot = cms.InputTag("GsfConvRejVars","dcot")
process.GsfElectronToId.tagVariables.convradius = cms.InputTag("GsfConvRejVars","convradius")
process.GsfElectronToId.tagVariables.passConvRej = cms.InputTag("GsfConvRejVars","passConvRej")
process.GsfElectronToId.pairVariables.costheta = cms.InputTag("CSVarsTagGsf","costheta")
process.GsfElectronToId.pairVariables.sin2theta = cms.InputTag("CSVarsTagGsf","sin2theta")
process.GsfElectronToId.pairVariables.tanphi = cms.InputTag("CSVarsTagGsf","tanphi")


process.GsfElectronPlusGsfElectron = process.GsfElectronToId.clone()
process.GsfElectronPlusGsfElectron.tagProbePairs = cms.InputTag("GsfGsf")
process.GsfElectronPlusGsfElectron.tagMatches = cms.InputTag("McMatchGsf")
process.GsfElectronPlusGsfElectron.pairVariables.costheta = cms.InputTag("CSVarsGsfGsf","costheta")
process.GsfElectronPlusGsfElectron.pairVariables.sin2theta = cms.InputTag("CSVarsGsfGsf","sin2theta")
process.GsfElectronPlusGsfElectron.pairVariables.tanphi = cms.InputTag("CSVarsGsfGsf","tanphi")


process.GsfElectronPlusMet = process.GsfElectronToId.clone()
process.GsfElectronPlusMet.tagProbePairs = cms.InputTag("elecMet")
process.GsfElectronPlusMet.tagVariables = cms.PSet()
process.GsfElectronPlusMet.pairVariables =  cms.PSet(ZVariablesToStore)
process.GsfElectronPlusMet.pairFlags =  cms.PSet( isMTabove40 = cms.string("mt > 40") )
process.GsfElectronPlusMet.isMC = cms.bool(False)


##    ___    _       __    _   _ _   _____ 
##   |_ _|__| |      \ \  | | | | | |_   _|
##    | |/ _` |  _____\ \ | |_| | |   | |  
##    | | (_| | |_____/ / |  _  | |___| |  
##   |___\__,_|      /_/  |_| |_|_____|_|
##
##  offline selection --> HLT. First specify which quantities to store in the TP tree. 
if False:#MC_flag:
    HLTmcTruthCommonStuff = cms.PSet(
        isMC = cms.bool(MC_flag),
        tagMatches = cms.InputTag("McMatchTag"),
        motherPdgId = cms.vint32(22,23),
        makeMCUnbiasTree = cms.bool(MC_flag),
        checkMotherInUnbiasEff = cms.bool(MC_flag),
        mcVariables = cms.PSet(
          probe_eta = cms.string("abs(eta)"),
          probe_phi  = cms.string("phi"),
          probe_et  = cms.string("et"),
          probe_charge = cms.string("charge"),
        ),
        mcFlags     =  cms.PSet(
          probe_flag = cms.string("pt>0")
        ),      
        )
else:
     HLTmcTruthCommonStuff = cms.PSet(
         isMC = cms.bool(False)
         )

##  WPTight --> HLT
process.WPTightToHLT = cms.EDAnalyzer("TagProbeFitTreeProducer",
    HLTmcTruthCommonStuff,                                
    variables = cms.PSet(
      probe_gsfEle_eta = cms.string("eta"),
      probe_gsfEle_phi  = cms.string("phi"),
      probe_gsfEle_et  = cms.string("et"),
      probe_gsfEle_charge = cms.string("charge"),
      probe_sc_et    = cms.string("superCluster.energy*sin(superClusterPosition.theta)"),    
      probe_sc_eta    = cms.string("abs(superCluster.eta)"), 
      probe_sc_phi    = cms.string("superCluster.phi"),
      probe_gsfEle_isEB           = cms.string("isEB"),
      probe_gsfEle_isEE           = cms.string("isEE"),
      probe_gsfEle_isGap          = cms.string("isGap"),
    ),
    ignoreExceptions =  cms.bool (False),
    addRunLumiInfo   =  cms.bool (False),
    addEventVariablesInfo   =  cms.bool (False),                                                        
    tagProbePairs = cms.InputTag("tagWPTight"),
    arbitration   = cms.string("Random2"),
    flags = cms.PSet( 
        probe_passingHLT = cms.InputTag("PassingHLT")        
    ),
    probeMatches  = cms.InputTag("McMatchWPTight"),
    allProbes     = cms.InputTag("PassingWPTight")
)

##  WPLoose --> HLT
process.WPLooseToHLT = process.WPTightToHLT.clone()
process.WPLooseToHLT.tagProbePairs = cms.InputTag("tagWPLoose")
process.WPLooseToHLT.probeMatches  = cms.InputTag("McMatchWPLoose")
process.WPLooseToHLT.allProbes     = cms.InputTag("PassingWPLoose")

##  WPMedium --> HLT
process.WPMediumToHLT = process.WPTightToHLT.clone()
process.WPMediumToHLT.tagProbePairs = cms.InputTag("tagWPMedium")
process.WPMediumToHLT.probeMatches  = cms.InputTag("McMatchWPMedium")
process.WPMediumToHLT.allProbes     = cms.InputTag("PassingWPMedium")

##  WPNone --> HLT
process.WPNoneToHLT = process.WPTightToHLT.clone()
process.WPNoneToHLT.tagProbePairs = cms.InputTag("tagWPNone")
process.WPNoneToHLT.probeMatches  = cms.InputTag("McMatchWPNone")
process.WPNoneToHLT.allProbes     = cms.InputTag("PassingWPNone")

process.tree_sequence = cms.Sequence(
    process.SuperClusterToGsfElectron +
    process.PhotonToGsfElectron +
    process.GsfElectronToId +
    process.GsfElectronPlusGsfElectron +
    process.GsfElectronPlusMet + 
    process.WPTightToHLT +
    process.WPMediumToHLT +
    process.WPLooseToHLT +
    process.WPNoneToHLT
)

##    ____       _   _     
##   |  _ \ __ _| |_| |__  
##   | |_) / _` | __| '_ \ 
##   |  __/ (_| | |_| | | |
##   |_|   \__,_|\__|_| |_|
##

if False:#MC_flag:
    process.tagAndProbe = cms.Path(
		process.patElectrons +
		process.eleRegressionEnergy +
		process.calibratedPatElectrons +
		process.pfiso +
		process.kt6PFJetsForIsolation +

        process.sc_sequence + process.eIDSequence + process.ele_sequence + 
        process.ext_ToNearestJet_sequence + 
        process.allTagsAndProbes +
        process.mc_sequence + 
        process.tree_sequence
    )
else:
    process.tagAndProbe = cms.Path(
		#process.patElectrons +
		#process.eleRegressionEnergy +
		#process.calibratedPatElectrons +
		#process.pfiso +
		#process.kt6PFJetsForIsolation +

        process.sc_sequence + process.eIDSequence + process.ele_sequence + 
        process.ext_ToNearestJet_sequence + 
        process.allTagsAndProbes +
        process.tree_sequence
    )

process.TFileService = cms.Service(
    "TFileService", fileName = cms.string(OUTPUT_FILE_NAME)
)
