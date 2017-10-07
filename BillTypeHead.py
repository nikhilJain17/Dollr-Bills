



import os
import io

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]='Credentials.json'

from google.cloud import vision
from google.cloud.vision import types

def billType(s):
    if ("Lincoln" in s):
        return 5
    elif ("Washington" in s):
        return 1
    else:
        return 0

def billValue(bill):
    client = vision.ImageAnnotatorClient()

    file_name = os.path.join(
        os.path.dirname(__file__),
        bill)

    with io.open(file_name, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)

    response = client.web_detection(image=image)
    entities = response.web_detection

    for entity in entities.web_entities:
        value = billType(str(entity.description))
        if(value == 5 or value == 0):
            return value

billList = ['five_dollar.jpeg','twenty_template.png']

for bill in billList:
    print billValue(bill)