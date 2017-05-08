# -*- coding: utf-8 -*-
"""
Created on Mon May  8 08:10:19 2017

@author: pcole
"""

import pdb
import numpy as np
from pygmi.raster import iodefs as pio
from pygmi.raster.datatypes import Data
import matplotlib.pyplot as plt
import scipy.interpolate as si
import scipy.signal as ss



def main():
    """ First 2 columns must be x and y """

    filename = r'C:\Work\Programming\pygmi\data\273Grav_2.67_40by39.dat'
    ofile = r'C:\Work\Programming\pygmi\data\gravdata.tif'

    filename = r'C:\Work\Programming\pygmi\data\filt_magdata.csv'
    ofile = r'C:\Work\Programming\pygmi\data\magdata.tif'
    srows = 0
    dlim = None
    xcol = 0
    ycol = 1
    zcol = 2
    dxy = 15

    # This bit reads in the first line to see if it is a header
    pntfile = open(filename)
    ltmp = pntfile.readline()
    pntfile.close()
    ltmp = ltmp.lower()
    isheader = any(c.isalpha() for c in ltmp)

    # Check for comma delimiting
    if ',' in ltmp:
        dlim = ','

    # Set skip rows
    if isheader:
        srows = 1

    # Now read in data

    datatmp = np.genfromtxt(filename, unpack=True, delimiter=dlim,
                            skip_header=srows, usemask=False)

    # Now we interpolate
    xdata = datatmp[xcol]
    ydata = datatmp[ycol]
    zdata = datatmp[zcol]

    # Filter

#    flen = 7
#    z2= ss.medfilt(zdata[:800],21)
#    z2= ss.wiener(zdata[:800],flen)
#
#    plt.plot(zdata[flen:800-flen])
#    plt.plot(z2[flen:800-flen])
#    plt.show()

    points = datatmp[:2].T

    newxdata = np.arange(xdata.min(), xdata.max(), dxy)
    newydata = np.arange(ydata.min(), ydata.max(), dxy)

    newpoints = np.meshgrid(newxdata, newydata)
    newpoints = (newpoints[0].flatten(), newpoints[1].flatten())

    grid = si.griddata(points, zdata, newpoints, method='cubic')

    grid.shape = (newydata.shape[0], newxdata.shape[0])

    grid = grid[::-1]

    # export data
    odat = Data()
    odat.dataid = ''
    odat.tlx = newxdata.min()
    odat.tly = newydata.max()
    odat.xdim = dxy
    odat.ydim = dxy
    odat.nrofbands = 1
    odat.nullvalue = 1e+20
    odat.rows, odat.cols = grid.shape
    odat.data = np.ma.masked_invalid(grid)

    tmp = pio.ExportData(None)
    tmp.ifile = ofile
#    tmp.export_ascii_xyz([odat])
    tmp.export_gdal([odat], 'ENVI')

    # Plotting section

    dataex = (newxdata.min(), newxdata.max(), newydata.min(), newydata.max())
#    plt.imshow(grid, cmap = plt.cm.jet, extent=dataex, origin='upper')


    plt.tricontourf(xdata, ydata, zdata, 40, cmap = plt.cm.jet)

#    plt.plot(xdata, ydata, '.')
    plt.colorbar()
    plt.show()


    pdb.set_trace()







if __name__ == "__main__":
    main()
