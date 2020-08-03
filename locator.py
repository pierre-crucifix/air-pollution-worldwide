import pandas as pd
import numpy as np
from geopandas.tools import geocode
from time import sleep

#Import database
city_for_locator_df = pd.read_csv(r".\Locations\city_listing_db.csv", index_col=0)

#Merge multiple rows regarding the same cities in order to realize as few requests as possible to Nominatim
city_for_locator_df.drop_duplicates(subset=['iso3','City/Town'], keep='first', inplace=True)

#Creating a col for longitude and one for the latitude
city_for_locator_df['long']=np.nan
city_for_locator_df['lat']=np.nan

#Preallocation before the loop
geo = geocode("Belgium", provider='nominatim', user_agent="air-pollution-worldwide")
long_and_lat=geo.to_crs('EPSG:4326')
sleep(2) #timer

#'Massive' Requests to Nominatim, one for each city
for i in city_for_locator_df.index:
    print(i)

    try:
        geo=geocode(city_for_locator_df.at[i,'Country'] + " " + city_for_locator_df.at[i,'City/Town'], provider='nominatim', user_agent="air-pollution-worldwide")

        # geo.to_crs({'init': 'epsg:3395'}) #Mercator projection
        long_and_lat=geo.to_crs('EPSG:4326') #WGS84 projection

        city_for_locator_df.at[i,'long']=long_and_lat.loc[0,"geometry"].x
        city_for_locator_df.at[i,'lat']=long_and_lat.loc[0,"geometry"].y
    except:
        print("problem while retriving long. and lat. of city "+str(i)+", skipped")

    sleep(2)

#Saving the results in order to not ask them again
city_for_locator_df.to_csv(r".\Locations\city_locations_db.csv")