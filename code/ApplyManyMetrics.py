import geopandas as gpd
from shapely.geometry import Polygon
import numpy as np

grid = gpd.read_file('/Users/hwheelen/Documents/GitHub/COI_Splitting/Hypothetical Data/RichmondGrid.shp')

boundary = gpd.read_file('/Users/hwheelen/Documents/GitHub/COI_Splitting/Hypothetical Data/splits/Boundary.shp')

half = gpd.read_file('/Users/hwheelen/Documents/GitHub/COI_Splitting/Hypothetical Data/splits/half.shp')

split_25_75 = gpd.read_file('/Users/hwheelen/Documents/GitHub/COI_Splitting/Hypothetical Data/splits/split_25_75.shp')

split_10_90 = gpd.read_file('/Users/hwheelen/Documents/GitHub/COI_Splitting/Hypothetical Data/splits/split_10_90.shp')

quarters = gpd.read_file('/Users/hwheelen/Documents/GitHub/COI_Splitting/Hypothetical Data/splits/split_quarters.shp')

four_uneven = gpd.read_file('/Users/hwheelen/Documents/GitHub/COI_Splitting/Hypothetical Data/splits/split_four_uneven.shp')

#make list of types of splits we want to calculate
splits = [boundary, half, split_25_75, split_10_90, quarters, four_uneven]


#first calculate simple splits aka how many times the community is cut


#then calculate MGGG split edges 


#calculate Jacobs splitting

#calculate effective number of components, or Taagepera components
for split in splits:
    #aggregate population into each component
    #define each component of split
    #loop through each component
        #calculate proportion of area
        comp_prop = 
        comp_prop_pop = 
    #add up squares of each prop
    #save 1/(sum of squares) as effective number of components