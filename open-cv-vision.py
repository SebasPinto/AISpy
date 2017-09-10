# Using Android IP Webcam video .jpg stream (tested) in Python2 OpenCV3

import urllib
import sys
import cv2
import base64
import numpy as np
import time
import json

from googleapiclient import discovery
from oauth2client.client import GoogleCredentials

# Replace the URL with your own IPwebcam shot.jpg IP:port
url='http://192.168.1.53:8080/shot.jpg'
service = discovery.build('vision', 'v1', developerKey='')


while True:
    # Use urllib to get the image from the IP camera
    
    imgResp = urllib.urlopen(url)
    
    # Numpy to convert into a array
    imgNp = np.array(bytearray(imgResp.read()),dtype=np.uint8)

    
    
    
    # Finally decode the array to OpenCV usable format ;) 
    img = cv2.imdecode(imgNp,-1)
    cv2.imshow('IPWebcam',img)
    ret, buf = cv2.imencode('.jpg', img)
    
    
    service_request = service.images().annotate(body={
            'requests': [{
                'image': {
                    'content': base64.b64encode(buf)
                },
                'features': [{
                    'type': 'LABEL_DETECTION',
                    'maxResults': 10
                }]
            }]
        })
	
	
	# put the image on screen
    
    response = service_request.execute()
    jsonResponse = json.dumps(response['responses'][0], indent=4, sort_keys=True)
    sys.stdout.write("\b" +jsonResponse)
    sys.stdout.flush()
    

    #To give the processor some less stress
    time.sleep(1) 

    # Quit if q is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
