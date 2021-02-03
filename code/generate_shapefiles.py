#generates 10 by 10 grid with bounds of chosen city

import geopandas as gpd
from shapely.geometry import Polygon
import numpy as np

#import any shapefile, really
bounds = gpd.read_file('/Users/hwheelen/Documents/GitHub/COI_Splitting/Voter_Precincts_RichmondVA/VoterPrecinct.shp')
xmin,ymin,xmax,ymax =  bounds.total_bounds

#adjust bounds until you have a 10 by 10 or other grid you want
width = (ymax - ymin)/10
height = (xmax - xmin)/10
rows = 10
cols = 10
XleftOrigin = xmin
XrightOrigin = xmin + width
YtopOrigin = ymax
YbottomOrigin = ymax- height

#create polygons and save
polygons = []
for i in range(cols):
   Ytop = YtopOrigin
   Ybottom =YbottomOrigin
   for j in range(rows):
       polygons.append(Polygon([(XleftOrigin, Ytop), (XrightOrigin, Ytop), (XrightOrigin, Ybottom), (XleftOrigin, Ybottom)])) 
       Ytop = Ytop - height
       Ybottom = Ybottom - height
   XleftOrigin = XleftOrigin + width
   XrightOrigin = XrightOrigin + width

grid = gpd.GeoDataFrame({'geometry':polygons})

#add population
grid['cont_pop'] = 10
grid['var_pop'] = 10
for index, row in grid.iterrows():
    n = np.random.randint(0,20,size=1)
    grid.var_pop[index] = n

print('cont_pop sum: ',grid.cont_pop.sum())
print('var_pop sum: ',grid.var_pop.sum())
grid = grid[['cont_pop', 'var_pop','geometry' ]]


#save shapefile
grid.to_file('/Users/hwheelen/Documents/GitHub/COI_Splitting/Hypothetical Data/RichmondGrid.shp')



#make something that splits in half by adjusting bounds again
width = (ymax - ymin)/2
height = (xmax - xmin)
rows = 1
cols = 2
XleftOrigin = xmin
XrightOrigin = xmin + width
YtopOrigin = ymax
YbottomOrigin = ymax- height

#create polygons and save
polygons = []
for i in range(cols):
   Ytop = YtopOrigin
   Ybottom =YbottomOrigin
   for j in range(rows):
       polygons.append(Polygon([(XleftOrigin, Ytop), (XrightOrigin, Ytop), (XrightOrigin, Ybottom), (XleftOrigin, Ybottom)])) 
       Ytop = Ytop - height
       Ybottom = Ybottom - height
   XleftOrigin = XleftOrigin + width
   XrightOrigin = XrightOrigin + width

grid = gpd.GeoDataFrame({'geometry':polygons})
grid.to_file('/Users/hwheelen/Documents/GitHub/COI_Splitting/Hypothetical Data/splits/half.shp')



#make something that splits 75/25 by adjusting bounds again
width = (ymax - ymin)/4
height = (xmax - xmin)
rows = 1
cols = 2
XleftOrigin = xmin
XrightOrigin = xmin + width + width + width
YtopOrigin = ymax
YbottomOrigin = ymax- height

#create polygons and save
polygons = []
for i in range(cols):
   Ytop = YtopOrigin
   Ybottom =YbottomOrigin
   for j in range(rows):
       polygons.append(Polygon([(XleftOrigin, Ytop), (XrightOrigin, Ytop), (XrightOrigin, Ybottom), (XleftOrigin, Ybottom)])) 
       Ytop = Ytop - height
       Ybottom = Ybottom - height
   XleftOrigin = XleftOrigin + width
   XrightOrigin = XrightOrigin + width

grid = gpd.GeoDataFrame({'geometry':polygons})
grid.to_file('/Users/hwheelen/Documents/GitHub/COI_Splitting/Hypothetical Data/splits/split_25_75.shp')

