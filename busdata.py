import sys
import urllib.request as request
import json
import time

import pandas as pd
import numpy as nm




def collectData(collection_time, collection_intervall, line_to_search):
   """
   Collects data collects movement data by busline @lineToSearch
   @collection_time amount of seconds and time between data collections is @collection_intervall.
   """
   jsonReturn = {}
   jsonReturn['locations'] = []
   
   url = 'http://data.itsfactory.fi/journeys/api/1/vehicle-activity'
   req = request.Request(url=url, method='GET')

   i = 0

   #Doing cordinate collecting while @collection_time is up
   while (i * collection_intervall) < (collection_time):
      data = request.urlopen(req).read().decode('utf8')
      data = json.loads(data)
      recorded = data['body'][0]['recordedAtTime']
      data = pd.DataFrame(data['body'], dtype=object)
      
      #Looping through and finding busses location at the time
      for row in data['monitoredVehicleJourney']:
         if row['lineRef'] == line_to_search:
            jsonReturn['locations'].append({  
            'longitude': row['vehicleLocation']['longitude'],
            'latitude': row['vehicleLocation']['latitude'],
            'time': recorded })
      i = i + 1
      time.sleep(collection_intervall)

   #Writing to json file
   tojson_frame = pd.DataFrame(jsonReturn)
   tojson_frame.to_json("busdata.json")
   return
   


collectData(100,5, '10')

