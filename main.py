from flask import Flask
import ee
from datetime import datetime, timedelta


app = Flask(__name__)


@app.route('/')
def processSomeData():

    print('started process')
    
    geocord = [11.589411596780081, 48.149503277976365]

    print('Initialising...')
    ee.Initialize()    

    # Create Earth Engine point
    point = ee.Geometry.Point(geocord)

    # Initial date of interest (inclusive).
    i_date = '2024-07-26'

    # Final date of interest (exclusive).
    f_date = '2024-06-26'

    # Import the MODIS land cover collection.
    lc = ee.ImageCollection('MODIS/006/MCD12Q1')

    scale = 1000  # scale in meters

    print('Getting info...')
    # Print the land cover type at the point.
    #land_cover = lc.first().sample(point, scale).first().get('LC_Type1').getInfo()
    
    print('Land cover value at urban point is:', land_cover)


    return land_cover
