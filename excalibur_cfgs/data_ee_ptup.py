import data_ee
import configtools

def config():
	cfg = data_ee.config()
	cfg['ElectronPtVariation'] = 'up'
	cfg['ElectronPtVariationFile'] = configtools.getPath() + "/data/electron_scalefactors/ElectronPtVariation.root"
	cfg['Processors'].insert(cfg['Processors'].index('producer:ZJetValidElectronsProducer')+1,'producer:ElectronPtVariator')
	return cfg
