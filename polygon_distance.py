#-------------------------------------------------------------------------------
# Name:        Euclidean distance between polygons
# Purpose:     A python script created for replacing the “Conefor Inputs”, a 
#              custom-made GIS extension for ESRI ArcGIS, developed by Jeff 
#              Jenness Enterprises (www.jennessent.com) specifically for 
#              preparing input TXT files for the Conefor software 
#              (www.conefor.org).
# Description: Two TXT files are created from a multi-features polygon 
#              shapefile: 
#              - Nodes: list of the FIDs and areas of each polygon
#              - Distances: minimum Euclidean distance between every pair of 
#                polygons
# Version:     v0.1      
# Author:      Nonpenso
# Created:     08-07-2014
#-------------------------------------------------------------------------------

from osgeo import ogr
from shapely.wkb import loads
import itertools

def poly_dist(inshp, outfolder):
    driver = ogr.GetDriverByName('ESRI Shapefile')
    dataset = driver.Open(inshp, 0)
    layer = dataset.GetLayer()
    shpname = inshp.split('\\')[-1].split('.')[0]

    distfile = outfolder + r"\dist_" + shpname + ".txt"
    nodefile = outfolder + r"\node_" + shpname + ".txt"
    d_obj = open(distfile, "w")
    n_obj = open(nodefile, "w")

    checklist = []
    for ind in itertools.combinations(xrange(layer.GetFeatureCount()),2):
        feat1 = layer.GetFeature(ind[0])
        feat2 = layer.GetFeature(ind[1])

        geom1 = loads(feat1.GetGeometryRef().ExportToWkb())
        geom2 = loads(feat2.GetGeometryRef().ExportToWkb())

        dist = geom1.distance(geom2)
        d_obj.write(str(ind[0]) + '\t' + str(ind[1]) + '\t' + str(dist) + '\n')

        if not ind[0] in checklist:
            checklist.append(ind[0])
            n_obj.write(str(ind[0]) + '\t' + str(geom1.area) + '\n')
        if not ind[1] in checklist:
            checklist.append(ind[1])
            n_obj.write(str(ind[1]) + '\t' + str(geom2.area) + '\n')

    d_obj.close()
    n_obj.close()
