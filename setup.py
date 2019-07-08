from setuptools import setup,find_packages

config = {
    'include_package_data': True,
    'description': 'Deep RegulAtory GenOmic Neural Networks (DragoNN)',
    'version': '0.2.7',
    'packages': ['dragonn'],
    'setup_requires': [],
    'install_requires': ['numpy==1.16', 'keras>=2.2.0','tensorflow-gpu>=1.7','deeplift>=0.6.9.0', 'shapely', 'matplotlib==2.2.3', 'plotnine==0.4.0','scikit-learn>=0.20.0', 'pydot_ng==1.0.0', 'h5py','seqdataloader>=0.124','simdna_dragonn','abstention'],
    'dependency_links': [],
    'scripts': [],
    'entry_points': {'console_scripts': ['dragonn = dragonn.__init__:main']},
    'name': 'dragonn'
}

if __name__== '__main__':
    setup(**config)
