import data_ee


def config():
	cfg = data_ee.config()
	cfg['ElectronSFVariation'] = 'down'
	cfg['ElectronEffTnPVariation'] = 'down'
	return cfg
