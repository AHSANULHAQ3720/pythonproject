import requests
import pandas as pd

x = requests.get("https://bahriatownservices.com/electric-dept.html")
print(x.status_code)
print(pd.DataFrame(x.headers))
print(x.request.body)

print("Header request sent:" + x.headers['date'])
print("Content Type:" + x.headers["Content-Type"])
# print("Text:",x.text[250:750])
print("Encoding:" + x.encoding)
