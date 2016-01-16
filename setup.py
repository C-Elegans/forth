from setuptools import setup
setup(
	name='forthc',
	version='0.1',
	packages=['forthc'],
	license='All rights reserved',
	entry_points = {
		"console_scripts":[
			"forthc = forthc:main"
		]
	}
)
