from distutils.core import setup

setup(
    # Application name:
    name="PyPomVisualiser",

    # Version number (initial):
    version="0.1.0",

    # Application author details:
    author="William Moorhouse",
    author_email="w-mg-moorhouse@gmail.com",

    # Packages
    package_dir= {'': 'src'},

    # Include additional files into the package
    include_package_data=True,

    # Details
    #url="http://pypi.python.org/pypi/MyApplication_v010/",

    #
    license="LICENSE",
    description="Maven Pom Visualisation tool, written in Python(obviously).",

    # long_description=open("README.txt").read(),

    # Dependent packages (distributions)
    install_requires=[
        "tkinter"
    ],
)
