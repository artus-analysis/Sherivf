import configtools


def config():
	cfg = {
		"BaseWeight": 1000,
		"CrossSection": 3503.71,
		"Energy": 8,
		"EventMetadata": "eventInfo",
		"EventWeight": "weight",
		"GenElectronStatus": 3,
		"GenParticlePdgIds": [
			23
		],
		"GenParticleStatus": 2,
		"GenParticleTypes": [
			"genParticle",
			"genElectron"
		],
		"GenParticles": "genParticles",
		"InputIsData": False,
		"LumiMetadata": "lumiInfo",
		"NumberGeneratedEvents": 30459503,
		"OutputPath": "mc_ee_gen.root",
		"Pipelines": {
			"nocuts_ak5PFJetsCHSL1L2L3": {
				"Consumers": [
					"ZJetTreeConsumer",
					"cutflow_histogram",
				],
				"EventWeight": "eventWeight",
				"Processors": [],
				"Quantities": [
					"genzpt",
					"genzeta",
					"genzphi",
					"genzeta",
					"genzy",
					"genzmass",
					"numberGeneratedEventsWeight",
					"crossSectionPerEventWeight",
					"ngenelectrons",
					"genepluspt",
					"genepluseta",
					"geneplusphi",
					"geneminuspt",
					"geneminuseta",
					"geneminusphi",
					"weight",
				]
			}
		},
		"Processors": [
			"producer:GenParticleProducer",
			"producer:CrossSectionWeightProducer",
			"producer:ZJetNumberGeneratedEventsWeightProducer",
			"producer:EventWeightProducer",
		],
		"Year": 2012,
	}
	cfg["InputFiles"] = configtools.setInputFiles(
		ekppath='/storage/a/dhaitz/skims/2015-08-06_ee-mc-gen_Run2012/kappa_DYJ*.root',
		nafpath='/pnfs/desy.de/cms/tier2/store/user/dhaitz/2015-08-06_ee-mc-gen_Run2012/kappa_DYJ*.root'
	)
	return cfg
