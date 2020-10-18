import requests
import time
  
# api-endpoint 
URL = "http://localhost:5000/shutdown"
  
# sending get request and saving the response as response object 
while True:
    try:
        r = requests.get(url=URL) 
        break
    except Exception as e:
        print(e)
        time.sleep(5)
