import geopandas as gpd
from shapely.geometry import Polygon
import numpy as np


#load in communities
richmond = gpd.read_file('/Users/hwheelen/Documents/GitHub/COI_Splitting/Voter_Precincts_RichmondVA/RichmondCOIs.shp')

#calculate population of each community and add it to a new column


#load in maps
map1 = gpd.read_file('/Users/hwheelen/Documents/GitHub/VA-gerrymander/Maps/Special Master Map/Court Order Map/Shapefile/New_Map.shp)

map2 = gpd.read_file('/Users/hwheelen/Documents/GitHub/VA-gerrymander/Maps/Enacted map/enacted.shp')

map3 = gpd.read_file('/Users/hwheelen/Documents/GitHub/VA-gerrymander/Maps/Reform map/Reform map all districts.shp')


#first, identify which maps split which communities


#next, calculate how many components each community is split into

#next, calculate Laakso and Taagepera number of compoonents of each community
for split in splits:
    #aggregate population into each component
    #define each component of split
    #loop through each component
        #calculate proportion of area
        comp_prop = 
        comp_prop_pop = 
    #add up squares of each prop
    #save 1/(sum of squares) as effective number of components

#then calculate MGGG split edges 


#calculate Jacobs splitting

#calculate effective number of components, or Taagepera components
