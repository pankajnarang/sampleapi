import  requests

endpoint    =   "https://httpbin.org/anything"
response    =   requests.get(endpoint, json={"query": "Hello World"})
print(response.json())
print(response.status_code)

endpoint01  =   "http://localhost:8000/demo/"
response01    =   requests.get(endpoint01)
print(response01.json())
print(response01.status_code)
