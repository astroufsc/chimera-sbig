from distutils.core import setup

setup(
    name='chimera-sbig',
    version='0.0.1',
    packages=['chimera_sbig', 'chimera_sbig.instruments'],
    url='http://github.com/astroufsc/chimera-sbig',
    license='GPL v2',
    author='Rodrigo Souza',
    author_email='william@iaa.es',
    description='Chimera plugin for Santa Barbara Instrument Group CCD cameras',
    install_requires=['chimera-python', 'enum34']
)
