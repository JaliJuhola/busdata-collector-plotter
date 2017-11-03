from busdata import collectData
from routespeeds import writeSpeeds

import sys

# Collecting data about bus number @argv[3] for @argv[1] seconds with @argv[2] intervall 
if len(sys.argv) == 4 and sys.argv[1].isdigit() and sys.argv[2].isdigit():
   collectData((int)(sys.argv[1]),(int)(sys.argv[2]), str(sys.argv[3]))
else:
   #using default values
   collectData(100, 5, '6')

writeSpeeds('tampere.png', 'tampere1.png')
