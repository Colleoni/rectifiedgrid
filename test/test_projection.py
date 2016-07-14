import os
import pyproj
import rectifiedgrid as rg
from rectifiedgrid.demo import get_demo_data
from gisdata import GOOD_DATA
from shapely import geometry
import numpy as np
from scipy import ndimage
from rasterio.warp import reproject, RESAMPLING


class TestInitialization(object):

    def test_reproject(self):
        grid4326 = get_demo_data('line4326')
        grid3035 = get_demo_data('line3035')
        print grid4326
        # print grid3035
        print "AA"
        print np.round(grid3035.reproject(grid4326, RESAMPLING.nearest), 2)
        assert False
