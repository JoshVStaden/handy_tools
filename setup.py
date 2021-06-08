from setuptools import setup

setup(
    name='handy_tools',
    version='0.1.0',    
    description='A set of handy tools for machine learning',
    url='https://github.com/JoshVStaden/handy_tools.git',
    author='Joshua van Staden',
    author_email='joshvstaden14@gmail.com',
    license='BSD 2-clause',
    packages=['handy_tools'],
    install_requires=['pandas',
                      'numpy',
                      'seaborn',
                      'sklearn',
                      'skimage'                     
                      ],

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',  
        'Operating System :: POSIX :: Linux',        
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)