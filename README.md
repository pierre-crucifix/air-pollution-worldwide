# air-pollution-worldwide
Investigation of air quality disparities in cities around the world

### Idea

It is common to hear that Brussels, London, New Delhi or Jakarta are polluted cities. Indeed, this is a well-known fact but it is way less clear how they are relatively polluted in comparison of each other as well as compared to World Health Organization norms. 

Therefore, this project had the mission to offer a better overview of the situation worldwide.

### Origin of analyzed data

database: _aap_air_quality_database_2018_v14_, obtained on https://www.who.int/airpollution/data/cities/en/

### Main results

The first two following figures give an overview by comparing the values region per region, with a data point per captor (annual mean). Indeed, it is easy to find online maps showing air pollution in quasi-real time, but they have the drawback to not give an overview all along the year. Thus unit of measure are the PM2.5 and PM10, revealing fine particulate in the air. To give an idea about reasonable limits, WHO set limit guidelines to max 10 μg/m3 PM2.5 and 20 μg/m3 PM10 (annual mean).

![SwarmPlot2.5](https://github.com/pierre-crucifix/air-pollution-worldwide/blob/master/Plots/SwarmPlot2.5.png "Logo Title Text 1")

![SwarmPlot10](https://github.com/pierre-crucifix/air-pollution-worldwide/blob/master/Plots/SwarmPlot10.png "Logo Title Text 1")

LMIC means Low and Middle Income Countries, while HIC is used for High Income Countries.

#### Interactive map

To go further, I have built an interactive map that can be downloaded [here](https://github.com/pierre-crucifix/air-pollution-worldwide/blob/master/MapWithPollutionPerCity.html) (Its name is _MapWithPollutionPerCity.html_ and this file is given at the root of this repo). The following screenshot reveals a preview of this map, with great differences per region. 



![Screenshot_Interactive_Map_Air_Pollution](https://github.com/pierre-crucifix/air-pollution-worldwide/blob/master/Plots/Screenshot_Interactive_Map_Air_Pollution.png "Logo Title Text 1")

In the [original file](https://github.com/pierre-crucifix/air-pollution-worldwide/blob/master/MapWithPollutionPerCity.html), you have the possibility to zoom in all around the world, and you can click on the cities to know the measured values (Annual Average of PM2.5 and PM10).
