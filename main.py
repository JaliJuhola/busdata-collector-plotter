from busdata import collectData

import sys


if len(sys.argv) == 4 and sys.argv[1].isdigit() and sys.argv[2].isdigit():
   collectData((int)(sys.argv[1]),(int)(sys.argv[1]), str(sys.argv[3]))
else:
   #using default values
   collectData(40, 5, '6')
