from PIL import Image, ImageFont, ImageDraw
import pandas as pd


def writeSpeeds(inputimage, outputimage):
   """
   Takes image from @inputimage and writes route with speeds to @outputimage
   """
   leftSide = 23.600829
   rightSide = 23.985991
   changesOnePixelX = 0.000167
   changesOnePixelY = 0.000082
   top = 61.544310
   bottom = 61.416956
   #Reading bus information
   im = Image.open(inputimage).convert('RGBA')
   bus_informations = pd.read_json('busdata.json')
   print(im.size)
   #painting speeds to image
   fnt = ImageFont.truetype('Pillow/Tests/fonts/FreeMono.ttf', 40)
   txt = Image.new('RGBA', im.size, (255,255,255,0))
   d = ImageDraw.Draw(txt)
   for bus_information in bus_informations['locations']:

      longitude = float(bus_information['longitude'])
      latitude = float(bus_information['latitude'])
      print(str(longitude) + ",    " + str(latitude))
      pixelsRight = 0
      pixelsTop = 0
      while longitude > leftSide:
         longitude = longitude - changesOnePixelX
         pixelsRight = pixelsRight + 1

      while latitude > bottom:
         latitude = latitude - changesOnePixelY
         pixelsTop = pixelsTop + 1

      print(str(pixelsRight) + ", " + str(pixelsTop))
      d.text((pixelsRight,pixelsTop), bus_information['speed'], font=fnt, fill=(0,0,0,220))
      
   out = Image.alpha_composite(im, txt)
   out.show()


writeSpeeds('tampere.png', 'tampere1.png')






"""
ylä(y)
61.544310, 23.649674  (Jälkimmäinen on sivusuunnassa)

ala (y)
61.416956, 23.754822


vasen (x)
61.467066, 23.600829

(oikea(x))
61.471190, 23.985991            1.671440972 leveysasteen muutosta/pikselit


muutos x = 0,385162
muutos y = 0,127354

2304 x 1536
"""


