from flask import Flask
import ee
from datetime import datetime, timedelta


app = Flask(__name__)

geocord = [11.589411596780081, 48.149503277976365]

@app.route('/')
def processSomeData(geocord):
    ee.Initialize()

    # Create Earth Engine point
    point = ee.Geometry.Point(geocord)

    # Get today's date
    f_date = datetime.today().strftime('%Y-%m-%d')

    # Calculate the start date (one month prior)
    i_date = (f_date - timedelta(days=30)).strftime('%Y-%m-%d')

    # Import the MODIS land cover collection.
    lc = ee.ImageCollection('MODIS/006/MCD12Q1')

    scale = 1000  # scale in meters

    # Print the land cover type at the point.
    land_cover = lc.first().sample(point, scale).first().get('LC_Type1').getInfo()
    
    print('Land cover value at urban point is:', land_cover)


    return land_cover
