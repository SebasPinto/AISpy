import urllib
import sys
import cv2
import base64
import numpy as np
import json

from googleapiclient import discovery
from oauth2client.client import GoogleCredentials

service = discovery.build('vision', 'v1', developerKey='AIzaSyDZOfi1tSK8EgmDbVjXbMNo5KkJblBAv74')

def detectImage(url):
	# Use urllib to get the image from the IP camera
    
    imgResp = urllib.urlopen(url)
    
    # Numpy to convert into a array
    imgNp = np.array(bytearray(imgResp.read()),dtype=np.uint8)

    
    
    
    # Finally decode the array to OpenCV usable format ;) 
    img = cv2.imdecode(imgNp,-1)
    #cv2.namedWindow('IPWebcam',cv2.WINDOW_NORMAL)
    #cv2.resizeWindow('image', 600,600)
    #cv2.imshow('IPWebcam',img)
    ret, buf = cv2.imencode('.jpg', img)
    
    
    service_request = service.images().annotate(body={
            'requests': [{
                'image': {
                    'content': base64.b64encode(buf)
                },
                'features': [{
                    'type': 'LABEL_DETECTION',
                    'maxResults': 1
                }]
            }]
        })
	
	
	# put the image on screen
    
    response = service_request.execute()
    jsonResponse = json.dumps(response['responses'][0], indent=4, sort_keys=True)
    #sys.stdout.write("\b" +jsonResponse)
    #sys.stdout.flush()
    res = json.loads(jsonResponse)
    return res['labelAnnotations'][0]['description']


 

