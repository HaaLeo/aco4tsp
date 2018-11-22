from os import path
from setuptools import find_packages, setup
with open(path.join(path.abspath(path.dirname(__file__)), 'README.md'), 'r') as f:
    LONG_DESCRIPTION = f.read()

setup(
    name='aco4tsp',  # PEP8: Packages should also have short, all-lowercase names, the use of underscores is discouraged
    version='0.0.2',
    packages=find_packages(exclude=['*test']),
    description='Implementation of Ant Colony Optimization for the Traveling Salesman Problem.',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    url='https://github.com/HaaLeo/aco4tsp',
    author='Leo Hanisch',
    license='BSD 3-Clause License',
    install_requires=[
        'tsplib95>=0.3.2, <1.0.0',
        'matplotlib>=3.0.2, <4.0.0',
        'networkx==2.1'  # Required by tsplib95 0.3.2
    ],
    project_urls={
        'Issue Tracker': 'https://github.com/HaaLeo/aco4tsp/issues',
        'Changelog': 'https://github.com/HaaLeo/aco4tsp/blob/master/CHANGELOG.md'
    },
    python_requires='>=3.6',
    keywords=[
        'ant',
        'colony',
        'optimization',
        'optimisation',
        'traveling',
        'salesman',
        'problem',
        'TSP',
        'tsp',
        'ACO',
        'aco',
        'TSPLIB95',
        'tsplib95'
        'networkx',
        'visualization',
        'matplotlib'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Developers',
        'Topic :: Education',
        'Topic :: Scientific/Engineering :: Artificial Intelligence'
    ],
    entry_points={
        'console_scripts': [
            'aco4tsp=aco4tsp.main:main'
        ]
    }
)
