try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
with open("README.rst", 'r') as f:
    long_description = f.read()

setup(
    name = "ecm_gooey_path",
    version = "1.0",
    author = "Jean-Emmanuel Longueville, Myriam Hanna",
    author_email = "jean.emmanuel.longueville(@)univ-poitiers.fr",
    description = "Test project",
    license = "MIT",
    include_package_data=True,
    zip_safe = False,
    packages= find_packages(),
    install_requires=['pandas',
                      'numpy',
                      'argparse',
                      'pyaml',
                      'gooey',
                      'importlib',],
    long_description=long_description,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: ",
    ],
    entry_points={
        'console_scripts':  ['ecm-gui = ecm.main_gui:main',]
        },
    data_files=[
        ('lib/python3.9/dist-packages/ecm/img',
            ['ecm/img/config_icon.png','ecm/img/program_icon.png' ])
        ],
)