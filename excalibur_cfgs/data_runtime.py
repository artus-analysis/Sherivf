import data

def config():
	cfg = data.config()
	for pipeline in cfg['Pipelines']:
		cfg['Pipelines'][pipeline]['Consumers'].append('RunTimeConsumer')
	return cfg
