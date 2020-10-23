import requests
import time 
  
# api-endpoint 
URL = "http://localhost:5000/"
  
# sending get request and saving the response as response object 
while True:
    try:
        r = requests.get(url=URL)
        if r.status_code == 200:
            break
        raise AssertionError("Status Code is {}".format(r.status_code))
    except Exception as e:
        print(e)
        time.sleep(5)
