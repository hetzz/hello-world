import requests
import json
from PIL import Image

f = open('data.json')
data = json.load(f)

def get_image(id= 621):
    r = requests.get("https://superheroapi.com/api/2831486060232433/"+str(id)+"/image")
    op = dict(r.json())
    with open('characters/pic2.jpg', 'wb') as handle:
            response = requests.get(op['url'], stream=True)

            if not response.ok:
                print (response)

            for block in response.iter_content(1024):
                if not block:
                    break

                handle.write(block)

def create_comic():
    image = Image.open("characters/pic1.jpg") 
    image.show()

get_image()
create_comic()