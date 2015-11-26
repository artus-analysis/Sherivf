import mc

def config():
	cfg = mc.config()
	for pipeline in cfg['Pipelines']:
		cfg['Pipelines'][pipeline]['Consumers'].append('RunTimeConsumer')
	return cfg
