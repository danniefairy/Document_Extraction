import requests 
import sys
  
# api-endpoint 
URL = "http://localhost:5000/shutdown"
  
# sending get request and saving the response as response object 
try:
    r = requests.get(url = URL) 
except Exception as e:
    print(e)
    sys.exit(1)