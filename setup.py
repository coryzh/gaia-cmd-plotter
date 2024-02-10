from setuptools import setup, find_packages

setup(
    name='gaia_cmd_plotter',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'matplotlib>=3.3.0',
    ],
    package_data={
        'gaia_cmd_plotter': ['gaia_cmd.mplstyle', 'data/gaia_cmd_background.png'],
    },
    author='Yue Cory Zhao',
    author_email='Yue.Zhao@soton.ac.uk',
    description='A Python package that provides a matplotlib.pyplot.Axes object that displays a Gaia CMD background.',
    url='https://github.com/coryzh/gaia_cmd_plotter',
)
