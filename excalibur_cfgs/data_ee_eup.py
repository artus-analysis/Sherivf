import data_ee


def config():
	cfg = data_ee.config()
	cfg['ElectronSFVariation'] = 'up'
	cfg['ElectronEffTnPVariation'] = 'up'
	return cfg
