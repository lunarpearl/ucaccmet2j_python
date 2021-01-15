#---part 1--- 
import json
with open('precipitation.json') as data:
    #finding out the station name of Seattle
    with open('stations.csv') as stations:
        headers = stations.readline()
        stations_info = []
        for city in stations:
            location, state, station = city.strip().split(',')
            stations_info.append({'location': location,'state':state,'station':station})
        station_Seattle = stations_info[1]['station']
    #filtering through data for Seattle and creating lists with precipitation info for each day(available in the data) of each separate month
    precipitation = json.load(data)
    precipitation_jan = []
    precipitation_feb = []
    precipitation_mar = []
    precipitation_apr = []
    precipitation_may = []
    precipitation_jun = []
    precipitation_jul = []
    precipitation_aug = []
    precipitation_sep = []
    precipitation_oct = []
    precipitation_nov = []
    precipitation_dec = []
    for measurement in precipitation:
        if measurement['station']== station_Seattle:
            #value is divided by 10 as data shows percepitation in 10th of mm and we need to calculate information in mm
            if '2010-01' in measurement['date']:
                precipitation_jan.append(measurement['value']/10)
            elif '2010-02' in measurement['date']:
                precipitation_feb.append(measurement['value']/10)
            elif '2010-03' in measurement['date']:
                precipitation_mar.append(measurement['value']/10)
            elif '2010-04' in measurement['date']:
                precipitation_apr.append(measurement['value']/10)
            elif '2010-05' in measurement['date']:
                precipitation_may.append(measurement['value']/10)
            elif '2010-06' in measurement['date']:
                precipitation_jun.append(measurement['value']/10)
            elif '2010-07' in measurement['date']:
                precipitation_jul.append(measurement['value']/10)
            elif '2010-08' in measurement['date']:
                precipitation_aug.append(measurement['value']/10)
            elif '2010-09' in measurement['date']:
                precipitation_sep.append(measurement['value']/10)
            elif '2010-10' in measurement['date']:
                precipitation_oct.append(measurement['value']/10)
            elif '2010-11' in measurement['date']:
                precipitation_nov.append(measurement['value']/10)
            elif '2010-12' in measurement['date']:
                precipitation_dec.append(measurement['value']/10)
    #making a list with monthly totals for Seattle
    totals = [sum(precipitation_jan),sum(precipitation_feb),sum(precipitation_mar),sum(precipitation_apr),sum(precipitation_may),sum(precipitation_jun),sum(precipitation_jul),sum(precipitation_aug),sum(precipitation_sep),sum(precipitation_oct),sum(precipitation_nov),sum(precipitation_dec)]
    with open('monthly_totals.json','w') as file:
        #save the results
        json.dump(totals,file, indent = 4)
#---part 2---
#calculating the total precepitation for 2010 in Seattle
total_2010 = sum(totals)
#
relative_precepitation = []
for month in totals:
    relative_precepitation.append(round(month/total_2010,1))
print(relative_precepitation)