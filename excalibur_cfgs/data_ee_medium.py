import configtools
import data_ee

def config():
	cfg = data_ee.config()
	cfg['ElectronID'] = 'vbft95_medium'
	return cfg