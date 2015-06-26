import subprocess
from osgeo import ogr

def gdalutil(util, command, verbose=True):
    """
    Run GDAL utilities
    - util = string of name of utility ('gdalinfo', 'gdal_translate', etc.)
    - command = string of utility's command
    - verbose = True to print the shell output

    e.g.
    >>> gdalutil('gdalinfo', '-stats C:\\dataset\\test.tif')

    Web page of GDAL utilities:
    http://gdal.org/gdal_utilities.html
    """
    gdaldir = 'E:\\Python27\\ArcGIS10.2\\Lib\\site-packages\\osgeo\\'
    cmd = gdaldir + util + '.exe ' + command
    proc = subprocess.Popen(cmd, stderr=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
    output, errors = proc.communicate()
    if proc.returncode == 0:
        if verbose == True:
            for txt in output.split('\r\n'):
                print txt
    else:
        print 'Command: ' + cmd
        print ' '
        for txt in errors.split('\r\n'):
            print txt
    return
