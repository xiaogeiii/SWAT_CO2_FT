# -*- coding: UTF-8 -*-
import arcpy
arcpy.env.workspace ="C:/Users/admin/Desktop/shp" #具有多个矢量的文件路径

fcs=arcpy.ListFeatureClasses() #读取矢量数据

fields=['yuyang','F9','F10','F11','F12','F13','F14','F15','F16','F17','F18','F19','jiben']

for fc in fcs:
	outfile = "C:/Users/admin/Desktop/shp/tif"
	cellSize = 759.999999999999
	for field in fields:
		outRaster =outfile+"/"+field
		# Execute FeatureToRaster
		arcpy.FeatureToRaster_conversion(fc, field, outRaster, cellSize)

