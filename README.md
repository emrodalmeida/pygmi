##Notice at 22 September 2014
PyGMI release 2.2.2 is now out! It contains numerous bugfixes including some relating to the multiprocessing modifications to the potential field calculations. Please make sure you are using this version.

#PyGMI Readme

PyGMI stands for *Python Geophysical Modelling and Interpretation*. It is a modelling and interpretation suite aimed at magnetic, gravity and other datasets. It includes:
* Magnetic and Gravity 3D forward modelling
* Cluster Analysis
* Routines for cutting, reprojecting and doing simple modifications to data
* Convenient display of data using pseudo-color, ternary and sunshaded representation

It is released under the Gnu General Public License version 3.0

For license information see the file LICENSE.txt

##Requirements
PyGMI will run on both Windows and Linux. It should be noted that the main development is done in Python 3.4 on Windows.

PyGMI is developed and has been tested with the following libraries in order to function:

* Python 3.4.1
* NumPy 1.8.2
* SciPy 0.14.0
* Matplotlib 1.3.1
* PyQt 4.10.4
* GDAL 1.11.0
* numexpr 2.4

It is possible that it migt work on earlier versions, especially on non-windows operating systems. Under windows, there are compiled .pyd files (python version of a dll) which require the NumPy and Python version to match. However, for actual releases, I do post windows binaries which include a standalone python distribution (that will not interfere with existing installations), so this should not be a problem.

##Installation

In general, if you satisfy the requirements, and have installed PyGMI as a library (python setup.py install), you can run PyGMI by using the following commands:

	import pygmi
	pygmi.main()

###Installation - Windows (Fast)
On Windows, the simplest is to either use WinPython or download an installer which includes WinPython.

The installer can be found on [Google Drive](https://209f493642c7e79b2a878320662bfff73a2946cf.googledrive.com/host/0B6BP_95afhWzN01tZzh5VG1aNk0/) and under the release section of github.

WinPython does not by default install itself into your registry, so it will not conflict with other versions of python.