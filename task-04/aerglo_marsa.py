import argparse
import requests
import urllib, json
import json

ap = argparse.ArgumentParser()
ap.add_argument("-d","--date",required=True,help="date when the picture was taken")
args = vars(ap.parse_args())
i="https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?earth_date={}&api_key=NXMc2il18EtWyCAm2Zm7NDM6j5I5gZQXM36SwRni".format(args["date"])
url = i
res=urllib.request.urlopen(url)
data= json.loads(res.read())
file = "nasa_mars.json"
with open(file, 'w') as file_object:
    json.dump(data, file_object)