#make something that splits 10/90 by adjusting bounds again
width = (ymax - ymin)/10
height = (xmax - xmin)
rows = 1
cols = 2
XleftOrigin = xmin
XrightOrigin = xmin + width + width + width + width + width + width + width + width + width
YtopOrigin = ymax
YbottomOrigin = ymax- height

#create polygons and save
polygons = []
for i in range(cols):
   Ytop = YtopOrigin
   Ybottom =YbottomOrigin
   for j in range(rows):
       polygons.append(Polygon([(XleftOrigin, Ytop), (XrightOrigin, Ytop), (XrightOrigin, Ybottom), (XleftOrigin, Ybottom)])) 
       Ytop = Ytop - height
       Ybottom = Ybottom - height
   XleftOrigin = XleftOrigin + width
   XrightOrigin = XrightOrigin + width

grid = gpd.GeoDataFrame({'geometry':polygons})
grid.to_file('/Users/hwheelen/Documents/GitHub/COI_Splitting/Hypothetical Data/splits/split_10_90.shp')

#make something that splits into quarters
width = (ymax - ymin)/2
height = (xmax - xmin)/2
rows = 2
cols = 2
XleftOrigin = xmin
XrightOrigin = xmin + width 
YtopOrigin = ymax
YbottomOrigin = ymax- height

#create polygons and save
polygons = []
for i in range(cols):
   Ytop = YtopOrigin
   Ybottom =YbottomOrigin
   for j in range(rows):
       polygons.append(Polygon([(XleftOrigin, Ytop), (XrightOrigin, Ytop), (XrightOrigin, Ybottom), (XleftOrigin, Ybottom)])) 
       Ytop = Ytop - height
       Ybottom = Ybottom - height
   XleftOrigin = XleftOrigin + width
   XrightOrigin = XrightOrigin + width

grid = gpd.GeoDataFrame({'geometry':polygons})
grid.to_file('/Users/hwheelen/Documents/GitHub/COI_Splitting/Hypothetical Data/splits/split_quarters.shp')

#make something that splits into 4 uneven pieces
width = (ymax - ymin)/4
height = (xmax - xmin)/2
rows = 2
cols = 2
XleftOrigin = xmin
XrightOrigin = xmin + width + width + width
YtopOrigin = ymax
YbottomOrigin = ymax- height

#create polygons and save
polygons = []
for i in range(cols):
   Ytop = YtopOrigin
   Ybottom =YbottomOrigin
   for j in range(rows):
       polygons.append(Polygon([(XleftOrigin, Ytop), (XrightOrigin, Ytop), (XrightOrigin, Ybottom), (XleftOrigin, Ybottom)])) 
       Ytop = Ytop - height
       Ybottom = Ybottom - height
   XleftOrigin = XleftOrigin + width
   XrightOrigin = XrightOrigin + width

grid = gpd.GeoDataFrame({'geometry':polygons})
grid.to_file('/Users/hwheelen/Documents/GitHub/COI_Splitting/Hypothetical Data/splits/split_four_uneven.shp')

#finally, make a boundary around the border
width = (ymax - ymin)
height = (xmax - xmin)
rows = 1
cols = 1
XleftOrigin = xmin
XrightOrigin = xmin + width 
YtopOrigin = ymax
YbottomOrigin = ymax- height

#create polygons and save
polygons = []
for i in range(cols):
   Ytop = YtopOrigin
   Ybottom =YbottomOrigin
   for j in range(rows):
       polygons.append(Polygon([(XleftOrigin, Ytop), (XrightOrigin, Ytop), (XrightOrigin, Ybottom), (XleftOrigin, Ybottom)])) 
       Ytop = Ytop - height
       Ybottom = Ybottom - height
   XleftOrigin = XleftOrigin + width
   XrightOrigin = XrightOrigin + width

grid = gpd.GeoDataFrame({'geometry':polygons})
grid.to_file('/Users/hwheelen/Documents/GitHub/COI_Splitting/Hypothetical Data/splits/Boundary.shp')